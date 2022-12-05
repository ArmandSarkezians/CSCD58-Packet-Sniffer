# Installing
```bash
sudo systemctl enable redis-server
sudo systemctl start redis-server
# sudo apt-get install python3-pip
pip3 install -r requirements.txt

# Some linux distributions do not come with whois preinstalled:
sudo apt-get install whois
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