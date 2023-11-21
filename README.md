# Kube-Operator

これはKubernetes上で監視対象を監視するソフトウェアです
![image](https://user-images.githubusercontent.com/68419885/284459924-49526340-42f0-4ac6-9dfa-475721602fc3.png)
## 使い方

この監視ソフトウェアは独自の設定ファイルを用います．以後.mtrファイルとします．
.mtrファイルのフォーマットは以下です．例えば以下の例ではwebというモジュールを使用して外形監視を行います．
```
module: #監視対象部
  web:
    url: http://example.com
  alert:
    url: http://slack.com
    runbookURL: http://runbook.com
    
module-rule: #監視条件部
  web:
    loop(3，3)
      web.status > 500:

condition: #配置方法部
  if web == True:
    alert("500 Error")
```

この設定ファイルが設定できたら以下のステップでKube-Operatorをデプロイします．

Step1
```
$ cd Kube-Operator/Operator/
```

Step2
```
kubectl apply -k . -n python
```

Step3
```
kubectl get pods -n python -w
```

