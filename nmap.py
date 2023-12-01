import socket
import sys
from defined_ports import *
from port_object import *


def check_ports_for_least_popular_ports(target_host, port_list):
    for port in port_list:
        host_socket_checker_online = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_socket_checker_online.settimeout(2)  # timeout for the connection attempt
        try:
            # Attempt to connect to the host on the current port
            host_socket_checker_online.connect((target_host, port))
            return True  # return to main if connection is successful
        except (socket.timeout, socket.error):
            # Connection failed on the current port, try the next one
            pass
        finally:
            host_socket_checker_online.close()
    return False  # No successful connection on any port, host is offline


def check_ports_for_two_first_level_ports(target_host, port_lists):
    for port_list in port_lists:
        if port_list == 2:
            check_ports_for_least_popular_ports(target_host, port_list)
        for port_object_entity in port_list.prioritized_port_list:
            port = port_object_entity.prot_number
            host_socket_checker_online = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host_socket_checker_online.settimeout(2)  # timeout for the  connection attempt
            try:
                # Attempt to connect to the host on the current port
                host_socket_checker_online.connect((target_host, port))
                return True  # return to main if connection is successful
            except (socket.timeout, socket.error):
                # Connection failed on the current port, try the next one
                pass
            finally:
                host_socket_checker_online.close()

    return False  # No successful connection on any port, host is offline


def singing_ports_list():
    high_priority_ports = WellKnownPorts([
        Port_object_entity(80),
        Port_object_entity(443),
        Port_object_entity(22),
        Port_object_entity(21),
        Port_object_entity(25),
        Port_object_entity(3389),
        Port_object_entity(1433),
        Port_object_entity(8080),
        Port_object_entity(8443),
    ])

    medium_priority_ports = WellKnownPorts([
        Port_object_entity(53),
        Port_object_entity(110),
        Port_object_entity(143),
        Port_object_entity(3306),
        Port_object_entity(5900),
        Port_object_entity(8000),
        Port_object_entity(8888),
        Port_object_entity(9090),

    ])

    low_priority_ports = range(1024, 49151)

    return high_priority_ports, medium_priority_ports, low_priority_ports


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nmap.py <host>")
        sys.exit(1)

    host = sys.argv[1]


    # Define lists of well-known ports, arranged by their priorities
    port_tuple = singing_ports_list()

    if  check_ports_for_two_first_level_ports(host, port_tuple):
        print(f"{host} is online")
    else:
        print(f"{host} is offline")
