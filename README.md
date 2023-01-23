# grafana-prometheus-custom-exporter
A Custom exporter that exports docker metrics for cpu and memory

## Requirements
* docker
* docker-compose
## To Run
`docker-compose up -d`
* The custom exporter runs on :8080 (`curl -X GET http://localhost:8080/metrics`)
* Grafana runs on port :3000 (Use admin/admin as the username/pwd for first login). Prometheus(`:9090`) is automatically configured as a datasource for grafana
## To stop
`docker-compose down -v`
