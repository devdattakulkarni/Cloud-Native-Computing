Setup
-----
Install Minikube
Install kubectl


Start Minikube cluster
----------------------
minikube start


Connect docker CLI on Host to Docker Daemon inside Minikube
------------------------------------------------------------
eval $(minikube docker-env)
docker images

Do this step from any terminal that you will use


Build container:
-----------------

# TODO : Requirement 1
docker build -t <> .


Deploy application to Minikube:
-------------------------------
kubectl apply -f greetings.yaml



Try app endpoints:
------------------
MINIKUBE_IP=$(minikube ip)
curl http://$MINIKUBE_IP:32767/
curl http://$MINIKUBE_IP:32767/greetings
curl http://$MINIKUBE_IP:32767/listcontents
curl http://$MINIKUBE_IP:32767/getk8sobjects


See Kubernetes resources:
-------------------------
kubectl get pods,services,configmaps,serviceaccounts,roles,rolebindings -l app=greetings


See Pod logs:
-------------
kubectl get pods -l app=greetings
kubectl logs <pod-name-from-above-output> 


Delete application:
-------------------
kubectl delete -f greetings.yaml

