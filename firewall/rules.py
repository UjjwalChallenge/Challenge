from collections import defaultdict as dd
from firewall.packet import IP
from firewall.utils import dec_to_bin


class DirectionNode:
    """ A node of the RulesDataStore tree which stores a direction and reference of
    the protocol nodes connected to it
    """

    def __init__(self, direction):
        self.root = direction
        self.protocols = {}


class ProtocolNode:
    """ A node of the RulesDataStore tree which stores a Protocol and reference of
    the port nodes connected to it
    """

    def __init__(self, protocol):
        self.root = protocol
        self.ports = {}


class IPTrieNode:
    """ A node of the RulesDataStore tree that forms the basis of Trie data structure used to store the IP Addresses
    """

    def __init__(self, node):
        self.root = node
        self.children = {"0": None, "1": None}


class PortNode:
    """ A node of the RulesDataStore which stores a Port and  reference of
    the root of a Trie data structure used to store IP Addresses
    """

    def __init__(self, port):
        self.root = port
        self.ip_trie_root = IPTrieNode('\0')

    def add_ips(self, ip_addrs):
        """ A function that is used to store ip addresses in a Port node's trie.
        Args:
            ip_addrs(list): list of ip addresses that need to be connected to an incoming port.
        """
        if len(ip_addrs) > 1:  # An IP range was specified
            start = ip_addrs[0].ip_obj
            end = ip_addrs[1].ip_obj
            while start <= end:
                # Iterates over the IP range and adds them to the Port node
                ip_to_add = IP(start.compressed)
                self.add_ip(ip_to_add)
                start += 1

        else:
            self.add_ip(ip_addrs[0])

    def add_ip(self, ip_addr):
        """ A function that is used to store an ip address in a Port node's trie
        Args:
            ip_addr(string): The ip address that needs to be added to the Port node's trie
        """
        octets = ip_addr.get_octets()
        temp = self.ip_trie_root
        for octet in octets:
            bin_octet = dec_to_bin(octet)
            for digit in bin_octet:
                if temp.children[digit]:
                    temp = temp.children[digit]
                else:
                    new_node = IPTrieNode(digit)
                    temp.children[digit] = new_node
                    temp = new_node

    def search_ip(self, ip_addr):
        """ A function that is used to search an ip address in the Port node's ip trie
        Args:
            ip_addr(string): The ip address which needs to be matched
        Returns:
            True if the ip address matched. False otherwise

        """
        octets = ip_addr.get_octets()
        temp = self.ip_trie_root
        for octet in octets:
            bin_octet = dec_to_bin(octet)
            for digit in bin_octet:
                if temp.children[digit]:
                    temp = temp.children[digit]
                else:
                    return False

        return True


class HeadNode:
    """ A node that represents the starting point of RulesDataStore Tree
    """

    def __init__(self, node=None):
        self.root = node
        self.directions = {}


class RulesDataStore(object):

    def __init__(self):
        self.root = HeadNode('\0')
        self.added = dd(lambda: False)

    def add_rule(self, rule_data, rule_str):
        """ A function that is used to add a rule to the RulesDataStore Tree

        Args:
            rule_data(dict): A dict object containing the details of the rule that needs to be added
            rule_str(string): A string containing the details of the rule that needs to be added
        """

        # checks if the rule already exists in the DataStore
        if self.added[rule_str]:
            return

        self.added[rule_str] = True

        direction = rule_data['direction']
        protocol = rule_data['protocol']
        ports = rule_data['ports']
        ip_addrs = rule_data['ips']

        temp = self.root  # root of the HeadNode

        """
        Level by level tree traversal which creates the appropriate nodes if absent
        in accordance with the rule data received 
        """

        if direction.val in temp.directions:
            temp = temp.directions[direction.val]
        else:
            temp.directions[direction.val] = DirectionNode(direction)
            temp = temp.directions[direction.val]

        if protocol.val in temp.protocols:
            temp = temp.protocols[protocol.val]
        else:
            temp.protocols[protocol.val] = ProtocolNode(protocol)
            temp = temp.protocols[protocol.val]

        # if the rule contains a range of ports
        if len(ports) > 1:
            for p in range(ports[0].val, ports[1].val + 1):
                new_port_node = PortNode(p)
                new_port_node.add_ips(ip_addrs)  # Adding ip addresses to a port

                if p in temp.ports:
                    temp.ports[p].add_ips(ip_addrs)
                else:
                    temp.ports[p] = new_port_node

        else:
            if ports[0] in temp.ports:
                temp.ports[ports[0].val].add_ips(ip_addrs)
            else:
                temp.ports[ports[0].val] = PortNode(ports[0])
                temp.ports[ports[0].val].add_ips(ip_addrs)

    def search(self, packet):
        """ A function that is used to check if a packet matches any of the rules present in the RulesDataStore
        Args:
            packet(packet.Packet): An object that contains the details of the packet that needs to be searched.
        Returns:
            A (boolean,string) tuple

            (True, Valid message): If the packet matched a rule in the DataStore
            (False, Invalid message):  If the packed didn't match a single rule in the DataStore
        """
        temp = self.root
        if packet.direction.val in temp.directions:
            temp = temp.directions[packet.direction.val]
        else:
            return False, "Direction not accepted"

        if packet.protocol.val in temp.protocols:
            temp = temp.protocols[packet.protocol.val]
        else:
            return False, "Protocol not accepted"

        if packet.port.val in temp.ports:
            temp = temp.ports[packet.port.val]
        else:
            return False, "Port not accepted"

        if not temp.search_ip(packet.ip):
            return False, "IP not accepted"

        return True, "Valid"
