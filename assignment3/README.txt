Setup
-----
Install Minikube
Install kubectl
Install Helm


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

# TODO : Requirement 1.1
docker build -t <> .


Install the greetings helm chart:
---------------------------------
helm install greetings1 -n greetings1 --create-namespace ./greetings-chart --set nodePort=32764 --set greeting="This is greetings1"
helm install greetings2 -n greetings2 --create-namespace ./greetings-chart --set nodePort=32765 --set greeting="This is greetings2"

Check helm releases:
--------------------
helm list

Try app endpoints:
------------------
    Linux:
        MINIKUBE_IP=$(minikube ip)
        URL1=http://$MINIKUBE_IP:32764
        URL2=http://$MINIKUBE_IP:32765

    MacOS/Windows:
        Use either option 1 or option 2.
        Option 2 is better as the URL will not change even when you re-deploy the application.
        Option 1:
            minikube service greetings --url
            URL=<output from previous command>
            On Windows+Powershell
            $URL=<output from previous command>
        Option 2:
            Terminal 1:
                kubectl port-forward service/greetings 8080:80
            Terminal 2:
                URL="http://localhost:8080"
        
            On Windows+Powershell, set the variable like this:
            $URL = "http://localhost:8080"

    curl $URL
    curl $URL/greetings
    curl $URL/listcontents
    curl $URL/getk8sobjects


Delete Helm releases:
----------------------
helm delete greetings1 -n greetings1
helm delete greetings2 -n greetings2


Use the plugins:
-----------------
export PATH=$PATH:`pwd`
kubectl greetings show greetings1
kubectl greetings show greetings2
kubectl greetings delete greetings1 greetings1
kubectl greetings delete greetings2 greetings2


