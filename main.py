import graphene
import json
from flask import Flask, request
from graphene import ObjectType, String, Schema

app = Flask(__name__)

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"), age=String(default_value='0'))
    goodbye = String()

    def resolve_hello(root, info, name, age):
        return f'Hello {name}!'
        # return 'Hello {} you are {} years old'.format(args['name'], args['age'])

    def resolve_goodbye(root, info):
        return 'See ya!'


schema = Schema(query=Query)

@app.route("/graphql", methods=['POST'])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)
