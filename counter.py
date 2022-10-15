from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/about")
def about(): 
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())
    
count = 0
    
@app.route('/', methods=['GET'])
def home():
    return str(count)
    
@app.route('/stat', methods=['GET'])
def stat():
    global count
    count+=1
    return str(count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)