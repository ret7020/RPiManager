import psutil
import socket
import socket

class Metrics:
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.local_ip = s.getsockname()[0]
        s.close()


    def get_metrics(self):
        temperature = psutil.sensors_temperatures()["cpu_thermal"][0].current
        hostname = socket.gethostname()
        return {"temperature": temperature, "loc_ip": self.local_ip, "hostname": hostname}