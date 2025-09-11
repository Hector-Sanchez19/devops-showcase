```mermaid
graph TD
  A[GitHub Repo] -->|Push| B[GitHub Actions CI/CD]
  B -->|Build & Push| C[Container Registry]
  C -->|Sync| D[ArgoCD]
  D -->|Deploy| E[Kubernetes Cluster]
  E -->|Metrics| F[Prometheus]
  F -->|Dashboards| G[Grafana]
