from datetime import datetime
from flask import request
from flask_restful import Resource


class Home(Resource):
    def get(self):
        q = request.args.get('q')
        dt = datetime.now()
        data = {
            'Query' :   q,
            'Date'  :   dt.strftime('%Y-%m-%d'),
            'Time'  :   dt.strftime('%H:%M')
        }
        return data, 200
