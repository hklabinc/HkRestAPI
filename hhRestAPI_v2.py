from flask import Flask, request, jsonify
app = Flask(__name__)
 
@app.route('/userLogin', methods = ['POST'])        # POST 방식 (HTTP Body에 데이터를 추가하여 요청하는 방식)
def userLogin():
    user = request.get_json()   # json 데이터를 받아옴
    return jsonify(user)        # 받아온 데이터를 다시 전송
 
@app.route('/environments/<language>')              #  GET 방식 - URI에 주소에 파라미터를 추가하여 요청하는 방식 (HTTP Header에 추가하는 방식)
def environments(language):
    return jsonify({"language":language})
 
 
if __name__ == "__main__":
    app.run()
