from flask import Flask, render_template, request

import chatbot

app = Flask(__name__)
test_list = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clear')
def clear():
    test_list.clear()
    return render_template('index.html')


@app.route('/home', methods=["POST"])
def home():
    user_input = request.form["user_input"]
    bot_message = chatbot.chat(user_input)
    test_list.insert(0, bot_message)
    test_list.insert(0, user_input)
    return render_template('index.html', user_input=user_input, messages=test_list)


if __name__ == '__main__':
    app.run(debug=True, port=5002)