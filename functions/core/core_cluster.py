from kubernetes import client, config

config.load_kube_config()
def list_contexts(flag):
    all_context=[]
    curr_context={}
    contexts=config.list_kube_config_contexts()
    # Context return list and object
    for context in contexts:
        if isinstance(context, list):
            all_context=context
        if isinstance(context, dict):
            curr_context=context
    if flag:
        print(curr_context["name"])
        return
    for con in all_context:
        print(con["name"],"\n")

    
def cluster_info():
    print("Cluster info")
    info=client.VersionApi()
    print(info.get_code())

