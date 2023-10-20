from condition_rule import extract_rule
from module_ana import extract_module
from filepath import file_path
from cpu import pod_cpu_per, pod_cpu_usage
from memori import pod_memori_per, pod_memori_usage
from alive import alive_status
from web import web_status
from alert_module import alert_mo
import time
from remote import remote
from remote2 import remote2
from remote3 import remote3
import re

file = file_path()
result = {}

def module_oversight():
    Extract_rule = extract_rule(file)
    for i in Extract_rule:
        if i in "alive":
            comparison = Extract_rule["alive"]["comparison"]
            if "alive.status" in comparison:
                alive_met = extract_module(file)
                alive_met2 = alive_met["alive"]["ip"]
                alive_result = alive_status(alive_met2)
                result["alive"] = alive_result
            elif comparison in "alive.time":
                alive_met = extract_module(file)
                alive_met2 = alive_met["alive"]["ip"]
        if i in "web":
            comparison = Extract_rule["web"]["comparison"]
            if "web.status" in comparison:
                web_met = extract_module(file)
                web_met2 = web_met["web"]["url"]
                web_result = web_status(web_met2)
                result["web"] = web_result
            elif "web.time" in comparison:
                web_met = extract_module(file)
                web_met2 = web_met["web"]["url"]
                web_result = web_status(web_met2)
                result["web"] = web_result
        if i in "cpu_pod":
            comparison = Extract_rule["cpu_pod"]["comparison"]
            if "cpu_pod.percent" in comparison:
                pattern = r'\b(\d+)\b'
                match = re.search(pattern, comparison)
                number = int(match.group())
                result_pod_cpu_per = pod_cpu_per(number)
                result["cpu_pod"] = result_pod_cpu_per
            elif "cpu_pod.usage" in comparison:
                pattern = r'\b(\d+)\b'
                match = re.search(pattern, comparison)
                number = int(match.group())
                result_cpu_use = pod_cpu_usage(number)
                result["cpu_pod"] = result_cpu_use
        if i in "memori_pod":
            comparison = Extract_rule["memori_pod"]["comparison"]
            if "memori_pod.percent" in comparison:
                pattern = r'\b(\d+)\b'
                match = re.search(pattern, comparison)
                number = int(match.group())
                result_memori_per = pod_memori_per(number)
                result["memori_pod"] = result_memori_per
            elif "memori_pod.usage" in comparison:
                pattern = r'\b(\d+)\b'
                match = re.search(pattern, comparison)
                number = int(match.group())
                result_memori_use = pod_memori_usage(number)
                result["memori_pod"] = result_memori_use
    return result

module = extract_module(file)
module_status = module_oversight()
print("module_status: ", module_status)

while True:
    remote()
    remote2()
    remote3()
    module_status = module_oversight()
    cpu_pod = module_status["cpu_pod"]
    memori_pod = module_status["memori_pod"]
    alive = module_status["alive"]
    web = module_status["web"]

    print(module_status)
    if cpu_pod == False:
        alert_mo(module["alert"]["url"], "cpu")
    if memori_pod == False:
        alert_mo(module["alert"]["url"], "memori")
    elif web == False:
        alert_mo(module["alert"]["url"], "web")
    elif cpu_pod and memori_pod == False:
        alert_mo(module["alert"]["url"], "cpu or memori")
        print("test4")
    elif alive == False:
        alert_mo(module["alert"]["url"], "alive")
    elif cpu_pod and memori_pod and alive == False:
        alert_mo(module["alert"]["url"], "cpu or memori or alive")
    print("test")
    time.sleep(5)

