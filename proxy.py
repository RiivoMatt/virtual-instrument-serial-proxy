from serial import Serial
import socketio

serial_port_name = 'COM3'
URL = "http://10.25.184.188:8000"

sio = socketio.Client()

# arduino = Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
serial_port = Serial(port=serial_port_name, baudrate=9600, timeout=.1)

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')
    
sio.connect(URL)

while True:
    line = serial_port.readline().decode('utf-8').strip()
    
    if line:
        print(line)
        sio.emit('send-data', {'sample': line})
  




