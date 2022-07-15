import pickle
from scipy.spatial import distance
from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
import numpy as np

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'sql538.main-hosting.eu'
app.config['MYSQL_DATABASE_USER'] = 'u544016274_Sebas'
app.config['MYSQL_DATABASE_PASSWORD'] = '_YHHq5xrmXV_q86KS#'
app.config['MYSQL_DATABASE_DB'] = 'u544016274_Zodiacales'
mysql.init_app(app)


@app.route('/')
def index():
    sql = "SELECT * FROM `respuestas`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)

    respuestas = cursor.fetchall()
    print(respuestas)

    conn.commit()
    return render_template('respuestas/index.html', respuestas=respuestas)


@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM respuestas WHERE id_respuesta=%s", (id))
    conn.commit()
    return redirect('/')


@app.route('/create')
def create():
    return render_template('respuestas/create.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return 'La url /predict esta siendo accesada directamentamente. Por favor dirigete a la pagina principal'

    if request.method == 'POST':
        _optimista = request.form['optimistaR']
        _pesimista = request.form['pesimistaR']
        _confianza = request.form['confianzaR']
        _atencion = request.form['atencionR']
        _afecto = request.form['afectoR']
        _extrovertida = request.form['extrovertidaR']
        _introvertida = request.form['introvertidaR']
        _inteligente = request.form['inteligenteR']
        _deprime = request.form['deprimeR']
        _fiesta = request.form['fiestaR']
        _fisico = request.form['fisicoR']
        _ejercicio = request.form['ejercicioR']
        _solitaria = request.form['solitariaR']
        _viajar = request.form['viajarR']
        _estacion = request.form['estacionR']
        _emprendedor = request.form['emprendedorR']
        _elemento = request.form['elementoR']

        sql = "INSERT INTO `respuestas` (`id_respuesta`, `optimistaR`, `pesimistaR`, `confianzaR`, `atencionR`, `afectoR`, `extrovertidaR`, `introvertidaR`, `inteligenteR`, `deprimeR`, `fiestaR`, `fisicoR`, `ejercicioR`, `solitariaR`, `viajarR`, `estacionR`, `emprendedorR`, `elementoR`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        datos = (int(_optimista), int(_pesimista), int(_confianza), int(_atencion), int(_afecto), int(_extrovertida), int(_introvertida), int(_inteligente), int(_deprime), int(_fiesta), int(_fisico), int(_ejercicio), int(_solitaria), int(_viajar), int(_estacion), int(_emprendedor), int(_elemento))

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        
        input_val = request.form

        input_val

        if input_val != None:
            # collecting values
            vals = []
            for key, value in input_val.items():
                vals.append(float(value))

        # Calculate Euclidean distances to freezed centroids
        with open('freezed_centroids.pkl', 'rb') as file:
            freezed_centroids = pickle.load(file)

        assigned_clusters = []
        l = []  # Lista de distancias

        for i, this_segment in enumerate(freezed_centroids):
            #dist = distance.euclidean(*vals, this_segment)
            d=np.array([*vals, this_segment])
            l.append(d)
            index_min = np.argmin(l)
            assigned_clusters.append(index_min)

        if index_min == 3:
            return render_template(
            './respuestas/predict.html', result_value3='Felicitaciones amigx pertences al grupo = A')
        elif index_min == 2:
            return render_template(
            './respuestas/predict.html', result_value2='Felicitaciones amigx pertences al grupo = B')
        elif index_min == 1 :
            return render_template(
            './respuestas/predict.html', result_value1='Felicitaciones amigx pertences al grupo = C')
        elif index_min == 0:
            return render_template(
            './respuestas/predict.html', result_value0='Felicitaciones amigx pertences al grupo = D')

if __name__ == '__main__':
    app.run(debug=True)