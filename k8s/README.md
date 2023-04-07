## Build docker container

### cd into app folder

```bash
docker build -f Dockerfile -t flask-demo:latest .
docker run -p 5000:5000 flask-demo
```

## Create kubernets deployment and service

### cd into k8s folder

```bash
kubectl create --filename deployment.yaml
kubectl create --filename service.yaml
minikube image load flask-demo:latest
kubectl get all
```

## Test service

```bash
minikube tunnel
kubectl get services
```
