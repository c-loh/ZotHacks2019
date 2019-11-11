from flask import Flask, jsonify
from flask_restful import Api
import a_1

app = Flask(__name__)
api = Api(app)

#api.add_resource(Hello, '/hello/<string:id>/')

#api.add_resource(Hello, '/hello/')

if __name__ == '__main__':
    app.run(port=5000, debug=True, use_reloader=True)