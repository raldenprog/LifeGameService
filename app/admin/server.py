from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    login = None
    if request.method == 'GET':
        login = request.args.get('login', None)
    if login:
        return login
    else:
        return "Hello"


if __name__ == '__main__':
    app.run()
