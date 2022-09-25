from flask_restx import Resource, Namespace
from flask import jsonify
import urllib.request
import json
from datetime import datetime

api = Namespace('deno-app', 'Heroku Consulting Deno App')


@api.route('/')
class getUsers(Resource):
    def get(self):
        url = "https://simple-deno.herokuapp.com/"
        print(url)
        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())

            return jsonify(data)
        except Exception as e:
            return {
                'Error': str(e)
            }, 500


@api.route('/<id>')
@api.doc(params={'id': {'description': 'User ID'}})
class getUser(Resource):
    def get(self, id):
        url = "https://simple-deno.herokuapp.com/" + str(id)
        print(url)
        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())

            return  jsonify(data)
        except Exception as e:
            return {
                'Error': str(e)
            }, 500

@api.route('/<name>,<email>')
@api.doc(params={'web': {'description': 'User web link'}})
class postUser(Resource):
    def post(self,name,email,web):
        if web is None:
            web = ""
        url = f"https://simple-deno.herokuapp.com/"
        print(url)
        try:
            # put = urllib.request.Request(url, method='POST')
            # response = urllib.request.urlopen(put)
            # data = json.loads(response.read())

            return  jsonify({})
        except Exception as e:
            return {
                'Error': str(e)
            }, 500

@api.route('/<id>')
@api.doc(params={'id': {'description': 'User ID'}})
class updateUser(Resource):
    def put(self,id):
        url = "https://simple-deno.herokuapp.com/" + str(id)
        print(url)
        try:
            data = {}
            # put = urllib.request.Request(url,method='PUT')
            # response = urllib.request.urlopen(put)
            # data = json.loads(response.read())

            return  jsonify(data)
        except Exception as e:
            return {
                'Error': str(e)
            }, 500

@api.route('/<id>')
class deleteUser(Resource):
    def delete(self,id):
        url = "https://simple-deno.herokuapp.com/" + str(id)
        print(url)
        try:
            # delete = urllib.request.Request(url, method='DELETE')
            # response = urllib.request.urlopen(delete)
            # data = json.loads(response.read())

            return  jsonify({})
        except Exception as e:
            return {
                'Error': str(e)
            }, 500