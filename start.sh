python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

sudo python3 ctl_gen.py
echo Please configure nginx.
echo standart port is 8790
echo Also you need to gen key `python3 keygen -n <key name>`