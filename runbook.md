# Runbook – DevOps Showcase

## Descripción del proyecto
Este proyecto es un showcase de DevOps que integra:

- Una aplicación Flask (`myapp`) con métricas Prometheus.
- Despliegue mediante **Helm**.
- Monitoreo con **Prometheus** y **Grafana**.
- Gestión de despliegues con **ArgoCD**.
- Dashboards listos en [`docs/dashboards/`](docs/dashboards/).

---

## 1. Requisitos previos

- Minikube o cluster Kubernetes disponible.
- Helm 3 instalado.
- Kubectl configurado para el cluster.
- Docker instalado (para construir imágenes locales).
- Acceso a Grafana y Prometheus (port-forward o NodePort).

---

## 2. Levantar el cluster

```bash
# Iniciar Minikube (con recursos recomendados)
minikube start --memory=4096 --cpus=2

# Crear namespaces
kubectl create namespace dev
kubectl create namespace monitoring
kubectl create namespace argocd
