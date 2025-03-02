from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)

swagger = Swagger(app)  # Initialize Flasgger
