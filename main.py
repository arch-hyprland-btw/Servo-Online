#For Pi Pico 2W (Also Works on Pico W)

import network
import socket
import time
from machine import Pin
from servo import Servo

# setup
servo = Servo(pin_id=28)  # control pin
angle = 0

# create AP
ap = network.WLAN(network.AP_IF)
ap.config(essid='Servo Control', password='servo-control') 
ap.active(True)

print("Starting access point...")
while not ap.active():
    pass
print('Access Point active')
print('Connect to Wi-Fi SSID:', ap.config('essid'))
print('IP address:', ap.ifconfig()[0])

#Webpage
html = """<!DOCTYPE html>
<html>
<head>
<title>Servo Controll</title>
<style>
  body { font-family: sans-serif; text-align: center; margin-top: 40px; }
  button { margin: 5px; padding: 15px 25px; font-size: 18px; }
</style>
<script>
let intervalId = null;

function startAdjust(dir) {
  // send first immediately
  fetch('/adjust?dir=' + dir);
  // then repeat every 200ms
  intervalId = setInterval(() => {
    fetch('/adjust?dir=' + dir);
  }, 200);
}

function stopAdjust() {
  if (intervalId) {
    clearInterval(intervalId);
    intervalId = null;
  }
}
</script>
</head>
<body>
  <h2>Servo Control</h2>
  <button onclick="fetch('/set?angle=0')">0</button>
  <button onclick="fetch('/set?angle=45')">45</button>
  <button onclick="fetch('/set?angle=90')">90</button>
  <button onclick="fetch('/set?angle=135')">135</button>
  <button onclick="fetch('/set?angle=180')">180</button><br>
</body>
</html>
"""

# Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)

# Main Loop
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024).decode()
        print("Request:", request)

        # handle commands
        if '/set?angle=' in request:
            try:
                new_angle = int(request.split('/set?angle=')[1].split(' ')[0])
                angle = max(0, min(180, new_angle))
            except:
                pass



        # move servo
        servo.write(angle)
        print("Servo set to:", angle)

        # send web page
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()

    except Exception as e:
        print("Error:", e)
        try:
            cl.close()
        except:
            pass


