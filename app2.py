from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/users'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

@app.route('/people')
def show_people():
    sort_key = request.args.get('sort')
    if sort_key not in ['name', 'surname', 'city', 'year']:
        sort_key = 'name'

    #people = Person.query.all()
    people = Person.query.order_by(getattr(Person, sort_key)).all()
    return render_template('people.html', people=people)

if __name__ == '__main__':
    app.run(debug=True)