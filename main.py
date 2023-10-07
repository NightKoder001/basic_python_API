from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

#GET method
@app.route("/get_user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Nightkoder",
        "email": "gautamj.iitm@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data, 200)

#POST method
@app.route("/create_user", methods = ["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug = "True")

