# import
from flask import Flask, render_template, request

# initilaise the app
app = Flask(__name__) 

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/forms')
def contact():
    return render_template('forms.html')

@app.route('/predict', methods=['post'])
def predict():
    number = request.form.get('phone')
    mail = request.form.get('email')
    name = request.form.get('name')

    print(number)
    print(mail)
    print(name)

    return 'Form submitted Thankyou'
# running the app
app.run(debug = True)