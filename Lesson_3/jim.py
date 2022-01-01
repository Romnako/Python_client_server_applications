from datetime import datetime

TIME = datetime.now().replace(microsecond=0).isoformat()

RESPONSE = {
    'response': None,
    'time': str(TIME),
    'alert': None,
    'from': "Server",
    'contacts': None
}

PRESENCE = {
    "action": "presence",
    "time": str(TIME),
    "type": "status",
    "user": {
        "account_name":'',
        "status": "I am!"
    }

}

MESSAGE = {
    "action": "presence",
    "time": str(TIME),
    "to": None,
    "message": None
}

SERV_RESP =  (
    ('200', 'OK'),
    ('401', 'Do not authorize'),
    ('404', 'Not found')
)