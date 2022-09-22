import psutil
import socket
import subprocess
from time import time
from utils import convert_seconds_to_time_spent

class Metrics:
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.local_ip = s.getsockname()[0]
        s.close()

    def get_metrics(self):
        temperature = psutil.sensors_temperatures()["cpu_thermal"][0].current
        cpu_load = psutil.cpu_percent()
        ram_load = psutil.virtual_memory().percent
        sd_load = psutil.disk_usage('/').percent
        seconds_from_boot = time() - psutil.boot_time()
        uptime = convert_seconds_to_time_spent(seconds_from_boot)

        hostname = socket.gethostname()
        subprocess_result = subprocess.Popen('iwget',shell=True,stdout=subprocess.PIPE)
        subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
        wifi_data = subprocess_output[0].decode('utf-8')
        try:
            wifi_net_name = wifi_data.split(" ")[5]
            wifi_net_status = "WIFI connected"
        except:
            wifi_net_name = "NONE"
            wifi_net_status = "NO WIFI"

        return {"temperature": temperature, "cpu_load": cpu_load, "ram_load": ram_load, "sd_load": sd_load ,"loc_ip": self.local_ip, "hostname": hostname, "wifi_net_name": wifi_net_name, "wifi_net_status": wifi_net_status, "uptime": uptime}
