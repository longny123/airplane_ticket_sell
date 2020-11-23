from flask import render_template
from server import create_app

app = create_app()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/admin')
def admin():
    return render_template("Admin/index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
