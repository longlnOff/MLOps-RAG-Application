# MLOps-RAG-Application

## ON-PREMISE

### 1. Setup enviroment

#### 1.1 Setup kubectl, kubectx and kubens
a. Install kubectl <br>
[kubernetes installation guide linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)


b. Install kubectx and kubens <br>
[ctx and kubens installation guide](https://github.com/ahmetb/kubectx?tab=readme-ov-file#kubectl-plugins-macos-and-linux)

#### 1.2 Install and Setup mininkube
a. Install and start minikube cluster <br>
[guide install and start minikube cluster](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)

b. Enable ingress in minikube <br>
[guide enable and check ingress on minikube](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/#enable-the-ingress-controller)
#### 1.3 Setup helm chart

[helm chart guide](https://helm.sh/docs/intro/install/)

### 2. Deploy service manually

clone repo: git clone https://github.com/longlnOff/MLOps-RAG-Application.git <br>

#### 2.1 Deploy nginx-ingress
- remember delete existing Ingress Class in minikube: kubectl delete ingressclass nginx <br>
- cd HelmChart/nginx-ingress/
- kubectl create ns nginx-system
- helm upgrade --install ingress-nginx . -n nginx-system <br>
After that, nginx ingress controller will be created in `nginx-ingress` namespace.

#### 2.2 Deploy application
- cd HelmChart/app/
- kubectl create ns model-serving
- helm upgrade --install chat . -n model-serving <br>

After that, application deployed in local cluster. <br>
To access application docs api: <br>
- get minikube cluster: minikube ip
- access web: minikube-ip:30000 <br>

To access application through nginx:
- sudo vim /etc/hosts
- minikube-ip chat.example.local <br>
Now, you can access FASTAPI docs with: chat.example.local/docs

#### 2.3 Deploy mornitoring service
