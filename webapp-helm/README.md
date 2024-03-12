# Helm Chart Details:
## Overview

The Web Application Helm Chart (webapp-helm) simplifies the deployment of a production-ready simple web application on Kubernetes. The chart is hosted on the S3 bucket `jeevana-webapp-helm` at the path `/charts` and consists of the following key files:

-   **Chart.yaml**: Describes metadata about the Helm chart, including its name, description, version, and API version.
    
-   **values.yaml**: Contains configurable parameters for the deployment, such as replica count, image details, service settings, resource limits, and ingress configurations.
    
-   **deployment.yaml**: Defines the Kubernetes Deployment resource, specifying the number of replicas, container image, and resource limits for the web application.
    
-   **ingress.yaml**: Configures the Kubernetes Ingress resource, enabling external access to the web application. Host, path, and rewrite rules are customizable.
    
-   **service.yaml**: Specifies the Kubernetes Service resource, defining how the web application is exposed within the Kubernetes cluster.
    

## Usage

1.  **Configure AWS Access Keys:** Before fetching the Helm chart from the S3 bucket, ensure that your AWS CLI is configured with the necessary access keys. Run the following command and follow the prompts:
    
    bashCopy code
    
    `aws configure` 
    
    This step is crucial for accessing the S3 bucket (`jeevana-webapp-helm`) and fetching the Helm chart.
    
2.  **Add the S3 bucket as your Helm repository:**
    
    bashCopy code
    
    `helm repo add webapp-repo s3://jeevana-webapp-helm/charts/` 
    
3.  **Clone the Helm chart repository:**
    

    
    `helm fetch webapp/webapp --version 0.1.0` 
    
4.  **Customize values in the `values.yaml` file according to specific deployment requirements.**
    
5.  **Deploy the Helm chart using the following command:**

    
    `helm install <release-name> webapp-helm-0.1.0.tgz` 
    
    Replace `<release-name>` with the desired Helm release name. The Helm chart is fetched from the S3 bucket, and the deployment is based on the specified configurations.
    
