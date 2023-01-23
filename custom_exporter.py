import os
import time

from prometheus_client import start_http_server, Gauge
import docker


DOCKER_CLIENT = docker.from_env()

CONTAINER_CPU_USAGE_PERCENT = Gauge('cpu_usage_percent',
                                    'CPU usage percentage  of container', ['container_id', 'container_name', 'container_image'])
CONTAINER_MEMORY_USAGE_BYTES = Gauge('memory_usage_bytes',
                                     'Memory usage in bytes of container', ['container_id', 'container_name', 'container_image'])


def get_stats():
    containers = DOCKER_CLIENT.containers.list()

    for container in containers:
        cstats = container.stats(stream=False)

        container_image = container.attrs["Config"]["Image"].split("@")[0]

        cpu_percent = 0.0
        cpu_percent += float(cstats["cpu_stats"]["cpu_usage"]["total_usage"]) /\
            float(cstats["cpu_stats"]["system_cpu_usage"]) * 100.0

        memory_usage = cstats["memory_stats"]["usage"]

        CONTAINER_CPU_USAGE_PERCENT.labels(container.id, container.name,
                                           container_image).set(cpu_percent)
        CONTAINER_MEMORY_USAGE_BYTES.labels(container.id, container.name,
                                            container_image).set(memory_usage)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8080)
    # Generate some requests.
    while True:
        get_stats()
        time.sleep(1)
