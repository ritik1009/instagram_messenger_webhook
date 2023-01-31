# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/instagram_webhook')
# ‘/’ URL is bound with hello_world() function.
def instgaram_webhook():
	print("hello",request)
	if request.method == 'POST':
		j = 0
		print("received data: ", request.json)
		resp = request.json
		try:
			msg = resp['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
			number = resp['entry'][0]['changes'][0]['value']['messages'][0]['from']
			print("\n number",number)
			j = 1
			print("\n message",msg)
		except:
			pass
		if j ==1 :
			print("hello in the if loop")
			#send_message(number=number,response = msg,message_type = 'text')
		return 'success', 200
	elif request.method == 'GET':
		print("\n ttttttt")
		try:
			challenge = request.args.get('hub.challenge')
			return challenge
		except:
			print("this is the ends")
			return 200
	else:
		return '',200


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	# app.run(ssl_context=('certificate.pem', 'key.pem'), host='0.0.0.0', port=80)
	app.run()