from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def blog():
    return render_template('blog.html',title='blog')


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=5000)
