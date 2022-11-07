from flask import Flask, render_template
import json
from numbers import Real
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from celery import Celery
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask import request, jsonify

db = create_engine('postgresql+psycopg2://jjjvxftvljouqa:a41a7e3069600c2daa7ed7e917e26216fbd28f517719f517c4529b994bb8e430@ec2-34-248-169-69.eu-west-1.compute.amazonaws.com:5432/dfmbp1l6kre1rn')
# create the app
app = Flask(__name__)

CORS(app, supports_credentials=True, allow_headers=True)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

base = declarative_base()

Session = sessionmaker(db)
session = Session()


ma = Marshmallow(app)

@app.cli.command('db_create')
def db_create():
    base.metadata.create_all(db)
    print('Database created')


@app.route("/db_create")
def db_create_all():
    base.metadata.create_all(db)




class Answers(base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    a1 = Column(String(50), nullable=False)
    a2 = Column(String(50), nullable=False)
    a3 = Column(String(50), nullable=False)
    a4 = Column(String(50), nullable=False)
    answer_name = Column(String(50), nullable=False)
    answer_n = Column(Integer, nullable=False)
    date_time = Column(DateTime, nullable=False)

class AnswersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'a1', 'a2', 'a3', 'a4', 'answer_name', 'answer_n', 'date_time')

answers_schema = AnswersSchema()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




@app.route("/get_answer")
def get_answer():
    title = "Title"
    a1 = 'a1'
    a2 = 'a2'
    a3 = 'a3'
    a4 = 'a4'
    answer_name = 'answer_name'
    answer_n = 1
    date_time = '2022-11-07'
    answer = Answers( title=title , a1=a1,
                a2=a2, a3=a3, a4=a4,answer_name=answer_name, answer_n=answer_n, date_time=date_time)
    print(answer)
    session.add(answer)
    session.commit()
    test = session.query(Answers).filter_by(title=title).first()
    print(test)
    # data = AnswersSchema.dump(test)
    # print(data)

    return "Some answer"

@app.route("/save")
def save():
    f = open('data.json', 'r+', encoding='utf-8')
    json_file = json.load(f)
    ln = len(json_file)
    dt = {
    "id":ln,
    "name":"noname",
    "description":"no description"
    }
    json_file.append(dt)
    json_data = json.dumps(json_file, indent=4, ensure_ascii=False)
    f = open('data.json', 'w', encoding='utf-8')
    f.write(json_data)
    f.close()
    return json_data

@app.route("/check_data")
def check():
    f = open('data.json', 'r+', encoding='utf-8')
    json_file = json.load(f)
    json_data = json.dumps(json_file, indent=4, ensure_ascii=False)
    return json_data

@app.route("/tmpl")
def tmpl_out():
    return_message = "Send fetch"
    # return return_message
    return render_template('tmpl.html',text = return_message)