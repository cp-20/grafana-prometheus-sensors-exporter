# grafana-prometheus-custom-exporter
A custom exporter that exports CPU temperature and so


## Requirements
- Docker
- lm-sensors

## To Run
`docker-compose up -d`
* The custom exporter runs on :9127 (`curl -X GET http://localhost:9127/metrics`)

## To stop
`docker-compose down -v`

## Acknowledgements
This repo is forked from [shashanklmurthy/grafana-prometheus-custom-exporter](https://github.com/shashanklmurthy/grafana-prometheus-custom-exporter).
