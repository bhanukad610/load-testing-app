python3 -m venv venv
source venv/bin/activate
locust -f src/locust.py --host https://www.bbc.com/