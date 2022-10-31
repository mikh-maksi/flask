from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


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