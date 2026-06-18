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
Linux/MacOS:
    eval $(minikube docker-env)

Windows (Powershell):
    minikube docker-env --shell powershell | Invoke-Expression

Verify:
    docker images

Run above steps from any terminal that you will use


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
            minikube service greetings -n greetings1 --url
            URL1=<output from previous command>
            On Windows+Powershell
            $URL1=<output from previous command>

            minikube service greetings -n greetings2 --url
            URL2=<output from previous command>
            On Windows+Powershell
            $URL2=<output from previous command>

        Option 2:
            Terminal 1:
                kubectl port-forward -n greeting1 service/greetings 8080:80
            Terminal 2:
                URL1="http://localhost:8080"
            On Windows+Powershell, set the variable like this:
            $URL1 = "http://localhost:8080"

            Terminal 3:
                kubectl port-forward -n greeting2 service/greetings 8081:80
            Terminal 4:
                URL2="http://localhost:8081"
            On Windows+Powershell, set the variable like this:
            $URL2 = "http://localhost:8081"

    curl $URL1
    curl $URL1/greetings
    curl $URL1/listcontents
    curl $URL1/getk8sobjects

    curl $URL2
    curl $URL2/greetings
    curl $URL2/listcontents
    curl $URL2/getk8sobjects

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


