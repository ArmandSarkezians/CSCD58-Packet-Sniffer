# Network Sniffer

Created by:

- Ahmed Halat (1006332951, halatahm)
- Mohamed Halat (1006322962, halatmoh)
- Armand Sarkezians (1006020574, sarkezi1)

for CSCD58 Winter 2022.

## Description and Goals

## Contributions
### Ahmed Halat

### Mohamed Halat

### Armand Sarkezians

## Running the Sniffer
The runner is divided into 2 sections, a backend and a frontend. The backend is responsible for sniffing the network and the frontend is responsible for displaying the data, each in their own terminal.
Instructions for setting up and running each are available in the READMEs in their respective directories. The backend runs best on a Linux machine, while the frontend can be run on any machine.

## Implementation and Documentation

### Backend
We used a few different tools to implement this project. The backend is written in python and runs with Flask and [SocketIO](https://flask-socketio.readthedocs.io/en/latest/).

#### Sniffing
In order to perform packet sniffing on the backend, we used the [Recvfrom](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom) function from the python socket library. This function allows us to receive data from a socket, and returns the data and the address of the sender.

The raw data from the socket is used to initialize the [Ethernet Object](ns-api/structures/ethernet.py) we created. This object is parses the Ethernet header data and stores the rest of the raw object data.
We then initialize the [IP Object](ns-api/structures/ipv4.py) and pass it the raw data from the Ethernet object. This object parses the IP header data and stores the rest of the raw object data. We then use the protocol number from the IP header to determine which protocol to initialize next. We initialize either the [TCP Object](ns-api/structures/tcp.py), [UDP Object](ns-api/structures/udp.py), or [ICMP Object](ns-api/structures/icmp.py) and pass it the raw data from the IP object. This object parses the protocol header data and stores the rest of the raw object data and is finally returned to the frontend through the SocketIO connection.

#### Arptables, Whois and Nmap
The implementation for fetching ARPTables, whois and nmap information is very similar. We use the python [subprocess](https://docs.python.org/3/library/subprocess.html) library to run the respective commands and return the output.
In the case of ARPTables and Whois, we also use [re](https://docs.python.org/3/library/re.html) to parse the output and return it in a more readable format. This required building out custom regex patterns for each command as seen in the [Whois Object](ns-api/structures/whois.py).

### Frontend
Our frontend is built using [Angular](https://angular.io/), a popular Typescript framework. The frontend UI is mainly designed and built by us, with a few components from [PrimeNG](https://www.primefaces.org/primeng/), a popular UI library for Angular. We also used [NGX-SocketIO](https://www.npmjs.com/package/ngx-socket-io) to connect to the SocketIO server on the backend.
## Analysis

## Conclusion
