from flask import Flask, request
import os
import json

from kubernetes import client, config

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/greetings")
def greetings():
    greeting = os.getenv("GREETING")
    return greeting


@app.route("/listcontents")
def listcontents():
    fp = open("/hostfolder/filenames.txt","r")
    lines = fp.readlines()
    return lines


@app.route("/getk8sobjects")
def get_cluster_details():
    config.load_incluster_config()

    namespace = "default"
    
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)

    output = {}

    pod_names = []
    for pod in pods.items:
        pod_names.append(pod.metadata.name)
    output["pods"] = pod_names

    cfg_map_names = []
    configmaps = v1.list_namespaced_config_map(namespace)
    for configmap in configmaps.items:
        cfg_map_names.append(configmap.metadata.name)
    output["configmaps"] = cfg_map_names

    sa_names = []
    serviceaccounts = v1.list_namespaced_service_account(namespace)
    for serviceaccount in serviceaccounts.items:
        sa_names.append(serviceaccount.metadata.name)
    output["serviceaccounts"] = sa_names

    obj_to_return = json.dumps(output)
    return obj_to_return


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
