'''
@module: API framework
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/docker-flash-api
@license: MIT License
@copyright: 2020 Leonardo Mauro
@access: public
'''

#-- Imports
import flask
import api
from flask import request, jsonify

#-- API predefinitions
app = flask.Flask('docker-flash-api')
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
appPort = 5050
api.init()


#-- Home page
@app.route('/', methods=['GET'])
def home():
    return "<h2>Docker - Flask API Framework</h2>\
    <p>This API is running - <a href=\"http://{0}/api/\">http://{0}/api/</a>.</p>".format(request.host)


#-- API url
@app.route('/api/', methods=['GET'])
def apiRun():
    response = api.run(request.args)
    return jsonify(response)


#-- Publishing app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=appPort)