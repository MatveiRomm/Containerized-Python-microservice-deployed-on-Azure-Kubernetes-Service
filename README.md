# Test-task

Welcome to Containerized Python microservice deployed on Azure Kubernetes Service.

The main purpose of this microservice is to display actual value of 1 BitCoin in EUR and CZK, server time and client request time via API in JSON format. As a result, we can make a GET request (curl) with a specific password in a header, which we have placed in the ENV variable. 

# Prerequisites:
1. "Docker" to create an image from Dockerfile and be able to run it.
2. "Kubectl" to manage our k8s cluster in the future.
3. "Azure account" (with container registry and kubernetes service) where we will push the docker image and deploy the k8s cluster. 

# Creating a docker image
After installing Docker, you can build a docker image from a Dockerfile.

docker build -t <name/ver> .

# Managing your Azure account

To create your own Azure account and basic k8s cluster, we can use the official documentation.

https://docs.microsoft.com/en-us/cli/azure/install-azure-cli - Installing the Azure CLI.

https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-acr?tabs=azure-cli - Creating a resource group, container registry, and pushing our docker image.

https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster?tabs=azure-cli - Creating a K8S cluster and connecting Kubectl to it. 

Optionally, we can use Azure Key Vault to secretly store passwords. This application will use the less secure option based on creating a configMap pod or secret pod for demonstration purposes.

# Deployment and running aplication. 

The application uses either config.yaml or secret.yaml to store our ENV password. Depending on which you chose, edit webapp.yaml (lines 22, 23) and then deploy one of the YAML files. 

The last part of the deployment is to change the image name (on line 18) in webapp.yaml depending on what you named it in the container registry.  After changing the image name, you can run the YAML file to create the deployment and the k8s service.

kubectl apply -f webapp.yaml

After about a minute you should be able to get an external IP using the command:

kubectl get service 

Find LoadBalancer and its external IP, through which we can get the actual JSON response (for example using curl). 

The application uses a simple x-Api-Key to handle the password. Use it as a header with a password to get a response.

curl -H "x-api-key: <password>" <external IP> 
