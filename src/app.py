from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/news"

mongo = PyMongo(app)
##Função para adição de notícias
@app.route('/add', methods=['POST'])
def add_news():
    _json = request.json
    _titulo = _json['titulo']
    _noticia = _json['noticia']
    _autor = _json['autor']

    if _noticia and _titulo and _autor and request.method == 'POST':

        id = mongo.db.new.insert({'noticia': _noticia, 'titulo': _titulo, 'autor': _autor})

        resp = jsonify("Noticia adicionada com sucesso")

        resp.status_code = 200

        return resp
    
    else:
        return not_found()



@app.route('/busca', methods=['POST'])
def ler():
    _json = request.json
    busca = _json['busca']
    if busca and request.method == 'POST':
        new = mongo.db.new.find({'titulo' or 'noticia' or 'autor' :busca})

        resp = dumps(new)
        return resp

    else:
        print("Não foi encontrado nada relacionado a sua busca.")

#Função para deletar notícia
@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    mongo.db.new.delete_one({'_id':ObjectId(id)})
    resp = jsonify("Notícia deleta com sucesso")

    resp.status_code = 200

    return resp

#Função para alteral a notícia
@app.route('/update/<id>', methods=['PUT'])
def update_news(id):
    _id = id
    _json = request.json
    _titulo = _json['titulo']
    _noticia = _json['noticia']
    _autor = _json['autor']

    if _noticia and _titulo and _autor and request.method == 'PUT':
        mongo.db.new.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'titulo': _titulo, 'noticia': _noticia, 'autor': _autor}})

        resp = jsonify("Noticia alterada com sucesso")

        resp.status_code = 200

        return resp 

    
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(debug=True)

