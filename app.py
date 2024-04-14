import csv
from flask import Flask, request, jsonify , render_template , url_for , flash ,redirect 
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm 
from flask_migrate import Migrate
import json 

app = Flask(__name__)

app.config['SECRET_KEY'] = '1987daa57f984128fe36ab84a540e4b1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mitigation.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

'''
class Mitigation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    techniqueid = db.Column(db.String(20), unique=True, nullable=False)
    technique = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    mitigationid = db.Column(db.String(20), unique=False, nullable=False)
    mitigation = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return f"Mitigation('{self.id}', '{self.techniqueid}', '{self.technique}', '{self.description}', '{self.mitigationid}', '{self.mitigation}')" 
'''       
'''
with app.app_context():
    db.create_all()
    # Any other database setup or operations 
'''
    
'''
def import_csv_to_db():
    with open('C:/Users/ninja/Desktop/mitigation.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            mitigation_entry = Mitigation(techniqueid=row[0], technique=row[1], description=row[2], mitigationid=row[3], mitigation=row[4])
            db.session.add(mitigation_entry)
        db.session.commit() 
'''

# Example usage
# import_csv_to_db('path_to_your_csv_file.csv')



'''@app.route('/import-csv')
def import_csv_route():
    import_data('C:/Users/ninja/Desktop/mitigation.csv')
    return 'CSV data imported successfully'
   ''' 

posts = [
    {
        'author': 'Blake Strom',
        'title': 'Getting Started with ATT&CK: Adversary Emulation and Red Teaming',
        'content': 'https://medium.com/mitre-attack/getting-started-with-attack-red-29f074ccf7e3',
        'date_posted': 'Published in MITRE ATT&CK® . 10 min read . Jul 18, 2019'
    }
]


@app.route('/show-data')
def show_data():
    # Replace 'your_json_file.json' with the path to your JSON file
    with open('mitigation.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)


@app.route("/")
def home():
    
    return render_template('home.html', posts= posts)


@app.route("/mitretool")
def mitigaion_result():
    return render_template('checker.html')


@app.route("/introduction")
def mitre_introduction():
    return render_template('introduction.html')

@app.route("/gpt")
def gptpage():
    return render_template('gpt.html',)

@app.route("/register" , methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register',form = form)

@app.route("/login" , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'bin@gmail.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/get_mitigation_data')
def get_mitigation_data():
    with open('mitigation.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
    