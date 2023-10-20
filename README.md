# Kube-Operator

これはKubernetes上で監視対象を監視するソフトウェアです

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

