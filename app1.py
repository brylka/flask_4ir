from flask import Flask, render_template

app = Flask(__name__)

people = [
    {'name': 'Jan', 'surname': 'Kowalski', 'city': 'Warszawa', 'year': 1990},
    {'name': 'Anna', 'surname': 'Nowak', 'city': 'Kraków', 'year': 1985},
    {'name': 'Piotr', 'surname': 'Zalewski', 'city': 'Gdańsk', 'year': 1988},
    {'name': 'Katarzyna', 'surname': 'Wójcik', 'city': 'Wrocław', 'year': 1992},
    {'name': 'Michała', 'surname': 'Kubiak', 'city': 'Poznań', 'year': 1991},
]

@app.route('/people')
def show_people():
    return render_template('people.html', people=people)

if __name__ == '__main__':
    app.run(debug=True)