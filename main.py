import helper, const
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/healthz')
def health():
	return 'Service Running Health Check Passed!'

@app.route('/set', methods=["POST"])
def insert_data():
    resp = helper.validate_request(request.json)
    
    if resp == -1:
        return jsonify(const.INV_INP_MSG)
    
    if resp == 1:
        return jsonify(const.INV_MSG)
    
    key = request.json['key']
    value = request.json['value']

    resp = helper.insert(key, value)
    
    if resp == 0:
        return jsonify(const.INS_S_MSG)
    
    return jsonify(const.INS_F_MSG)
    
@app.route('/get/<key>')
def get_key(key):
    resp = helper.get(key)
    
    if resp == None:
        return jsonify(const.NF_MSG)
    
    return jsonify({'Message':"Key `{0}` Found".format(key),"value":resp})

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    query = {}
    
    if "prefix" not in args:
        query["prefix"]  = ""
    else:
        query["prefix"] = args["prefix"]
    
    if 'suffix' not in args:
        query["suffix"] = ""
    else:
        query["suffix"] = args["suffix"]
    
    result = helper.search(query["prefix"], query["suffix"])
    
    return jsonify({"data":result})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3300)
