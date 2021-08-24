from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
import joblib
import traceback
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pacientes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    ejection_fraction = db.Column(db.Integer)
    serum_creatinine = db.Column(db.Float)
    time = db.Column(db.Integer)
    death_event = db.Column(db.Integer)

    def __init__(self, age, ejection_fraction, serum_creatinine, time, death_event):
        self.age = age
        self.ejection_fraction = ejection_fraction
        self.serum_creatinine = serum_creatinine
        self.time = time
        self.death_event = death_event

class SchemaPaciente(ma.Schema):
    class Meta:
        fields = ('id', 'age', 'ejection_fraction', 'serum_creatinine', 'time', 'death_event')

paciente_schema = SchemaPaciente()
pacientes_schema = SchemaPaciente(many=True)

class UserManager(Resource):
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            pacientes = Paciente.query.all()
            return jsonify(pacientes_schema.dump(pacientes))

        paciente = Paciente.query.get(id)
        return jsonify(paciente_schema.dump(paciente))

    @staticmethod
    def post():
        if svc:
            try:
                json_ = request.json
                dataframe = pd.DataFrame(json_)
                previsao = list(svc.predict(dataframe))

                resultado = []
                for i in previsao:
                    if i == 0:
                        resultado.append('Sobreviveu')
                    elif i == 1:
                        resultado.append('Morreu')

                for i in range(len(previsao)):
                    age = dataframe.iloc[i]['age']
                    ejection_fraction = dataframe.iloc[i]['ejection_fraction']
                    serum_creatinine = dataframe.iloc[i]['serum_creatinine']
                    time = dataframe.iloc[i]['time']
                    death_event = int(previsao[i])

                    paciente = Paciente(age, ejection_fraction, serum_creatinine, time, death_event)
                    db.session.add(paciente)

                db.session.commit()

                return jsonify({'Previsao': str(resultado)})

            except:
                return jsonify({'Trace': traceback.format_exc()})

        else:
            return('Não existe nenhum modelo para usar.')

api.add_resource(UserManager, '/api')

if __name__ == '__main__':
    svc = joblib.load('ModeloSVC.pkl')
    app.run(debug=True)


