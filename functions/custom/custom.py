from kubernetes import client, config,dynamic
import yaml,json
from kubernetes.client import ApiException
from kubernetes.dynamic import DynamicClient

config.load_kube_config()


def validate_manifest(file):
    print("Validating manifest...")
    dyn_client=dynamic.DynamicClient(
        client.ApiClient()
    )
    try:
        with open(file) as f:
            manifest = yaml.safe_load(f)
            required = ["apiVersion", "kind", "metadata"]
            missing = [k for k in required if k not in manifest]
            if missing:
                print("Manifest missing required fields: %s" % missing)
            else:

                resource = dyn_client.resources.get(
                    api_version=manifest["apiVersion"],
                    kind=manifest["kind"]
                )

                namespace = manifest.get("metadata", {}).get("namespace")

                # Server-side dry run (actual API validation)
                if resource.namespaced:
                    resource.create(
                        body=manifest,
                        namespace=namespace or "default",
                        dry_run="All"
                    )
                else:
                    resource.create(
                        body=manifest,
                        dry_run="All"
                    )
                print("Manifest validated")
                # kind = manifest["kind"]

                # if kind == "Deployment":
                #     apps_v1 = client.AppsV1Api()
                #     apps_v1.create_namespaced_deployment(
                #         namespace=manifest["metadata"]["namespace"],
                #         body=manifest,
                #         dry_run="All"  # 🔥 THIS is validation
                #     )
                # if kind == "Pod":
                #     v1=client.CoreV1Api()
                #     v1.create_namespaced_pod(
                #         namespace="default",
                #         body=manifest,
                #         dry_run="All"
                #     )
    except ApiException as e:
        error = json.loads(e.body)
        print(error["message"])
    except Exception as e:
        print(e)


def drift_detection():
    print("Drift detection...")

def resource_usage(namespace):
    print("Resource usage...")
