#!/bin/bash
echo "**** Begin installing k3s"

#Install
curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.19.5+k3s1 K3S_KUBECONFIG_MODE="644" sh -
echo "**** End installing k3s"

#kubectl proxy --address='0.0.0.0' /dev/null &

# echo "***Installing helm"
# curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
# chmod 700 get_helm.sh
# ./get_helm.sh
