
from time import sleep
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
# log cors errors
app.logger.setLevel('INFO')

app.debug = True
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'Hello World'

@app.route('/arp')
def arp():
    return 'Arp Table'

@app.route('/whois')
def whois():
    return 'Whois'

# Pushing data to the client
@app.route('/push')
def push():
    socketio.emit('packets', {'data': 'Hello World'})
    return 'packets'

@socketio.on('packets')
def sniffer():
    app.logger.info('packets: ')
    socketio.emit('packets', {'data': 'Hello World'})

app.logger.info('Starting app')
if __name__ == '__main__':
    socketio.run(app, debug=True)
