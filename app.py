from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
Socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@Socketio.on('message')
def handleMessage(msg):
    print("Message:", msg)
    send(msg, broadcast = True)
if __name__ == '__main__':
    Socketio.run(app, port=3000, debug=True, host="0.0.0.0")
 
