import CShift
import EncodingLog
import DecodingLog
import json

from flask import Flask
app = Flask(__name__)
cs = CShift()

@app.route('/api/encode',methods=['POST'])
def postEncode():
    Message = request.json['Message']
    Shift = request.json['Shift']
    encodedMessage = cs.encode(Message, Shift)
    encodeResponse = jsonify({ 'EncodedMessage': encodedMessage })
    logEncoding(json.dumps(encodeResponse))
    return encodeResponse, 200

@app.route('/api/decode',methods=['POST'])
def postDecode():
    Message = request.json['Message']
    Shift = request.json['Shift']
    decodedMessage = cs.decode(Message,Shift)
    decodeResponse = jsonify({ 'DecodedMessage': decodedMessage };
    logDecoding(json.dumps(decodeResponse))
    return decodeResponse, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=23456)