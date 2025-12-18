import os,subprocess
import cmd
from functions.core.core_cluster import list_contexts,cluster_info
from functions.namespace.namespace import list_namespace_all,create_namespace,delete_namespace
from functions.pods.pod import list_pods,list_pod_by_labels
print("Creating a CLI using python")


class MyCLI(cmd.Cmd):
    prompt= 'K8s>>'
    intro = 'Welcome to K8s Cli'
    # Namespace Commands
    def do_list_namespace(self,arg):
        list_namespace_all()
    def do_create_namespace(self,name):
        if not name:
            print("Please provide the namespace name")
        else:
            create_namespace(name)
    def do_delete_namespace(self,name):
        if not name:
            print("Please provide the namespace name")
        else:
            delete_namespace(name)

    # Core Commands
    def do_cluster_info(self,arg):
        cluster_info()
    def do_list_context(self,arg):
        if arg == "--current":
            list_contexts(1)
        else:
            list_contexts(0)
    def help_switch_context(self):
        print("Command to run: switch <contextName>")

    # Pods Commands
    def do_list_pod(self,arg):
        labels_list=[]
        if arg:
            args = arg.split(" ")
            namespace = args[0]
            if len(args) > 1:
                print("inside")
                labels = args[1].split(",")
                print(labels)
                list_pod_by_labels(namespace,labels)
            else:
                list_pods(namespace)
        else:
            namespace = "default"
            list_pods(namespace)
    
    # def help_list_by_labels(self):
    #     print("Command to run: list by labels <namespace> <labels>")
    #
    # def do_list_by_labels(self,arg):
    #     if not arg:
    #         print("Please provide the namespace and labels")
    #         return True
    #     namespace, labels = arg.split(maxsplit=1)
    #     list_pod_by_labels(namespace,labels)
    def do_quit(self, line):
        """Exit the CLI."""
        return True         
        

if __name__ == "__main__":
    cli=MyCLI()
    cli.cmdloop()        