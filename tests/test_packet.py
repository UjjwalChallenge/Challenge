import pytest
from firewall import packet

def test_integrity():
    packet_data = {
        "direction": "outbound",
        "protocol": "tcp",
        "port": 20000,
        "ip": "192.168.10.11"
    }

    new_packet = packet.Packet(packet_data)

    assert new_packet.direction.val == packet_data["direction"]
    assert new_packet.protocol.val == packet_data["protocol"]
    assert new_packet.port.val == packet_data["port"]
    assert new_packet.ip.val == packet_data["ip"]

