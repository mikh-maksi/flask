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
import time
from datetime import datetime


# db = create_engine('postgresql+psycopg2://jjjvxftvljouqa:a41a7e3069600c2daa7ed7e917e26216fbd28f517719f517c4529b994bb8e430@ec2-34-248-169-69.eu-west-1.compute.amazonaws.com:5432/dfmbp1l6kre1rn')
db = create_engine('postgresql+psycopg2://fuvnjouopjkqjz:457d26bac4530137e6f5fe1cf70d0b89ce4a9659c00fc076186ba123329495db@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/dffjdini6butuh')
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
    return 'Database created'

@app.route("/db_create")
def db_create_all():
    base.metadata.create_all(db)
    return 'Database created'


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

class Actions(base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    user = Column(String(100), nullable=False)
    date_time = Column(DateTime, nullable=False)

class Action1(base):
    __tablename__ = 'action1'
    id = Column(Integer, primary_key=True)
    user = Column(String(100), nullable=False)
    type = Column(Integer, nullable=False)
    date_time = Column(DateTime, nullable=False)

class AnswersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'a1', 'a2', 'a3', 'a4', 'answer_name', 'answer_n', 'date_time')

class ActionsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'date_time')

class Action1Schema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'type','date_time')

answers_schema = AnswersSchema()
actions_schema = ActionsSchema()
action1_schema = Action1Schema()



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/actions",methods=['GET'])
def actions():

    if request.method == "GET":
        if request.args.get('user') == None:
            user = ''
        else:
            user = request.args.get('user')
    # last_time = session.query(Actions).filter_by(user=user).all()
    last_time = session.query(Actions).all()
    data = actions_schema.dump(last_time)
    n = len(last_time)-1
    print(len(last_time))
    out = last_time[0].user
    print(str(out))
    time1 = last_time[0].date_time
    print(str(out))
    out = last_time[n].date_time
    print(str(out))
    print(datetime.fromtimestamp(time.time()))
    print(datetime.fromtimestamp(time.time())-last_time[0].date_time)
    d = datetime.fromtimestamp(time.time())-last_time[0].date_time



    action = Actions( user=user,date_time=datetime.fromtimestamp(time.time()))
    print(action)
    session.add(action)
    session.commit()    
    return d


@app.route("/act",methods=['GET'])
def act():
    if request.method == "GET":
        if request.args.get('user') == None:
            user = ''
        else:
            user = request.args.get('user')

        if request.args.get('type') == None:
            type = ''
        else:
            type = request.args.get('type')
    action = Actions( user=user,type = type, date_time=datetime.fromtimestamp(time.time()))
    print(action)
    session.add(action)
    session.commit()    
    return "<p>User</p>"



@app.route("/send_question",methods=['GET'])
def send_question():
    if request.method == "GET":
        if request.args.get('title') == None:
            title = ''
        else:
            title = request.args.get('title')

        if request.args.get('a1') == None:
            a1 = ''
        else:
            a1 = request.args.get('a1')

        if request.args.get('a2') == None:
            a2 = ''
        else:
            a2 = request.args.get('a2')

        if request.args.get('a3') == None:
            a3 = ''
        else:
            a3 = request.args.get('a3')

        if request.args.get('a4') == None:
            a4 = ''
        else:
            a4 = request.args.get('a4')
        if request.args.get('answer_name') == None:
            answer_name = ''
        else:
            answer_name = request.args.get('answer_name')

        if request.args.get('answer_n') == None:
            answer_n = ''
        else:
            answer_n = request.args.get('answer_n')

        if request.args.get('date_time') == None:
            date_time = '2022-01-01'
        else:
            date_time = request.args.get('date_time')

    answer = Answers( title=title , a1=a1,
                a2=a2, a3=a3, a4=a4,answer_name=answer_name, answer_n=answer_n, date_time=date_time)
    print(answer)
    session.add(answer)
    session.commit()


    test = session.query(Answers).filter_by(title=title).first()
    print(test)
    data = answers_schema.dump(test)
    print(data)

    return jsonify(data=data, message=f'Answer {answer.id} successful registered'), 202

# https://flask-start-app.herokuapp.com/send_question?title=title&a1=a1&a2=a2&a3=a3&a4=a4&answer_name=answer_name&answer_n=answer_n&date_time=2022-11-07

@app.route("/get_question/<int:id>")
def get_answer_test(id: int):
    session.commit()
    test = session.query(Answers).filter_by(id=id).first()
    print(test)
    data = answers_schema.dump(test)
    print(data)

    return jsonify(data=data), 202

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