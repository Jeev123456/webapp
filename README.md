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

ref https://github.com/Jeev123456/webapp/blob/main/webapp-helm/README.md

          
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
        
ref https://github.com/Jeev123456/webapp/blob/main/webapp-helm/README.md
    
5.  **Verify the deployment:**
    
    
    kubectl get pods
    kubectl get services
    kubectl get ingress

` 
    
6.  **Access the application using the specified domain.**
## Key Points:

-   **simple_webapp.py:** This file contains a basic Flask web application that returns the current date and time when accessed.
    
-   **Helm Chart (`webapp-helm`):** The Helm chart provides a standardized way of packaging, deploying, and managing Kubernetes applications. It includes configurations for deployment, service, and ingress for the web application.
