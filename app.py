from etc.app import app

DEBUG = False
PORT = 5000

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)