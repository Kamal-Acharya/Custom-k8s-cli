# K8s Python CLI

A lightweight, interactive **Kubernetes CLI built using Python** and the standard `cmd` module.  
This tool interacts **directly with the Kubernetes API (no kubectl dependency)** and is designed for **learning, automation, and day-to-day DevOps operations**.

---

## ✨ Features

- Interactive shell (`K8s>>` prompt)
- Namespace management
  - List namespaces
  - Create namespace
  - Delete namespace
- Pod operations
  - List pods in a namespace
  - List pods using label selectors
- Deployment operations
  - List deployments
  - List deployments using labels
  - Scale deployments
- Cluster operations
  - View cluster information
  - List kubeconfig contexts
  - Show current context
- Manifest validation
  - Server-side validation using Kubernetes API (`dry-run=server`)

---

## 📦 Project Structure

```text
.
├── main.py
├── functions/
│   ├── core/
│   │   └── core_cluster.py
│   ├── namespace/
│   │   └── namespace.py
│   ├── pods/
│   │   └── pod.py
│   ├── deployments/
│   │   └── deployment.py
│   └── custom/
│       └── custom.py


---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* Kubernetes cluster access
* Valid `~/.kube/config`
* Python Kubernetes client

```bash
pip install kubernetes

```

---

### Run the CLI

```bash
python main.py
```

You should see:

```text
Welcome to K8s Cli
K8s>>
```

---

## 📘 Available Commands

### Namespace Commands

| Command                   | Description            |
| ------------------------- | ---------------------- |
| `list_namespace`          | List all namespaces    |
| `create_namespace <name>` | Create a new namespace |
| `delete_namespace <name>` | Delete a namespace     |

---

### Pod Commands
| Command                                | Description                    |
| -------------------------------------- | ------------------------------ |
| `list_pod`                             | List pods in default namespace |
| `list_pod -n <namespace>`              | List pods in a namespace       |
| `list_pod -n <namespace> -l key=value` | List pods using labels         |


**Example:**

```text
K8s>> list_pod default app=nginx
```
---
### Deployment Commands

| Command                                    | Description                     |
| ------------------------------------------ | ------------------------------- |
| `list_deployment`                          | List deployments                |
| `list_deployment -n <namespace>`           | List deployments in a namespace |
| `list_deployment -l key=value`             | List deployments using labels   |
| `scale_deployment -a <name> -r <replicas>` | Scale a deployment              |


---

### Cluster Commands

| Command                  | Description                  |
| ------------------------ | ---------------------------- |
| `cluster_info`           | Show cluster information     |
| `list_context`           | List all kubeconfig contexts |
| `list_context --current` | Show current context         |

---

### Utility Commands

| Command | Description  |
| ------- | ------------ |
| `quit`  | Exit the CLI |

---

## 🆘 Help

Each command supports built-in help:

```text
K8s>> help
K8s>> help list_pod
```

---

## 🧠 Design Notes

* Built using Python's `cmd.Cmd`
* Uses Kubernetes Python client (no shelling out to `kubectl`)
* Easy to extend with new commands

---

## 🛠️ Future Enhancements

* Context switching support
* Resource describe & delete commands
* YAML apply support
* Autocompletion
* Configurable kubeconfig path
* Error handling & logging

---

## 🙌 Author

Built by **Kamal Acharya** — DevOps Engineer
