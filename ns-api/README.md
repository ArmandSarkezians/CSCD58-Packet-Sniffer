# Installing

```bash
# sudo apt-get install python3-pip
pip3 install -r requirements.txt

# Some linux distributions do not come with whois preinstalled:
sudo apt-get install whois
```

# Setup

```bash
export FLASK_APP=app.py
```

# Running

```bash
flask run
```

# Common Errors

## Error: ModuleNotFoundError: No module named 'flask'

```bash
pip3 install flask
```

## Error: ModuleNotFoundError: No module named 'whois'

```bash
sudo apt-get install whois
```

## Error: PermissionError: [Errno 1] Operation not permitted

```bash
# Run the app with:
sudo flask run
```

## Error: Port 5000 is in use by another program

```bash
# Be warned this is an aggressive way to kill a process
sudo kill -9 $(lsof -t -i:5000)$

# If the above does not work then you must change the backend location
# in ns-ui/src/environments/environment.ts to a new port number (5001 lets say)
# and run the app with:
sudo flask run --port 5001
```
