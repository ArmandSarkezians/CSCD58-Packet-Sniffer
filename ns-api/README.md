# Pre-reqs
```sh
# redis
sudo add-apt-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get install redis
```

# Installing
```bash
sudo systemctl enable redis-server
sudo systemctl start redis-server
sudo apt-get install python3-pip
pip3 install -r requirements.txt
```

# Setup
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

# Running
```bash
flask run
```