import argparse
import shlex
import cmd

from functions.core.core_cluster import list_contexts, cluster_info
from functions.namespace.namespace import (
    list_namespace_all,
    create_namespace,
    delete_namespace
)
from functions.pods.pod import list_pods, list_pod_by_labels
from functions.deployments.deployment import (
    list_deployments,
    list_deployment_by_labels,
    scale_deployment
)
from functions.custom.custom import validate_manifest


class MyCLI(cmd.Cmd):
    """
    Kubernetes CLI tool (kubectl-inspired)

    Type `help` to list commands
    Type `help <command>` for command usage
    """

    prompt = "K8s>> "
    intro = "Welcome to K8s CLI 🚀 (type `help` to get started)"

    # ------------------------------------------------------------------
    # Namespace Commands
    # ------------------------------------------------------------------

    def do_list_namespace(self, arg):
        """List all namespaces in the cluster

        Usage:
          list_namespace
        """
        list_namespace_all()

    def do_create_namespace(self, name):
        """Create a new namespace

        Usage:
          create_namespace <namespace-name>
        """
        if not name:
            print("❌ Namespace name is required")
            return
        create_namespace(name)

    def do_delete_namespace(self, name):
        """Delete a namespace

        Usage:
          delete_namespace <namespace-name>
        """
        if not name:
            print("❌ Namespace name is required")
            return
        delete_namespace(name)

    # ------------------------------------------------------------------
    # Cluster Commands
    # ------------------------------------------------------------------

    def do_cluster_info(self, arg):
        """Show cluster information

        Usage:
          cluster_info
        """
        cluster_info()

    def do_list_context(self, arg):
        """List kubeconfig contexts

        Usage:
          list_context
          list_context --current
        """
        list_contexts(1 if arg == "--current" else 0)

    # ------------------------------------------------------------------
    # Pod Commands
    # ------------------------------------------------------------------

    def do_list_pod(self, arg):
        """List pods in a namespace

        Usage:
          list_pod
          list_pod -n dev
          list_pod -n dev -l app=nginx,env=prod
        """
        parser = argparse.ArgumentParser(
            prog="list_pod",
            description="List Kubernetes pods"
        )
        parser.add_argument("-n", "--namespace", default="default")
        parser.add_argument("-l", "--labels", help="key=value,key=value")

        try:
            args = parser.parse_args(shlex.split(arg))
        except SystemExit:
            return

        if args.labels:
            list_pod_by_labels(args.namespace, args.labels.split(","))
        else:
            list_pods(args.namespace)

    # ------------------------------------------------------------------
    # Deployment Commands
    # ------------------------------------------------------------------

    def do_list_deployment(self, arg):
        """List deployments in a namespace

        Usage:
          list_deployment
          list_deployment -n dev
          list_deployment -n dev -l app=myapp
        """
        parser = argparse.ArgumentParser(
            prog="list_deployment",
            description="List Kubernetes deployments"
        )
        parser.add_argument("-n", "--namespace", default="default")
        parser.add_argument("-l", "--labels", help="key=value,key=value")

        try:
            args = parser.parse_args(shlex.split(arg))
        except SystemExit:
            return

        if args.labels:
            list_deployment_by_labels(args.namespace, args.labels.split(","))
        else:
            list_deployments(args.namespace)

    def do_scale_deployment(self, arg):
        """Scale a deployment

        Usage:
          scale_deployment -a my-app -r 3
          scale_deployment -a my-app -n dev -r 5
        """
        parser = argparse.ArgumentParser(
            prog="scale_deployment",
            description="Scale a Kubernetes deployment"
        )
        parser.add_argument("-a", "--name", required=True)
        parser.add_argument("-n", "--namespace", default="default")
        parser.add_argument("-r", "--replicas", required=True, type=int)

        try:
            args = parser.parse_args(shlex.split(arg))
        except SystemExit:
            return

        scale_deployment(args.namespace, args.name, args.replicas)

    # ------------------------------------------------------------------
    # Custom / Utility Commands
    # ------------------------------------------------------------------

    def do_validate(self, filename):
        """Validate a Kubernetes manifest (server-side dry-run)

        Usage:
          validate deployment.yaml
        """
        if not filename:
            print("❌ Filename is required")
            return
        validate_manifest(filename)

    # ------------------------------------------------------------------
    # Exit
    # ------------------------------------------------------------------

    def do_quit(self, arg):
        """Exit the CLI

        Usage:
          quit
        """
        print("Goodbye 👋")
        return True

    def do_exit(self, arg):
        """Exit the CLI"""
        return self.do_quit(arg)


if __name__ == "__main__":
    MyCLI().cmdloop()
