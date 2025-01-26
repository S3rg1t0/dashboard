from flask import Flask, jsonify, render_template

from snap7.client import Client
from snap7.util import get_int

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/readPLC')
def readPLC():
    client = Client()
    client.connect(address='192.168.0.1',
                   rack=0,
                   slot=1)

    data = client.db_read(db_number=100,
                          start=0,
                          size=10)
    data_int = get_int(data, 0)
    data_int_1 = get_int(data, 2)
    data_int_2 = get_int(data, 4)
    data_int_3 = get_int(data, 6)
    client.disconnect()
    return jsonify({
        'data_int': data_int,
        'data_int_1': data_int_1,
        'data_int_2': data_int_2,
        'data_int_3': data_int_3,
    })


if __name__ == '__main__':
    app.run()
