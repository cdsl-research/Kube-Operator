import json
import re
def pod_cpu_usage(usage):
    with open("myapp/data.json", "r", encoding="UTF-8") as file:
        file_con = file.read()
        data_dict = json.loads(file_con)  # JSON文字列を辞書に変換
        pod_metrics_value = data_dict.get("pod_metrics", [])
        if not pod_metrics_value:
            print("pod_metrics not found in the file.")
            return False
        print("pod_metrics_value: ", pod_metrics_value)
        cpu_values = [int(metric[1].replace('m', '')) for metric in pod_metrics_value] # memori_valuesを定義
        print(cpu_values)    
        for i in cpu_values:
            if i >= usage:
                return False
        
        return True


def pod_cpu_per(percent):
    with open("myapp/data.json", "r", encoding="UTF-8") as file:
        file_con = file.read()
        data_dict = json.loads(file_con)  # JSON文字列を辞書に変換
        pod_metrics_value = data_dict.get("pod_metrics", [])
        if not pod_metrics_value:
            return False
        
        for i in pod_metrics_value:
            i = list(map(lambda n: re.sub('[0-9]+m', n[:-1], n), i))
            #i.replace('m', '')
            print("i: ",i)
            cpu_usage_percent = (int(i[1]) / 3000) * 100  # ここで計算
            if cpu_usage_percent > percent:
                print(cpu_usage_percent)
                return False

        return True

