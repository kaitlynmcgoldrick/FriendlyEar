from flask import Flask, jsonify, abort, request, make_response, url_for
from twilio.rest import Client
import sched, time
import importlib
from sklearn.externals import joblib

from tuning_model import scorer

import sched, time 

#Server
app = Flask(__name__)

#Account Tokens for using Twilio
account_sid = "AC5791a2d86be0252e5b6e8694ef387ee6"
auth_token = "357b1976cfd256b37ca43313aabe5c8f"

#Numbers
my_num = "+15148230517"
twilio_num = "+15796000924"

#Twilio SMS Client
client = Client(account_sid, auth_token)

#Scheduler to schedule texts at specific intervals
s = sched.scheduler(time.time, time.sleep)

#Classification Model
model = joblib.load('model.sav')

#User Count
count = 0

@app.route("/", methods=["GET"])
def helloWorld():
	return "Hello World"

@app.route("/api/inputUserData", methods=["POST"])
def doStuff():
	if not request.json or not "text" in request.json:
		abort(400)
	text = {"time": request.json["time"],
		"title": request.json["text"]}
	score = scorer(request.json["text"], model)
	global count
	if score > 0.5:	#Depressed
               #increase count by one
		count += 1
		print(count)
	else:			#Not Depressed
		#decrease count by one
		count -= 1
		print(count)
	return jsonify({"text": text}), 201
@app.route("/api/getCount", methods=["GET"])
def getCount():
	return jsonify({"count" : count}), 201
@app.route("/api/checkOnUser", methods=["GET"])
def checkOnUser():
	global count
	if count >= 3:
		client.messages.create(
			to = my_num,
			from_ = twilio_num,
			body = "Hey, I sense you're not feeling so good. Is everything okay?"
		)
		count = 0		
		print("---> Texted User")
		return jsonify({"texted" : "no"}), 201
	else:
		print("---> Did Not Text User")
		return jsonify({"texted" : "yes"}), 201

if __name__ == '__main__':
	
	app.run(host = '0.0.0.0', port=80)
		
