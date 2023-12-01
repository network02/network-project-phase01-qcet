import sys
from defined_ports import *
from port_object import *
from host_utility import *



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
        Port_object_entity(1234),
        Port_object_entity(5678),
        Port_object_entity(9876),
        Port_object_entity(3333),
        Port_object_entity(9999),
    ])
    return high_priority_ports, medium_priority_ports





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nmap.py <host>")
        sys.exit(1)

    host = sys.argv[1]

    # Define lists of well-known ports, arranged by their priorities
    port_tuple = singing_ports_list()
    Host_Scanner = Scanner(host, port_tuple)
    if Host_Scanner.check_ports_for_two_first_level_ports():
        print(f"{host} is online")
    else:
        print(f"{host} is offline")
