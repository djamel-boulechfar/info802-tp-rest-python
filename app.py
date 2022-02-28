from flask import Flask, request
from flask_restful import Resource, Api

import os

app = Flask(__name__)
api = Api(app)

port = int(os.environ.get('PORT', 5000))


class CalculeTempsParcours(Resource):
    def get(self, distance, autonomie, temps_chargement, vitesse_moyenne):
        if distance < autonomie:
            nb_recharges_requises = 0
        else:
            nb_recharges_requises = distance // autonomie;
        resultat = distance / vitesse_moyenne * 60 + nb_recharges_requises * temps_chargement
        return {'tempsParcours': resultat}


class CalculeTempsParcoursAvecMaps(Resource):
    def get(self, distance, autonomie, temps_chargement, duree_trajet):
        if distance < autonomie:
            nb_recharges_requises = 0
        else:
            nb_recharges_requises = distance // autonomie
        resultat = duree_trajet + nb_recharges_requises * temps_chargement * 60
        return {'tempsParcours': resultat,
                'tempsChargement': temps_chargement,
                'nbRecharges': nb_recharges_requises}

api.add_resource(CalculeTempsParcours, '/calculeTempsParcours/<int:distance>/<int:autonomie>/<int:temps_chargement>/<int:vitesse_moyenne>')
api.add_resource(CalculeTempsParcoursAvecMaps, '/calculeTempsParcoursAvecMaps/<int:distance>/<int:autonomie>/<int:temps_chargement>/<int:duree_trajet>')

if __name__ == '__main__':
    # Local test
    # app.run(host='localhost', port=port)
    # Heroku
    app.run(host='0.0.0.0', port=port)
