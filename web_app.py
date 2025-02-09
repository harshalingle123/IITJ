from flask import Flask

app = Flask(__name__)

@app.route('/hellow')
def hello_VMS():
    return "<h1>This message from VM2 and send hellow to VM1</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)