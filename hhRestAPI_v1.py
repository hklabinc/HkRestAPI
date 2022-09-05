from flask import Flask
app = Flask (__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user')
def hello_user():
    return 'Hello, User!'

@app.route('/user2/<userName>') # URL뒤에 <>을 이용해 가변 경로를 적는다
def hello_user2(userName):
    return 'Hello, %s'%(userName)

if __name__ == "__main__":
    app.run()