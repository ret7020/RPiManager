# RPiManager
You can monitor your Raspberry PI status real time from any place using adaptive(mobile & pc) web interface!

## Demo
![image](https://user-images.githubusercontent.com/55328925/191785303-71c6e480-5fb2-4bb6-831d-aaa82758fae9.png)

## Installation
1. Clone this repository on your raspberry pi
```
git clone https://github.com/ret7020/RPiManager/
cd RPiManager
```
2. Install python modules</br>
```
pip3 install -r requirements.txt
```
3. Run web server</br>
```
python3 server.py
```
4. Open 'http://RPI_IP:8080/' in web browser

## White IP
If you don't have white ip you can tunnel web port using ngrok or local tunnel(lt).