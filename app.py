from flask import Flask, render_template, jsonify, request
import random
import os
app = Flask(__name__)

# 姓名列表
international_list = ['张炜婷', '张景添', '彭洁']
domestic_list = ['詹家雄', '艾志鹏']

@app.route('/')
def index():
    # 从两个组中各选择一个人
    winner_international = random.choice(international_list)
    winner_domestic = random.choice(domestic_list)
    
    return render_template('index.html', winner_international=winner_international, winner_domestic=winner_domestic)

@app.route('/draw', methods=['POST'])
def draw():
    # 从两个组中各选择一个人
    winner_international = random.choice(international_list)
    winner_domestic = random.choice(domestic_list)
    
    return jsonify(winner_international=winner_international, winner_domestic=winner_domestic)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
