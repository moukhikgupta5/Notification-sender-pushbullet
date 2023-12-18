from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import firebase_admin
from pushbullet import PushBullet

cred_obj = firebase_admin.credentials.Certificate('firebase.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://seizure-detection-1f412-default-rtdb.firebaseio.com/'
})

from firebase_admin import db

ref = db.reference("/")

# initialize our Flask application

app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST", "GET"])
@cross_origin()
def sendData():
    seizure_time = ''
    seizure_date = ''
    seizure_loc = ''
    user_token = ''
    if request.method == 'POST':
        # Handle POST request data
        data = request.json  # assuming data is sent as JSON in the request body
        seizure_time = data.get('time')
        seizure_date = data.get('date')
        seizure_loc = data.get('location')
        user_token = data.get('usrToken')
    elif request.method == 'GET':
        # Handle GET request data
        seizure_time = request.args.get('time')
        seizure_date = request.args.get('date')
        seizure_loc = request.args.get('location')
        user_token = request.args.get('usrToken')
    print(seizure_time)
    
    formatted_token = user_token.replace(".", "(*)")
    while("." in formatted_token):
        formatted_token = formatted_token.replace(".", "(*)")

    val = {
            "time": seizure_time,
            "date": seizure_date,
            "location": seizure_loc,
            "token": user_token,
        }
    ref = db.reference("/" + str(formatted_token))
    ref.push().set(val)
    

    pb = PushBullet(user_token)
    push = pb.push_note("Alert", "A seizure has occured! Time: " + str(seizure_time) + " | Location: " + str(seizure_loc))
    return jsonify(0)
    


#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True, port=6486)