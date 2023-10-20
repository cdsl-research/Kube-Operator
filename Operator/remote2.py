import xmlrpc.client

def remote2():
    with xmlrpc.client.ServerProxy('http://192.168.100.189:6000/') as proxy:
        # サーバー上のget_disk()関数を呼び出し
        disk_data = proxy.get_disk()
        print(disk_data)
        file2 = "data2.json"
        with open(file2, "w") as json_file:
            json_file.write(disk_data)

remote2()

