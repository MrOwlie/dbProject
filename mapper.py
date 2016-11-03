from flask import Flask
from flask import render_template
import pyjade
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def root():
    return render_template('index.jade')


if __name__ == '__main__':
    app.run()
