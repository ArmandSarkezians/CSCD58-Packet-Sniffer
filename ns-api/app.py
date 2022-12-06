# pylint: disable=import-error
import socket
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from functionalities import Sniffer, get_arp_table, get_whois, get_nmap
from helpers import load, append, redis_store

thread = None
app = Flask(__name__)

app.logger.setLevel('INFO')
app.debug = True
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*",  async_mode='threading')
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

def emitter(channel, data):
    socketio.emit(channel, data)
    # print(data)

RAT = Sniffer(emitter)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/arp')
def arp():
    return get_arp_table()

@app.route('/nmap')
def nmap():
    return get_nmap()

@app.route('/lookup/<ip>')
def lookup(ip):
    whois = get_whois([ip])[0].to_json()
    nmap = get_nmap(ip)
    return {
        "whois": whois,
        "nmap": nmap
    }


@app.route('/whois')
def whois():
    res = map(lambda x: x.to_json(), get_whois())
    return list(res)

@app.route('/load_packets')
def load_packets():
    events = [] # redis_store.lrange("packets", 0, -1 )
    return events

@socketio.on('disconnect')
def stop_sniffing():
    global thread
    RAT.stop()


@app.route('/start_sniffing')
def start_sniffer():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=sniffer)
        return 'Sniffer started'
    else:
        RAT.start()
        return 'Sniffer Resumed'

@socketio.event
def sniffer():
    print("Listening for packets...\n")
    RAT.start()

if __name__ == '__main__':
    app.logger.info('Starting app')