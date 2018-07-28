#! /usr/bin/python3.6

try:
    import docker
    from flask import Flask
except ImportError as e:
    print('Please install the requirements file by using: pip install -r requirements.txt before continuing.\n{}'
          .format(e))

app = Flask(__name__)

@app.route('/')
def DoomsDay():
    return "Hello :)"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
