from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS
import healthyPetsTableClient


app = Flask(__name__)
CORS(app)

@app.route("/")
def healthCheckResponse():
    return jsonify({"message" : "Nothing here, used for health check. Try /mypets instead."})
    
@app.route("/mypets")
def getMyPets():

    serviceResponse = healthyPetsTableClient.getAllMyPets()

    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

# Run the service on the local server it has been deployed to,
# listening on port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
