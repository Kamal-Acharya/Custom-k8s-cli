from kubernetes import client, config
from kubernetes.client import ApiException

config.load_kube_config()


def list_deployments(namespace):
    api_instance = client.AppsV1Api()
    try:
        deployments=api_instance.list_namespaced_deployment(namespace)
        for deployment in deployments.items:
            print(deployment.metadata.name)
    except ApiException as e:
        print(e)

def list_deployment_by_labels(namespace,labels):
    api_instance = client.AppsV1Api()
    deployments=api_instance.list_namespaced_deployment(namespace)
    for deployment in deployments.items:
        deploy_labels = deployment.metadata.labels
        deploy_label_list = [f"{k}={v}" for k, v in deploy_labels.items()]
        if all(label in deploy_label_list for label in labels):
            print(deployment.metadata.name)

def scale_deployment(namespace,deployment_name,replicas):
    api_instance = client.AppsV1Api()
    try:
        scale_client= client.V1ScaleSpec(replicas=replicas)

        body = {
            "spec": {
                "replicas":  scale_client.replicas
            }
        }
        api_instance.patch_namespaced_deployment_scale(namespace=namespace,name=deployment_name,body=body)
        print("Deployment scaled to",replicas)
    except ApiException as e:
        print(e)
    except Exception as e:
        print(e)

def restart_deployment(namespace,deployment_name,labels):
    print("Restarting deployment")