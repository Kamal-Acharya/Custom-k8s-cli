from kubernetes import client, config

config.load_kube_config()


def list_pods(namespace):
    if not namespace:
        print("Provide the nameapce to list Pod")
        return
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    pods = v1.list_namespaced_pod(namespace=namespace)
    for i in pods.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def list_pod_by_labels(namespace, labels):
    if namespace or labels:
        exit
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace=namespace)
    for pod in pods.items:
        if labels in pod.metadata.labels:
            print(pod.metadata.name, pod.metadata.labels)