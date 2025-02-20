# 2주차에 완성한 쇼핑몰에 두 가지 기능 추가하기
# 1) 주문하기(POST): 정보 입력 후 '주문하기' 버튼클릭 시 주문목록에 추가
# 2) 주문내역보기(GET): 페이지 로딩 후 하단 주문 목록이 자동으로 보이기

from flask import Flask, render_template, jsonify, request

app = Flask(__name__) 

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')

# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name' : name_receive,
        'count' : count_receive,
        'address' : address_receive,
        'phone' : phone_receive
    }

    db.candle.insert_one(doc)

    return jsonify({'msg':'주문이 완료되었습니다!'})

# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.candle.find({}, {'_id':False}))
    return jsonify({'all_orders':orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)