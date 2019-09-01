from flask import render_template, Flask, url_for, request
import random
from models import Number

app  = Flask("Guess")

gen_number = Number(score=random.randrange(1, 100))
stored_number = gen_number.put()
count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
	global gen_number
	global stored_number
	global count
	input_number = request.form.get("number")
	if request.method == 'POST':
		try:
			if int(input_number) > stored_number.get().score:
				reply = "Your input is greater, you entered %s. Try again"%(input_number)
				img = 'sad'
				count += 1
				#print stored_number.get()
				return render_template('index.html', reply=reply, img=img)
			elif int(input_number) < stored_number.get().score:
				reply = "Your input is lesser, you entered %s. Try again"%(input_number)
				img = 'sad'
				count += 1
				#print stored_number.get()
				return render_template('index.html', reply=reply, img=img)
			else:
				if count == 1:
					reply = "You got it in %s try"%(count)
				else:
					reply = "You got it in %s tries"%(count)
				img = 'win'
				gen_number.score = random.randrange(1, 100)
				stored_number = gen_number.put()
				count = 0
				#print count
				return render_template('index.html', reply=reply, img=img)
		except:
			return render_template('index.html', reply="Please enter a number")
	else:
		return render_template('index.html')
