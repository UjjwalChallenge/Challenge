from abc import ABC, abstractmethod
from ipaddress import ip_address


class PacketComponent(ABC):
    """ An Abstract class that forms the interface for the different types of components in a Packet
    """

    @abstractmethod
    def is_valid(self):
        """ An abstract function to check the validity of a component
        """
        pass


class IP(PacketComponent):
    """ A type of PacketComponent used to manage the ip address received from the user
    """

    def __init__(self, ip_addr):
        """
        Args:
            ip_addr(string): The ip address inputted by the user
        """
        self.val = ip_addr
        try:
            self.ip_obj = ip_address(self.val)
        except ValueError:
            pass
        self.octets = self.val.split(".")

    def get_octets(self):
        """
        Returns:
           self.octets(list): All the octets in the received ip address.
        """
        return self.octets

    def is_valid(self):
        """ Checks if the received ip address is valid or not
        Returns:
            True if ip address is valid, False otherwise
        """
        if self.ip_obj:
            return True
        return False


class Direction(PacketComponent):
    """ A type of PacketComponent used to manage the direction received from the user

    class variables:
        DIRECTIONS(list) : Stores a list of permissible directions
    """
    DIRECTIONS = ["inbound", "outbound"]

    def __init__(self, direction):
        self.val = direction

    def is_valid(self):
        """ Checks if the received direction is valid or not.

        Returns:
            True if ip direction is valid, False otherwise
        """
        return self.val in Direction.DIRECTIONS


class Port(PacketComponent):
    """ A type of PacketComponent used to manage the port received from the user
    """

    def __init__(self, port):
        self.val = int(port)

    def is_valid(self):
        """ Checks if the received port is valid or not
        Returns:
            True if the port is valid, False otherwise
        """
        return 1 <= self.val <= 65535


class Protocol(PacketComponent):
    """A type of PacketComponent used to manage the protocol received from the user

    class variables:
        PROTOCOLS (list) : Stores a list of permissible protocols
    """
    PROTOCOLS = ["UDP", "TCP"]

    def __init__(self, protocol):
        self.val = protocol

    def is_valid(self):
        return self.val in Protocol.PROTOCOLS


class Packet(object):
    """ A class that is used to store different types of PacketComponent objects. 
    """
    def __init__(self, data):
        self.ip = IP(data['ip'])
        self.direction = Direction(data['direction'])
        self.port = Port(data['port'])
        self.protocol = Protocol(data['protocol'])

    def is_valid(self):
        """ A function to check the validity of a packet.

        Returns:
            True if the packet is valid. False otherwise.
        """
        if not self.direction.is_valid():
            return False, "Invalid Direction"

        if not self.protocol.is_valid():
            return False, "Invalid Protocol"

        if not self.port.is_valid():
            return False, "Invalid Port"

        if not self.ip.is_valid():
            return False, "Invalid IP"

        return True, "Valid packet"


class PacketComponentFactory(ABC):
    """ An abstract class that forms the blueprint of factory classes used to generate
    a collection of PacketComponent
    """

    @abstractmethod
    def generate(self):
        """
        Returns:
            A collection of PacketComponent
        """
        pass


class IPFactory(PacketComponentFactory):
    """ A factory class that is used to generate a collection of type IP
    """

    def __init__(self, ips):
        """
        Args:
            ips(list): A list of ip address strings inputted by the user.
        """
        self.ips = ips

    def generate(self):
        """ Generates a collection of type IP from the ip addresses received
        Returns:
            new_ips(list): A collection of type IP
        """
        new_ips = []
        for ip_addr in self.ips:
            new_ips.append(IP(ip_addr))

        return new_ips


class PortFactory(PacketComponentFactory):
    """ A factory class that is used to generate a collection of type Port
    """

    def __init__(self, ports):
        """
        Args:
            ports(list): A list of port strings inputted by the user.
        """
        self.ports = ports

    def generate(self):
        """ Generates a collection of type Port from the ip addresses received
        Returns:
            new_ports(list): A collection of type Port
        """
        new_ports = []
        for port in self.ports:
            new_ports.append(Port(port))

        return new_ports
