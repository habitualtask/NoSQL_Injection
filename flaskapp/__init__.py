from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/',methods=['GET'])
def test():
    return render_template('form.html')

@app.route('/login'.methods=['GET'])
def mongoTest():
    client=MongoClient('mongodb://localhost:27017/')
    db = client.nodejs
    collection = db.user
    idtext = request.args.get('idtext')
    pwtext = request.args.get('pwtext')
    results = collection.find({"id":idtext,"pw":pwtext})
    client.close()
    num=0
    print('%s'%pwtext)
    if results is not None:
        for i in results:
            num=+1
    if num==0:
        return 'nonedata'
    else:
        return 'hello %s'%idtext
if __name__=="__main__":
    app.run('0.0.0.0',port=80)