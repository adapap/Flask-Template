import logging
from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
app.config['SECRET_KEY'] = r'-\x0c(q\xe0#/\xd4\x9c\x1c\x99\xa2\x16f[\x9b'
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

# Pug - HTML Template Engine
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
# Sass - CSS Preprocessor
Scss(app, static_dir='app/static/css', asset_dir='app/static/scss')

@app.route('/')
def index():
    return render_template('index.pug')