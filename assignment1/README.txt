Steps
-----

Build container:
-----------------
./build.sh


Run container:
---------------
container1=$(./run.sh)

When you modify the application to use port 5001,
change the port in the commands below.

curl http://localhost:5000/
curl http://localhost:5000/greetings
curl http://localhost:5000/listcontents


See container logs:
--------------------
docker logs $container1


Stop container:
---------------
docker stop $container1
