import xmlrpc.client

def remote3():
    with xmlrpc.client.ServerProxy('http://192.168.100.189:8000/') as proxy:
        network_data = proxy.get_network()
        print(network_data)
        with open("data3.json", "w") as json_file:
            json_file.write(network_data)
