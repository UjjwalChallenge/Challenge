import pytest

from firewall.firewall import Firewall

fw = Firewall('./tests/test_data.csv')


def test_rule_1():
    # inbound,tcp,80,192.168.1.2-192.168.1.5

    valid_L, _ = fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")
    assert valid_L == True

    valid_H, _ = fw.accept_packet("inbound", "tcp", 80, "192.168.1.5")
    assert valid_H == True

    valid_N, _ = fw.accept_packet("inbound", "tcp", 80, "192.168.1.3")
    assert valid_N == True

    invalid_ip_L, err = fw.accept_packet("inbound", "tcp", 80, "192.168.1.1")
    assert invalid_ip_L == False and err == "IP not accepted"

    invalid_ip_H, err = fw.accept_packet("inbound", "tcp", 80, "192.168.1.6")
    assert invalid_ip_H == False and err == "IP not accepted"

    invalid_port, err = fw.accept_packet("outbound", "tcp", 9, "192.168.1.5")
    assert invalid_port == False and err == "Port not accepted"


def test_rule_2():
    # outbound,tcp,10000-20000,192.168.10.11

    valid_L, _ = fw.accept_packet("outbound", "tcp", 10000, "192.168.10.11")
    assert valid_L == True

    valid_H, _ = fw.accept_packet("outbound", "tcp", 20000, "192.168.10.11")
    assert valid_H == True

    valid_N, _ = fw.accept_packet("outbound", "tcp", 10500, "192.168.10.11")
    assert valid_N == True

    invalid_ip, err = fw.accept_packet("outbound", "tcp", 10500, "192.168.10.12")
    assert invalid_ip == False and err == "IP not accepted"

    invalid_port_H, err = fw.accept_packet("outbound", "tcp", 20500, "192.168.10.11")
    assert invalid_port_H == False and err == "Port not accepted"

    invalid_port_L, err = fw.accept_packet("outbound", "tcp", 500, "192.168.10.11")
    assert invalid_port_L == False and err == "Port not accepted"


def test_rule_3():
    # inbound,udp,53,192.168.1.1-192.168.2.5

    valid_L, _ = fw.accept_packet("inbound", "udp", 53, "192.168.1.1")
    assert valid_L == True

    valid_N, _ = fw.accept_packet("inbound", "udp", 53, "192.168.1.100")
    assert valid_N == True

    valid_H, _ = fw.accept_packet("inbound", "udp", 53, "192.168.2.5")
    assert valid_H == True

    invalid_port_L, err = fw.accept_packet("inbound", "udp", 1, "192.168.1.1")
    assert invalid_port_L == False and err == "Port not accepted"

    invalid_port_H, err = fw.accept_packet("inbound", "udp", 60, "192.168.1.1")
    assert invalid_port_H == False and err == "Port not accepted"

    invalid_ip_L, err = fw.accept_packet("inbound", "udp", 53, "192.168.1.0")
    assert invalid_ip_L == False and err == "IP not accepted"

    invalid_ip_H, err = fw.accept_packet("inbound", "udp", 53, "192.168.2.6")
    assert invalid_ip_H == False and err == "IP not accepted"


def test_rule_4():
    # outbound,udp,1000-2000,52.12.48.92

    valid_port_L, _ = fw.accept_packet("outbound", "udp", 1000, "52.12.48.92")
    assert valid_port_L == True

    valid_port_N, _ = fw.accept_packet("outbound", "udp", 1500, "52.12.48.92")
    assert valid_port_N == True

    valid_port_H, _ = fw.accept_packet("outbound", "udp", 2000, "52.12.48.92")
    assert valid_port_H == True

    invalid_port_L, err = fw.accept_packet("outbound", "udp", 500, "52.12.48.92")
    assert invalid_port_L == False and err == "Port not accepted"

    invalid_port_H, err = fw.accept_packet("outbound", "udp", 2500, "52.12.48.92")
    assert invalid_port_H == False and err == "Port not accepted"

    invalid_ip_L, err = fw.accept_packet("outbound", "udp", 1500, "52.12.48.90")
    assert invalid_port_L == False and err == "IP not accepted"

    invalid_ip_H, err = fw.accept_packet("outbound", "udp", 1500, "52.12.48.94")
    assert invalid_port_H == False and err == "IP not accepted"
