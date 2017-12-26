from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Sensor not found'}, 404
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A sensor with name '{}' already exists.".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the sensor.'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Sensor deleted'}
        return {'message': 'Sensor not found'}, 404
class StoreList(Resource):
    def get(self):
        return {'sensors': [store.json() for store in StoreModel.query.all()]}
