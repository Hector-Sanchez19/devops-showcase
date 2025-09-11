# DevOps Showcase


Este proyecto es un **mini stack DevOps completo**, diseñado para mostrar habilidades en **Kubernetes, Helm, ArgoCD, Prometheus y Grafana**, así como buenas prácticas de despliegue y observabilidad. Sirve como portafolio profesional para roles de DevOps/SRE/Cloud.

---

## Estructura del proyecto

```
devops-showcase/
├── app/                      # Código fuente de la aplicación Flask
│   └── main.py
├── charts/myapp/             # Helm chart para desplegar la app
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── manifests/                # Manifiestos para ArgoCD y Kubernetes
│   └── application.yaml
├── docs/
│   └── dashboards/           # Dashboards de Grafana
│       ├── myapp-dashboard.json
│       └── nodes-metrics.json
├── runbook.md                # Guía de despliegue y troubleshooting
├── README.md                 # Este archivo
└── .gitignore
```

---

## Tecnologías utilizadas

- **Kubernetes** – Orquestación de contenedores  
- **Helm** – Gestión de despliegues y plantillas  
- **ArgoCD** – GitOps para despliegues automáticos  
- **Prometheus** – Recolección de métricas de la aplicación y cluster  
- **Grafana** – Visualización de métricas en dashboards  
- **Flask** – Aplicación ejemplo con métricas Prometheus  

---

## Despliegue del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Hector-Sanchez19/devops-showcase.git
cd devops-showcase
```

### 2. Instalar la aplicación en Kubernetes usando Helm

```bash
kubectl create namespace dev
cd charts/myapp
helm install myapp . -n dev -f values.yaml
```

### 3. Configurar ArgoCD (opcional, si quieres GitOps)

```bash
kubectl apply -f manifests/application.yaml -n argocd
```

- Abre ArgoCD y sincroniza la aplicación:  

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

- URL: `https://localhost:8080`

---

### 4. Monitoreo con Prometheus y Grafana

#### Prometheus

```bash
kubectl port-forward svc/kube-prometheus-prometheus -n monitoring 9090:9090
```

- URL: `http://localhost:9090`  
- Verifica que los targets (`myapp`, `kubelet`, `apiserver`) estén `UP`.

#### Grafana

```bash
kubectl port-forward svc/kube-prometheus-grafana -n monitoring 3000:80
```

- URL: `http://localhost:3000`  
- Credenciales: obtenidas desde el secret `grafana-admin`:

```bash
kubectl get secret grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 -d
```

- Importa los dashboards de `docs/dashboards/`:
  - `myapp-dashboard.json`
  - `nodes-metrics.json`

---

### 5. Probar la aplicación

```bash
kubectl port-forward svc/myapp -n dev 5000:5000
curl http://localhost:5000
curl http://localhost:5000/metrics
```

- Debes recibir **HTTP 200** y métricas Prometheus.

---

## Finalidad del proyecto

- Demostrar **habilidades de DevOps y Observabilidad**  
- Mostrar un **despliegue completo de aplicación microservicio** con Helm y ArgoCD  
- Visualizar métricas de aplicación y cluster con Prometheus y Grafana  
- Servir como **proyecto profesional para LinkedIn/GitHub**

---

## Runbook y troubleshooting

- Revisa `runbook.md` para **pasos de despliegue, errores comunes y soluciones**  
- Incluye instrucciones para limpiar historial de Git si hay archivos grandes

---

## Notas importantes

- Los binarios de Terraform (`.terraform/providers/`) **no están en el repositorio**  
- Para ejecutar Terraform, **descarga los providers automáticamente**

