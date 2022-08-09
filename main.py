from flask import Flask, jsonify, request, make_response, abort

from database import db
from models.animes import ANIMES, ANIMESEncoder

app = Flask(__name__)
app.config['DEBUG']=True
app.json_encoder = ANIMESEncoder

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Status': 404, 'Error': 'Resourcer not found'}), 404)


@app.route('/animes', methods=['GET'])
def lists():
    return jsonify({'animes': db})

@app.route('/animes/<int:id>', methods=['GET'])
def list(id):
    for anime in db:
        if id == anime.id:
            return jsonify(anime)
    abort(404)
    
    
@app.route('/animes', methods=['POST'])
def create():
    if not request.json or not 'Name' in request.json:
        abort(404)
    anime = ANIMES(
        request.json['Name'],
        request.json['Autor'],
        request.json['Description']
    )
    db.append(anime)
    return jsonify(anime), 201


@app.route('/animes/<int:id>', methods=['PUT'])
def update(id):
    if not request.json:
        abort(404)
    for anime in db:
        if anime.id == id:
            anime.Name = request.json['Name'],
            anime.Autor = request.json['Autor'],
            anime.Description = request.json['Description']
            return jsonify({'Atualizado com sucesso.': True})
    abort(404)
    
@app.route('/animes/<int:id>', methods=['Delete'])  
def delete(id):
    for anime in db:
        if anime.id == id:
            db.remove(anime)
            return jsonify({'Excluído com sucesso.': True})
    abort(404)
    
app.run()