from flask import Flask, render_template, request, session, url_for, redirect, g
import aircraft_scrapdata

app = Flask(__name__)

app.secret_key = 'dYIbV9GL3VtVyGWq2tpjndfuig6d3278gbz6T80WjuY'

@app.route('/question', methods = ['GET', 'POST'])
def question():

    manufacturer_list = ['Embraer', 'Antonov', "ATR", 'Bombardier', 'Cessna', 'Fokker', 'Tupolev', 'Ilyushin', 'Boeing', 'Airbus']

    aircraft_dict = {
        'Embraer': ['170', '175', '190', '195', '145', '120'],
        'Antonov': ['AN-124', 'AN-225'],
        'ATR': ['ATR-42', 'ATR-72', '72', '42'],
        'Bombardier': ['Q400', 'CRJ-200', 'CRJ-900', 'CRJ-700' 'Global'],
        'Cessna': ['152', '172', '182', 'Citation'],
        'Fokker': ['50', '70', '100'],
        'Tupolev': ['134'],
        'Ilyushin': ['62'],
        'Boeing': ['727', '737', '747', '757', '767', '777', '787'],
        'Airbus': ['A300', 'A310', 'A318', 'A319', 'A320', 'A321', 'A330', 'A340', 'A350', 'A360']
        # 'McDonnell Douglas': ['1'],
        # 'General Dynamics': ['1'],
        # 'Lockheed Martin': ['1'],
        # 'British Aerospace': ['1'],
    }

    aircraft, imagelink = aircraft_scrapdata.findplane(aircraft_dict)
    manufacturer = aircraft[0]
    model = aircraft[1]
    print(manufacturer)
    if request.method == "POST":
        manu = request.form['123']
        print(f'{manu}')
        return render_template('question.jinja2', manufacturer_list = manufacturer_list, manufacturer = manufacturer)
    return render_template('question.jinja2', manufacturer_list = manufacturer_list, manufacturer = manufacturer)

if __name__ == '__main__':
    app.run(debug=True)