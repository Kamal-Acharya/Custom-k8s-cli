from kubernetes import client,config
from kubernetes.client.exceptions import ApiException

config.load_kube_config()


def check_namespace_exist(name):
    api_instance = client.CoreV1Api()
    namespaces = api_instance.list_namespace()
    namespace_names = [ns.metadata.name for ns in namespaces.items]
    if name in namespace_names:
        return True
    else:
        return False
def list_namespace_all():
    api_instance = client.CoreV1Api()
    namespaces = api_instance.list_namespace()
    for n in namespaces.items:
        print(n.metadata.name)
def create_namespace(name):
    api_instance = client.CoreV1Api()
    if check_namespace_exist(name):
        print("Namespace already exist")
    else:
        try:
            body = client.V1Namespace(
                metadata=client.V1ObjectMeta(name=name)
            )
            api_instance.create_namespace(body=body)
            print(f"Namespace '{name}' created successfully")
        except ApiException as e:
            print(f"Failed to create namespace: {e}")
def delete_namespace(name):
    api_instance = client.CoreV1Api()
    try:
        api_instance.delete_namespace(name)
    except ApiException as e:
        print(f"Failed to create namespace: {e}")


