# K8s Python CLI

A lightweight, interactive **Kubernetes CLI built using Python** and the standard `cmd` module. This tool is designed for learning, automation, and quick operational tasks without relying directly on `kubectl` commands.

---

## ✨ Features

* Interactive shell (`K8s>>` prompt)
* Namespace management

  * List namespaces
  * Create namespace
  * Delete namespace
* Pod operations

  * List pods in a namespace
  * List pods using label selectors
* Cluster operations

  * View cluster information
  * List kubeconfig contexts
  * Show current context

---

## 📦 Project Structure

```text
.
├── main.py
├── functions/
│   ├── get_k8s_resource/
│   │   ├── list_pods.py
│   │   └── list_pod_by_labels.py
│   ├── core/
│   │   └── core_cluster.py
│   └── namespace/
│       └── namespace.py
```

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

| Command                                       | Description                  |
| --------------------------------------------- | ---------------------------- |
| `list_pod <namespace>`                        | List all pods in a namespace |
| `list_by_labels <namespace> <label-selector>` | List pods using labels       |

**Example:**

```text
K8s>> list_by_labels default app=nginx
```

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
K8s>> help list_by_labels
```

---

## 🧠 Design Notes

* Built using Python's `cmd.Cmd`
* Uses Kubernetes Python client (no shelling out to `kubectl`)
* Easy to extend with new commands
* Ideal as a **portfolio DevOps project** or **learning tool**

---

## 🛠️ Future Enhancements

* Context switching support
* Resource describe & delete commands
* YAML apply support
* Autocompletion
* Configurable kubeconfig path
* Error handling & logging

---

## 📄 License

MIT License

---

## 🙌 Author

Built by **Kamal Acharya** — DevOps Engineer

If you're using this as a project, feel free to extend it and showcase it in interviews 🚀
