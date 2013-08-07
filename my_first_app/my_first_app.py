# This is whre you can start you python file for your week1 web app
# Name: Aarthi Narayan

#from flask import Flask
import flask, flask.views
import os
#Create flask application object
app = flask.Flask(__name__)

# Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return self.get()


app.add_url_rule('/',view_func=View.as_view('main'), methods=['GET','POST'])

app.debug = True
app.run()