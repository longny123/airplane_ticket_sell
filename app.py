from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("HomePage.html")

@app.route('/SignIn', methods=['GET','POST'])
def sign_in_sign_up():
    return render_template("SignInPage.html")

@app.route('/Logined', methods=['GET'])
def logined():
    return render_template("LogIned.html")


if __name__ == '__main__':
    app.run()
