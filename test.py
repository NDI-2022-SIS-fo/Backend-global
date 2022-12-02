import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("je suis connect")


sio.connect("http://localhost:5000")
sio.wait()