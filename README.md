## Cloud Native Architecture Nanodegree (CNAND): Observability

### kubectl port fowarding examples:
kubectl --namespace monitoring port-forward svc/prometheus-grafana --address 0.0.0.0 3000:80

kubectl port-forward $(kubectl get pods -l-app="my-sample-app" -o name) 8888:8888

-----------------------------------------
# Project Installation process
This is the guide for installation process on the project

## 1. Helm instalation
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

## 2. Helm installing prometheus
```
kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --kubeconfig /etc/rancher/k3s/k3s.yaml
```

## 3. Install Jeager
```
kubectl create namespace observability
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.28.0/deploy/crds/jaegertracing.io_jaegers_crd.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.28.0/deploy/service_account.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.28.0/deploy/role.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.28.0/deploy/role_binding.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.28.0/deploy/operator.yaml

```

## 4. Cluster wide Jeager
```
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.28.0/deploy/cluster_role.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.28.0/deploy/cluster_role_binding.yaml

```

## 5. Apply other YAML files
kubectl apply -f manifests/app
kubectl apply -f manifests/jaeger-tracing
kubectl create namespace 
kubectl apply -f manifests2/mongo
kubectl apply -f manifests2/app


```
kubectl get pod -n monitoring | grep grafana

> prometheus-grafana-5cddc775c4-w4b9g 
kubectl port-forward -n monitoring prometheus-grafana-5cddc775c4-bf8gc --address 0.0.0.0 3000:3000
#kubectl port-forward -n monitoring service/prometheus-grafana --address 0.0.0.0 3000:80 // This is a running example

kubectl get -n observability ingress

kubectl port-forward svc/frontend-service 8080:8080

kubectl get deployment jaeger-operator -n observability
```

# Prometheus querys
```
node_boot_time_seconds{container="node-exporter", endpoint="metrics", instance="10.0.2.15:9100", job="node-exporter", namespace="monitoring", pod="prometheus-prometheus-node-exporter-n5tdq", service="prometheus-prometheus-node-exporter"}
time() - node_boot_time_seconds{job="node-exporter", instance=~"10.0.2.15:9100"}
```

## upload manifets to vagrant
vagrant upload [file] [destination]
vagrant upload .\manifests 


## Creating Jaeger 
After verify the correct Jaeger creation of deployment
```
kubectl get deployment -n observability
kubectl get jaegers -n observability

kubectl get deployment,pods,svc  -n observability


kubectl port-forward -n observability  service/backend-query --address 0.0.0.0 16686:16686

-> Remember to have abailable the port on a vagrant config file
```
