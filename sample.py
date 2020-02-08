from firewall.firewall import Firewall

fw = Firewall('data.csv')
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
print(fw.accept_packet("outbound", "tcp", 20000, "192.168.10.11"))
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
