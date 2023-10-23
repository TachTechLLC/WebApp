from flask import Flask, request, Response
import os

TOKEN = os.environ["AUTHORIZATION_TOKEN"]

# Init app
app = Flask(__name__)


@app.route('/api/v1/users', methods=["GET"])
def get_users():
    """Get Users
    """
    auth_header = request.headers.get("Authorization")
    if auth_header != f"Bearer {TOKEN}":
        return Response(status=401)
    return Response("[{'name': 'Armen Martirosyan', 'phone':'+19876543210'}]")

# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)