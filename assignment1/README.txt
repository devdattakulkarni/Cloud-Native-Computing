Steps
-----

Build container:
-----------------

# TODO : Requirement 5 
docker build -t <> .

Run container:
---------------

# TODO : Requirement 6
# Make the following changes in the docker run command:
# 1. Update the port
# 2. Volume mount the current folder on the host to the folder "/hostfolder"
# 3. Pass the GREETING env var with value "Spring was earlier."
# 4. Pass your image tag from the build section above
# 5. Map host port 5000 to container port 5001

docker run -p 5000:5001 -d --name assignment1 <>


Try the application:
----------------------

curl http://localhost:5000/
curl http://localhost:5000/greetings
curl http://localhost:5000/listcontents


See container logs:
--------------------
docker logs assignment1


Go inside the container:
------------------------
docker exec -it assignment1 /bin/bash


Stop container:
---------------
docker stop assignment1


Remove container:
-------------------
docker rm assignment1