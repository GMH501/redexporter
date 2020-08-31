# Redexporter
Prometheus metrics exporter for Redmine application.

## Getting Started

### Running in Docker
```
$ docker run -d -p 8080:8080 --name redexporter gmh501/redexporter \
-e REDMINE_URL=<redmine_url> \ 
-e REDMINE_USER=<redmine_user> \ 
-e REDMINE_PASSWORD=<redmine_password>
```
