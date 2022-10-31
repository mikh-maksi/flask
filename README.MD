# Flask
## Simple Start
Для того, щоб використовувати фреймворк Flask його необхідно встановити як бібліотеку. Для цього в консолі <a href = "https://git-scm.com/downloads">Git Bash</a>
```
pip install Flask
```

Для простого запуску сервісу на Flask напишемо наступну програму.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
Далі - відкриємо командну строку у відповідній папці та виконаємо команду:
```
flask run
```
<img src = "img/flask01.jpg">   

Далі - відкриємо браузер за посиланням: <a href = "http://127.0.0.1:5000/" target = "_blank">http://127.0.0.1:5000/</a>  
<img src = "img/flask02.jpg">   

## Підготовка до завантаження на Heroku
Додати файл requirements.txt
```python
amqp==5.1.1
APScheduler==3.9.1
billiard==3.6.4.0
cachetools==5.2.0
celery==5.2.7
certifi==2022.9.14
charset-normalizer==2.1.1
click==8.1.3
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.2.0
colorama==0.4.5
Flask==2.1.3
Flask-APScheduler==1.12.4
Flask-Cors==3.0.10
flask-marshmallow==0.14.0
Flask-SQLAlchemy==2.5.1
google-api-core==2.10.1
google-api-python-client==2.61.0
google-auth==2.11.1
google-auth-httplib2==0.1.0
googleapis-common-protos==1.56.4
greenlet==1.1.2
gunicorn==20.1.0
httplib2==0.20.4
idna==3.4
importlib-metadata==4.12.0
itsdangerous==2.1.2
Jinja2==3.1.2
kombu==5.2.4
MarkupSafe==2.1.1
marshmallow==3.17.0
marshmallow-sqlalchemy==0.28.0
oauth2client==4.1.3
packaging==21.3
prompt-toolkit==3.0.31
protobuf==4.21.6
psycopg2==2.9.3
pyasn1==0.4.8
pyasn1-modules==0.2.8
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2022.2.1
pytz-deprecation-shim==0.1.0.post0
requests==2.28.1
rsa==4.9
schedule==1.1.0
six==1.16.0
SQLAlchemy==1.4.39
tzdata==2022.2
tzlocal==4.2
uritemplate==4.1.1
urllib3==1.26.12
vine==5.0.0
wcwidth==0.2.5
Werkzeug==2.1.2
zipp==3.8.1
```

Та файл Procfile
```
web: gunicorn app:app
```
## Підготовка до завантаження на Heroku
Реєструємося на сервісі Heroku 
<img src = "img/flask03.jpg">   
<img src = "img/flask04.jpg">   
<img src = "img/flask05.jpg">   
<img src = "img/flask06.jpg">   
<img src = "img/flask07.jpg">   
<img src = "img/flask08.jpg">   
<img src = "img/flask09.jpg">   
<img src = "img/flask10.jpg">   
<img src = "img/flask11.jpg">   

## Створення додатку на Heroku
<img src = "img/flask12.jpg">   
<img src = "img/flask13.jpg">   
<img src = "img/flask14.jpg">   
<img src = "img/flask15.jpg">   
<img src = "img/flask17.jpg">   
<img src = "img/flask18.jpg">   

## Підключаємо репозиторій на GitHub
<img src = "img/flask20.jpg">   
<img src = "img/flask21.jpg">   
<img src = "img/flask22.jpg">   
<img src = "img/flask23.jpg">   
<img src = "img/flask24.jpg">   
<img src = "img/flask25.jpg">   
<img src = "img/flask26.jpg">   

## Запускаємо деплой із репозитарію
Для того, щоб деплой було виконано успішно, та додаток запустився необхідно обов'язково додати файли requirements.txt та Procfile із вмістом, який описаной вище.
<img src = "img/flask27.jpg">   
<img src = "img/flask30.jpg">   

## Продивитись логи
Для того, щоб контролювати виконання додатку (в тому числі бачити вивід в консоль) на Horoku можна дивитись логі.
<img src = "img/flask28.jpg">   
<img src = "img/flask29.jpg">   

# Заняття 2. Збереження даних
Для початку - використаємо для збереження даних файл в форматі JSON.  
Для цього додамо у вихідний код Flask наступний код:  

```python
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
```
А також створити в коренневій папці файл `data.json`:
```
[
    {
        "id": 0,
        "name": "noname",
        "description": "no description"
    }
]
```
