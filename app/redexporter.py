import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
from random import randint


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        g = GaugeMetricFamily("MemoryUsage", 'Help text', labels=['instance'])
        g.add_metric(["instance01.us.west.local"], 20)
        yield g

        c = CounterMetricFamily("HttpRequests", 'Help text', labels=['app'])
        c.add_metric(["example"], randint(0, 300))
        yield c


if __name__ == '__main__':
    start_http_server(8080)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)