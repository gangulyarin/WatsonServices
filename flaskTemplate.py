import flask
from flask import request, Flask, render_template
from toneAnalyzer import sendTone
import json

app = flask.Flask(__name__, static_url_path='')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def root():
    num = request.args.get("val")
    #return f"<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p><p>Value given is {num}</p>"
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    #processed_text = text.upper()
    toneResponse = json.loads(sendTone(text))
    print(type(toneResponse))
    #tone = toneResponse[0].document_tone.tones[0]
    #return processed_text
    return render_template("index.html",jsonobj=toneResponse['document_tone']['tones'])

#app.run()
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
