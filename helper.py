DATASTORE = {}

def insert(key, value):
    DATASTORE[key] = value
    return 0

def get(key):
    if key in DATASTORE:
        return DATASTORE[key]
    return None

def search(prefix, suffix):
    result = {}
    if prefix == "" and suffix == "":
        return DATASTORE
    if prefix != "":
        for key in DATASTORE:
            if key.startswith(prefix):
                result[key] = DATASTORE[key]
    elif suffix != "":
        for key in DATASTORE:
            if key.endswith(suffix):
                result[key] = DATASTORE[key]
    return result
    
def validate_request(req):
    # return -1 for invalid input
    # return 1 for incomplete input
    # return 0 if can be inserted
    if "key" not in req or "value" not in req:
        return -1
    if req["key"] == "":
        return 1
    return 0