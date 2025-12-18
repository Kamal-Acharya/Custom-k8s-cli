from kubernetes import client, config
from datetime import datetime, timezone

config.load_kube_config()

def format_timedelta(delta):
    seconds = int(delta.total_seconds())

    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds // 60}m"
    elif seconds < 86400:
        return f"{seconds // 3600}h"
    else:
        return f"{seconds // 86400}d"
def get_pod_age(pod):
    created = pod.metadata.creation_timestamp
    now = datetime.now(timezone.utc)
    delta = now - created

    return format_timedelta(delta)
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
    print("Listing pods with their labels:")
    v1 = client.CoreV1Api()
    print(labels)
    pods = v1.list_namespaced_pod(namespace=namespace)
    for pod in pods.items:
        pod_labels = pod.metadata.labels or {}

        # Convert dict → ["key=value", ...]
        pod_label_list = [f"{k}={v}" for k, v in pod_labels.items()]

        # Check if all requested labels exist in pod labels
        if all(label in pod_label_list for label in labels):
            age=get_pod_age(pod)
            print(pod.metadata.name,age)