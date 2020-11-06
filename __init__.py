from flask import Flask, render_template, request
from model import *

app = Flask(__name__)

communes = get_commune()


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', communes=communes)


@app.route("/data", methods=['GET', 'POST'])
def table():
    if request.form.get('commune') != '-':
        output = get_show_data(request.form.get('commune'))[0]
    elif request.args.get('phone') != '':
        output = get_show_data_cp(request.form.get('phone'))[0]

    json_data = {'Commune': output[3],
                 'Score_global': output[5],
                 'access_interface': output[6],
                 'access_linformation': output[7], 'competance_admin': output[8],
                 'competance_numerique': output[9], 'department': output[12],
                 'dep_score_global': output[13], 'dep_access_interface': output[14],
                 'dep_access_linformation': output[15], 'dep_competance_admin': output[16],
                 'dep_competance_numerique': output[17], 'nom_de_la_region': output[20],
                 'reg_score_global': output[21], 'reg_access_interface': output[22],
                 'reg_access_linformation': output[23], 'reg_competance_admin': output[24],
                 'reg_competance_numerique': output[25]}
    return render_template('data_display.html', result=json_data, communes=communes)


if __name__ == '__main__':
    app.run(port=5252)
