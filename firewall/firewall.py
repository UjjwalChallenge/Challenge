from firewall.packet import Packet, Direction, Protocol, IPFactory, PortFactory

from firewall.rules import RulesDataStore
import csv


class Firewall:

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.rds = RulesDataStore()
        self.read()

    def read(self):
        """
        Reads the specified .csv file, interprets every line as a rule and adds it to the
        RulesDataStore
        """
        with open(self.file_path) as f:
            f_reader = csv.reader(f, delimiter=',')
            for rule in f_reader:
                rule_data = {
                    "direction": Direction(rule[0]),
                    "protocol": Protocol(rule[1]),
                    "ports": PortFactory(rule[2].split('-')).generate(),
                    "ips": IPFactory(rule[3].split("-")).generate()
                }
                # forms a rule string from the rule read
                rule_str = "".join(rule)
                # adds the rule to the RulesDataStore
                self.rds.add_rule(rule_data, rule_str)

    def accept_packet(self, direction, protocol, port, ip_address):
        """Used to find whether a packet is acceptable or not, according to the rules
        present in the RulesDataStore

        Args:
            direction(string): Direction of the packet i.e. inbound or outbound
            protocol(string): Packet protocol - udp or tcp
            port(string): Packet port. Should be in range [1,65535]
            ip_address(string): IP address of the packet.

        Returns:
            True if packet is acceptable. False otherwise
        """

        # storing packet data received from the user as a dictionary
        packet_data = {
            "direction": direction,
            "protocol": protocol,
            "port": str(port),
            "ip": ip_address
        }

        # creates a new packet object from the packet_data
        new_packet = Packet(packet_data)

        # checks if new packet is valid or not
        if not new_packet.is_valid():
            return False, "Invalid Packet"

        # checks for the validity of packet in the RulesDataStore
        return self.rds.search(new_packet)
