from CB import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    f=open("chat_history.txt",'a')
    f.write(userText+'\n')
    ans=str(chatbot.get_response(userText))
    f.write(ans+'\n')
    f.close()
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True) 