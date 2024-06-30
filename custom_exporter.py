import os
import time

from prometheus_client import start_http_server, Gauge
import sensors

CPU_TEMPERATURE = Gauge('cpu_temperature_celsius', 'CPU temperature (℃)', ['chip', 'core'])

def get_stats():
    
    sensors.init()
    try:
        for chip in sensors.iter_detected_chips():
            for feature in chip:
                CPU_TEMPERATURE.labels(chip, feature.label).set(feature.get_value())
    finally:
        sensors.cleanup()


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(os.environ.get('PORT', 9127))
    # Generate some requests.
    while True:
        get_stats()
        time.sleep(1)
