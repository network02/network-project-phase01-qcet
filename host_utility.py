import socket


class Scanner:
    def __init__(self, host, list_of_scanner_port):
        self.host = host
        self.priority_port_list = list_of_scanner_port


    def check_ports_for_least_popular_ports(self, port_list):
        INT_MAX_ITER = 5 # for saying, it is offline , for simplicity
        for port in port_list:
            INT_MAX_ITER += 1
            host_socket_checker_online = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host_socket_checker_online.settimeout(2)  # timeout for the connection attempt
            try:
                # Attempt to connect to the host on the current port
                host_socket_checker_online.connect((self.host, port))
                return True  # return to main if connection is successful
            except (socket.timeout, socket.error):
                # Connection failed on the current port, try the next one
                pass
            finally:
                host_socket_checker_online.close()
            if 3 <= INT_MAX_ITER: # for saying, it is offline , for simplicity
                break


        return False  # No successful connection on any port, host is offline


    def check_ports_for_two_first_level_ports(self):
        for port_list in self.priority_port_list:
            for port_object_entity in port_list.prioritized_port_list:
                port = port_object_entity.prot_number
                host_socket_checker_online = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host_socket_checker_online.settimeout(2)  # timeout for the  connection attempt
                try:
                    # Attempt to connect to the host on the current port
                    host_socket_checker_online.connect((self.host, port))
                    return True  # return to main if connection is successful
                except (socket.timeout, socket.error):
                    # Connection failed on the current port, try the next one
                    pass
                finally:
                    host_socket_checker_online.close()

        low_priority_ports = range(1024, 49151)
        self.check_ports_for_least_popular_ports(low_priority_ports)
        return False  # No successful connection on any port, host is offline
