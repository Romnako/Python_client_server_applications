from datetime import datetime

TIME = datetime.now().replace(microsecond=0).isoformat()

RESPONSE = {
    "response": None,
    "time": str(TIME),
    "alert": None,
    "from": 'Server',
    "contacts": []
}

PRESENCE = {
    "action": "presence",
    "time": str(TIME),
    "type": "status",
    "user": {
        "account_name": '',
        "status": "I am here!"
    }
}

MESSAGE = {
    "action": "msg",
    "time": str(TIME),
    "from": None,
    "to": None,
    "message": None
}

SERV_RESP = (
    ('200', 'OK'),
    ('401', 'Not log in'),
    ('404', 'Not found')
)