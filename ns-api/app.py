# pylint: disable=import-error
import config, time, socket
from redis import Redis
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from functionalities import Sniffer, get_arp_table, get_whois

thread = None
app = Flask(__name__)
CORS(app)

app.logger.setLevel('INFO')
app.debug = True

redis_store = Redis.from_url(config.REDIS_URL)
socketio = SocketIO(app, cors_allowed_origins="*",  async_mode='threading')
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

arptable = get_arp_table()
redis_store.set("arptable", arptable)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/arp')
def arp():
    return get_arp_table()

@app.route('/whois')
def whois():
    return get_whois()


@socketio.on('connect')
def start_sniffer():
    global thread
    emit('packets', "sniffer")
    if thread is None:
        emit('packets', "start sniffer")
        thread = socketio.start_background_task(target=sniffer)


@socketio.event
def sniffer():
    rat = Sniffer(socketio, redis_store)
    rat.sniff()


if __name__ == '__main__':
    app.logger.info('Starting app')