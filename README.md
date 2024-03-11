# Containerized Application Deployment and Infrastructure Orchestration

## Summary:

This project demonstrates the deployment of a simple web application using Docker containers and Kubernetes. The application, built with Flask, displays the current date and time when accessed. The project includes a Dockerfile for building the container image, a Helm chart for Kubernetes deployment, and relevant configurations.

## Project Structure:

webapp 
├── app 
│ ├── requirements.txt 
│ └── simple_webapp.py 
├── Dockerfile



 ### Dockerfile:
 

    FROM python:3.9-slim
    WORKDIR /app
    COPY ./app/* /app/
    RUN pip install --no-cache-dir -r requirements.txt
    EXPOSE 5000
    CMD ["python", "simple_webapp.py"]

### simple_webapp.py:



    from flask import Flask
    import datetime
    
    app = Flask(__name__)
    
    @app.route('/')
    def print_current_date():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Current Date and Time: {current_date}"
    
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)

### requirements.txt:

    flask
    datetime 


    

## Helm Chart Details:

The Helm chart (`webapp-helm`) is available on an S3 bucket named `jeenana-webapp-helm`.

### Helm Chart Structure:



├── Chart.yaml
├── templates
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── service.yaml
└── values.yaml` 

#### Chart.yaml:


    apiVersion: v2
    name: webapp
    description: A Helm chart for deploying a production-ready simple web application
    version: 0.1.0

#### values.yaml:



    replicaCount: 2  
    image:
      repository: "jeev123456/webapp"  
      tag: "latest"
      pullPolicy: Always  
      registrySecret: regcred
    service:
      name: webapp-service
      type: ClusterIP 
      port: 5000
      targetPort: 5000
    
    resources:
      limits:
        cpu: 200m
        memory: 256Mi
      requests:
        cpu: 100m
        memory: 128Mi
    
    ingress:
      enabled: true
      path: /
      annotations:
        nginx.ingress.kubernetes.io/rewrite-target: /
      hosts:
        - host: your-domain.com  
          paths:
            - /

#### deployment.yaml:


    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: {{ .Release.Name }}
    spec:
      replicas: {{ .Values.replicaCount }}
      selector:
        matchLabels:
          app: webapp
      template:
        metadata:
          labels:
            app: webapp
        spec:
          containers:
          - name: webapp
            image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
            ports:
            - containerPort: 5000
            resources:
              limits:
                cpu: {{ .Values.resources.limits.cpu }}
                memory: {{ .Values.resources.limits.memory }}
              requests:
                cpu: {{ .Values.resources.requests.cpu }}
                memory: {{ .Values.resources.requests.memory }}
          imagePullSecrets:
          - name: {{ .Values.image.registrySecret }}` 
    
    #### ingress.yaml:
    
    
    `apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: {{ .Release.Name }}-ingress
      annotations:
        nginx.ingress.kubernetes.io/rewrite-target: /
    spec:
      ingressClassName: nginx  
      rules:
      - host: {{ .Values.ingress.host }}
        http:
          paths:
          - path: {{ .Values.ingress.path }}
            pathType: Prefix
            backend:
              service:
                name: {{ .Values.service.name }}
                port:
                  number: {{ .Values.service.port }}

#### service.yaml:



    apiVersion: v1
    kind: Service
    metadata:
      name: {{ .Values.service.name }}
    spec:
      selector:
        app: webapp
      ports:
        - protocol: "TCP"
          port: {{ .Values.service.port }}
          targetPort: {{ .Values.service.targetPort }}
          
## Prerequisites:

-   Minikube
-   Enable Ingress in Minikube

### Kubernetes Secrets Creation:

`kubectl create secret docker-registry regcred \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=jeevanareddy005@gmail.com \
  --docker-password=<password>` 

## Setup Instructions:

1.  **Clone the repository:**
    


     git clone https://github.com/Jeev123456/webapp
      cd webapp
    
2.  **Build the Docker image:**
    

    
    `docker build -t webapp .` 
3.   **Push the Docker image to Docker Hub:**

   `docker push jeev123456/webapp`
    
4.  **Deploy the Helm chart:**
        
    `helm install webapp ./webapp-helm` 
    
5.  **Verify the deployment:**
    
    
    kubectl get pods
    kubectl get services
    kubectl get ingress

` 
    
6.  **Access the application using the specified domain.**
## Key Points:

-   **simple_webapp.py:** This file contains a basic Flask web application that returns the current date and time when accessed.
    
-   **Helm Chart (`webapp-helm`):** The Helm chart provides a standardized way of packaging, deploying, and managing Kubernetes applications. It includes configurations for deployment, service, and ingress for the web application.
