import json
def pod_memori_usage(usage):
    with open("myapp/data.json", "r", encoding="UTF-8") as file:
        file_con = file.read()
        data_dict = json.loads(file_con)  # JSON文字列を辞書に変換
        pod_metrics_value = data_dict.get("pod_metrics", [])
        if not pod_metrics_value:
            print("pod_metrics not found in the file.")
            return False
        memori_values = [int(metric[2].replace('Mi', '')) for metric in pod_metrics_value] # memori_valuesを定義
        print(memori_values)
        for i in memori_values:
            if i >= usage:
                return False
        return True

def pod_memori_per(percent):
    with open("myapp/data.json", "r", encoding="UTF-8") as file:
        file_con = file.read()
        data_dict = json.loads(file_con)  # JSON文字列を辞書に変換
        pod_metrics_value = data_dict.get("pod_metrics", [])
        if not pod_metrics_value:
            print("pod_metrics not found in the file.")
            return False
        
        for i in pod_metrics_value:
            print(i)
            memori_usage_percent = (int(i[2]) / 800000) * 100  # ここで計算
            print(memori_usage_percent)
            if memori_usage_percent > percent:
                return False

        return True
    
    

    
    

