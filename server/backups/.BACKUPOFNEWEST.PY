import sched, time
from flask import Flask, jsonify, abort, request, make_response, url_for
from twilio.rest import Client

#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('yourserver.key')
#context.use_certificate_file('yourserver.crt')


app = Flask(__name__)

account_sid = "AC5791a2d86be0252e5b6e8694ef387ee6"
auth_token = "357b1976cfd256b37ca43313aabe5c8f"

#app = Flask(__name__)
scheduler = sched.scheduler(time.time, time.sleep)

client = Client(account_sid,auth_token)

my_num = "+15149699306"
twilio_num = "+15796000924"


#@app.route('/api/inputUserData', methods=['OPTIONS'])
#def yourMethod():
#    response = jsonify({'some': 'data'})
#    response.headers.add('Access-Control-Allow-Origin', '*')
#    return response


@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/api/inputUserData', methods=["POST"])
def addUserData():
	if not request.json or not 'text' in request.json:
		abort(400)
	input = {
		'time': request.json['time'],
		'text': request.json['text']
	}
	print("Received text:\t", input['text'])
	#testFunction()
	response = jsonify({'text': input['text']})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 21

#@app.route('/api/inputUserData', methods=['OPTIONS'])
#def option_response():
#	print("RECEIVED")
#	return Response(headers={'Access-Control-Allow-Origin': '*'}, status=200)
#
#def updateCount(text):
#	textGroup = classifyText(text)
#	if textGroup < 0.5:
#		#increase count by one
#		pass
#	else:
#		#decrease count by one
#		pass
#	checkOnUser("josh")
#	return -1
#
#def classifyText(text):
#	pass
#	 
#def checkOnUser(user):
#	if user["count"] > arbitraryNumber:
#		textUser(user)
#
#def textUser(user):
#	client.messages.create(
#    		to = my_num,
#    		from_ = twilio_num,
#    		body = "Test"
#	)

if __name__ == '__main__':
	app.run( host='0.0.0.0', port=80)
	# get user count
	
