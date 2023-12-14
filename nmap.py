import sys
import os
from defined_ports import *
from port_object import *
from host_utility import *
from local_client import *


def singing_ports_list():
    high_priority_ports = Well_Known_Ports([
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

    medium_priority_ports = Well_Known_Ports([
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


def port_Scanner(host, initial_port, final_port):
    # Define lists of well-known ports, arranged by their priorities
    port_tuple = singing_ports_list()
    Host_Scanner = Scanner(host, port_tuple, initial_port, final_port)
    if Host_Scanner.check_ports_for_two_first_level_ports():
        print(f"{host} is online")
    else:
        print(f"{host} is offline")

    available_ports_for_target_host = Host_Scanner.scan_range_of_input_ports()
    if len(available_ports_for_target_host) != 0:

        for port in available_ports_for_target_host:
            print(f"open port detected: {host}    --port:{port}     -- service: {Scanner.get_service_port(port)}")

    else:
        print("There is no open port detected in range you provide")

    return


def GET_POST_METHOD():

    while True:
        os.system("cls")
        print("Enter 'GET user_id' or 'POST user_name user_age' to simulate a request: ")
        print ("0.Exit")
        request = input()
        if "GET" in request or "POST" in request:
            client_request = Client_connection()
            client_request.intilize_connection_to_server(request)
            input("Enter to continue")
        elif request == '0':
            break
        else:
            print ("Bad request. Enter to try again")
            input()



    return




def initialize_program(scan_flag = False):

    if scan_flag:
        while True:
            os.system("cls")
            print("please enter the the IP **NOTE DO NOT USE PYTHON AT FIRST**")
            received_input = input()
            received_input_split = received_input.split()
            host = received_input_split[0]
            initial_port = int(received_input_split[1])
            final_port = int(received_input_split[2])
            port_Scanner(host, initial_port, final_port)
            user_choice = input("To Scan again press 0 otherwise 1 :")
            if user_choice == '0':
                pass
            else:
                break
    else:
        GET_POST_METHOD()

    input("Press enter to continue")
    os.system("cls")
    return


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Usage: python nmap.py <host>")
        sys.exit(1)

    host = sys.argv[1]
    initial_port = int(sys.argv[2])  # it is string , converting to integer
    final_port = int(sys.argv[3])
    port_Scanner(host, initial_port, final_port)
    while True:
        print ("If you want to scan another IP address Enter 0 otherwise press 1 to proceed with HTTP commands simulation:")
        print("0.Scan IP")
        print("1.HTTP Commands Simulation")
        print("2.Exit")
        try :
            command = input()
            if command == '0':
                initialize_program(True)
            elif command == '1':
                initialize_program(False)
            elif command == '2':
                print("Exiting the program  ...")
                break
            else:
                raise ValueError("Key wrong pressed")
        except ValueError as error :
            os.system("cls")
            print(f"The Error is {error}")
            print("Please enter a valid choice")