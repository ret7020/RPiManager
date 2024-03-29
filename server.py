from flask import Flask, render_template, jsonify
from metrics import Metrics
import cv2
import threading
from config import *

cap = cv2.VideoCapture(CAMERA_IP)

ret, IMG = cap.read()
def loop():
    global IMG
    while True:
        ret, IMG = cap.read()

class MonitorApp:
    def __init__(self, name, host='0.0.0.0', port='8000'):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True

        ## UI routes
        @self.app.route('/')
        def __index():
            return self.index()
        
        @self.app.route('/camera')
        def __camera():
            return self.cam()

        ## API route
        @self.app.route('/api/poll_metrics')
        def __polling():
            return self.polling()
        
        


    def run(self):
        self.app.run(host=self.host, port=self.port)

    def render_table(self, metrics_data):
        return render_template("metrics_table.html", temperature=metrics_data["temperature"], temp_ok=10 <= metrics_data["temperature"] <= 75, ip=metrics_data["loc_ip"], hostname=metrics_data["hostname"], wifi_net_status=metrics_data["wifi_net_status"], wifi_net_name=metrics_data["wifi_net_name"], cpu_load=metrics_data["cpu_load"], ram_load=metrics_data["ram_load"], sd_load=metrics_data["sd_load"], uptime=metrics_data["uptime"])
    def index(self):
        metrics_data = mtr.get_metrics()
        return render_template("index.html", table_data=self.render_table(metrics_data))
    def polling(self):
        metrics_data = mtr.get_metrics()
        return {"status": True, "data": "metrics_data", "html_table": self.render_table(metrics_data)}
    
    def cam(self):
        global IMG
        cv2.imwrite("/home/pi/Documents/Progs/RPiWebMonitor/static/images/frame.png", IMG)
        return "<img src='/static/images/frame.png'>"


if __name__ == "__main__":
    threading.Thread(target=lambda: loop()).start()
    mtr = Metrics()
    app = MonitorApp(__name__)
    app.run()
