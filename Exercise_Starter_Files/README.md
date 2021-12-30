# Process to execute
Install kubernetes
        curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.19.5+k3s1 K3S_KUBECONFIG_MODE="644" sh -

vagrant upload sampleapp/k8s

1. Install Helm
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh

2. Install Graphana-Prometheus
kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --kubeconfig /etc/rancher/k3s/k3s.yaml

kubectl get pod -n monitoring | grep grafana
kubectl port-forward -n monitoring prometheus-grafana-6cd544d85d-sfglr --address 0.0.0.0 3000:3000
admin
prom-operator

3. Install Jeager
kubectl create namespace observability
kubectl create  -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.29.0/deploy/crds/jaegertracing.io_jaegers_crd.yaml
kubectl create  -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.29.0/deploy/service_account.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.29.0/deploy/role.yaml
kubectl create  -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.29.0/deploy/role_binding.yaml
kubectl create  -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.29.0/deploy/operator.yaml
# Give cluster-wide permissions to the Jaeger operator
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.29.0/deploy/cluster_role.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/v1.29.0/deploy/cluster_role_binding.yaml



4. Apply 
    jaeger-app-2.yaml
        deployment.apps/second-sample-app
    jaeger-app-1.yaml
        deployment.apps/my-sample-app
    jaeger-instance
        jaeger.jaegertracing.io/simplest

kubectl port-forward service/simplest-query 16686:16686

simplest-query.default.svc.cluster.local:16686