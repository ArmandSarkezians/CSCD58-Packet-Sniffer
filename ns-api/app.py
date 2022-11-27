# pylint: disable=import-error
import time, socket
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from structures import Ethernet, IPv4, TCP, UDP, ICMP

app = Flask(__name__)
CORS(app)
# log cors errors
app.logger.setLevel('INFO')

app.debug = True
socketio = SocketIO(app, cors_allowed_origins="*",  async_mode='threading')
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
thread = None

@app.route('/')
def index():
    return 'Hello World'

@app.route('/arp')
def arp():
    return 'Arp Table'

@app.route('/whois')
def whois():
    return 'Whois'


@socketio.on('connect')
def emit_market_data():
    global thread
    emit('packets', "sniffer")
    if thread is None:
        emit('packets', "start sniffer")
        thread = socketio.start_background_task(target=sniffer)


@socketio.event
def sniffer():
    print("Listening for packets...\n")
    while True:
        raw_data, addr = s.recvfrom(65536)
        hdr = Ethernet(raw_data)
        # Protocol 8 is for IPv4
        if hdr.protocol == 8:
            ipv4 = IPv4(raw_data)

            # Protocol 1 is for ICMP
            if ipv4.protocol == 1:
                icmp = ICMP(ipv4.raw_data)
                socketio.emit('packets', icmp)
                print(icmp)
            # Protocol 6 is for TCP
            elif ipv4.protocol == 6:
                tcp = TCP(ipv4.raw_data)
                socketio.emit('packets', tcp)
                print(tcp)
            # Protocol 17 is for UDP
            elif ipv4.protocol == 17:
                udp = UDP(ipv4.raw_data)
                socketio.emit('packets', udp)
                print(udp)
            # Other protocols
            else:
                print("Other protocol: ", ipv4.protocol)
                socketio.emit('packets', ipv4.protocol)
        # Other protocols
        else:
            print("Other protocol: ", hdr)
            socketio.emit('packets', hdr)

if __name__ == '__main__':
    app.logger.info('Starting app')