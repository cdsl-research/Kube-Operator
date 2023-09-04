import subprocess #subprocessをインポート
import time
def alive_status(ip):#pingを送る関数
    
    
    res = subprocess.run(["ping",str(ip),"-c","1", "-W","300"],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
    print(res.stdout.decode("cp932"))
    if res.returncode == 0:
        ans = True
    else:
        ans = False
    print("----------")
    return ans

def alive_time(ip):#pingを送る関数
    start_time = time.time()
    
    res = subprocess.run(["ping",str(ip),"-c","1", "-W","300"],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
    print(res.stdout.decode("cp932"))
    if res.returncode == 0:
        ans = True
    else:
        ans = False
    print("----------")
    end_time = time.time()
    total =end_time -start_time
    return ans
