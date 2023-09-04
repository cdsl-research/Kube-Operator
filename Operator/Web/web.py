import requests
import time
def web_status(url):
    status = requests.get(url)
    if status.status_code >= 400:
        return False
    else:
        return True

def web_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time() 
    response_time = end_time - start_time
    return response_time
