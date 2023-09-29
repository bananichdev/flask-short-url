from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import datetime
import requests

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


def shortener(url):
    url = f'https://clck.ru/--?url={url}'
    response = requests.get(
        url
    )
    return response.text


class URLForm(FlaskForm):
    original_url = StringField(
        'Вставьте ссылку',
        validators=[DataRequired(message='Поле не должно быть пустым'),
                    URL(message='Неверная ссылка')]
    )
    submit = SubmitField(
        'Получить короткую ссылку'
    )


class URLModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    short_url = db.Column(db.String(255), nullable=False)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        new_url = URLModel()
        new_url.original_url = form.original_url.data
        new_url.short_url = shortener(new_url)
        db.session.add(new_url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template(
        'index.html',
        form=form
    )


@app.route('/urls')
def urls():
    urls_list = URLModel.query.all()
    return render_template(
        'urls.html',
        urls_list=urls_list
    )


@app.route('/<int:id>')
def redirect_to_url(id):
    query = URLModel.query.get(id)
    query.visits += 1
    url = query.original_url
    db.session.add(query)
    db.session.commit()
    return redirect(
        url
    )
