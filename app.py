import pickle
from scipy.spatial import distance
from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
import numpy as np

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'zodiacales'
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
            dist = distance.euclidean(*vals, this_segment)
            l.append(dist)
            index_min = np.argmin(l)
            assigned_clusters.append(index_min)

        return render_template(
            'predict.html', result_value=f'Segmento Calculado = # {index_min}'
        )

if __name__ == '__main__':
    app.run(debug=True)
