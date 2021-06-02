from etc.app import app

DEBUG = True
PORT = 5000

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)