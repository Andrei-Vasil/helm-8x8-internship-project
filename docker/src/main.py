from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def go():
    return 'hello world'

def main():
    app.run(host='0.0.0.0', port='80')


if __name__ == "__main__":
    main()
