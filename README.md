# Kube-Operator

これはKubernetes上で監視対象を監視するソフトウェアです
![image](https://user-images.githubusercontent.com/68419885/284459924-49526340-42f0-4ac6-9dfa-475721602fc3.png)
## 使い方

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

