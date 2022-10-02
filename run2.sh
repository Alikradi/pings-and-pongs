export FLASK_APP=ping.py
flask run --host 0.0.0.0 --port 5001
export FLASK_DEBUG=1
flask run
