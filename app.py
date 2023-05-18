from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/api/hello')
def doctors():
    return jsonify({"message":"Success deploy done dockerfile","status":200})

if __name__ == '__main__':
    app.run(debug=True, port='3333',host='0.0.0.0')