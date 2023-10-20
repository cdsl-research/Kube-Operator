import xmlrpc.client
from module_ana import extract_module  # 引数代入部
from filepath import file_path  # ファイルのパス
import json

file = file_path()


def remote():
    with xmlrpc.client.ServerProxy('http://192.168.100.204:30652/') as proxy:
        module = extract_module(file)
        cpu_pods = module["cpu_pod"]
        print(cpu_pods)
        namespace_cpu = cpu_pods["namespace"]
        file2 = "data.json"
        print("tetetetete")
        parsed_data = json.dumps(json.loads(proxy.get_pod_metrics_and_info(namespace_cpu)), indent=2)
        with open(file2, "w") as json_file:
            json_file.write(parsed_data)


remote()

