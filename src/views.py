from flask import jsonify
from src import app, User

@app.route("/")
def home():
    return jsonify({
        "message": "Hi Carrington, my name is Wonderful"
    })

@app.route("/about")
def about():
    return jsonify({
        "message": "About Us"
    })


@app.route('/users', methods=['GET'])
def get_users():
    """
    Get Users API
    ---
    get:
      description: Returns a list of users
      responses:
        200:
          description: A successful response
          schema:
            type: object
            properties:
              message:
                type: list
                example: []
    """
    users = User.query.all()

    return jsonify(users)  # Dataclass automatically converts to JSON

@app.route('/api/greet', methods=['GET'])
def greet():
    """
    Greet API
    ---
    get:
      description: Returns a greeting message
      responses:
        200:
          description: A successful response
          schema:
            type: object
            properties:
              message:
                type: string
                example: "Hello, world!"
    """
    return jsonify({"message": "Hello, world!"})