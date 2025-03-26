from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_age():
    age = None
    if request.method == 'POST':
        birth_year = request.form.get('birth_year')
        if birth_year and birth_year.isdigit():
            current_year = datetime.now().year
            age = current_year - int(birth_year)
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(debug=True)
