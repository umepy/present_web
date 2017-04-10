from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def index():
    title='プレゼント案集計'
    message='プレゼント案の提案をお願いします．(e.g.　靴下)'
    return render_template('index.html',message=message,title=title)

@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "送信完了"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        dic={}
        name = request.form['name']
        present = request.form['present']
        with open('C:/Users/Haru/PycharmProjects/present_web/save.json', 'r') as file:
              dic = json.load(file)
        dic[name]=present
        with open('C:/Users/Haru/PycharmProjects/present_web/save.json', 'w') as file:
            json.dump(dic,file)
        print(dic)
        # index.html をレンダリングする
        return render_template('index.html',
                               name=name+'さん，提案ありがとうございました', title=title)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000)
