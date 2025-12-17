from kubernetes import client, config
import os


config.load_kube_config()

v1 = config

methods = [m for m in dir(v1) if not m.startswith("_")]
for m in methods:
    with open(file="config.txt",mode="a") as f:
        f.write(f"{m}\n")

