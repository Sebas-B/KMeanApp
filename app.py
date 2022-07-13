from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL

app= Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='horóscopos'
mysql.init_app(app)

@app.route('/')
def index():

    sql="SELECT * FROM `respuestas`;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)

    respuestas=cursor.fetchall()
    print(respuestas)
    
    conn.commit()
    return render_template('respuestas/index.html', respuestas=respuestas )

@app.route('/destroy/<int:id>')
def destroy(id):
    conn= mysql.connect()
    cursor=conn.cursor()
    
    cursor.execute("DELETE FROM respuestas WHERE id_respuesta=%s",(id))
    conn.commit()
    return redirect('/')

@app.route('/create')
def create():

    return render_template('respuestas/create.html')

@app.route('/store', methods=['POST'])
def storage():

    _optimista=request.form['optimistaR']
    _pesimista=request.form['pesimistaR']
    _confianza=request.form['confianzaR']
    _atencion=request.form['atencionR']
    _afecto=request.form['afectoR']
    _extrovertida=request.form['extrovertidaR']
    _introvertida=request.form['introvertidaR']
    _inteligente=request.form['inteligenteR']
    _deprime=request.form['deprimeR']
    _fiesta=request.form['fiestaR']
    _fisico=request.form['fisicoR']
    _ejercicio=request.form['ejercicioR']
    _solitaria=request.form['solitariaR']
    _viajar=request.form['viajarR']
    _estacion=request.form['estacionR']
    _emprendedor=request.form['emprendedorR']
    _elemento=request.form['elementoR']
    
    sql="INSERT INTO `respuestas` (`id_respuesta`, `optimistaR`, `pesimistaR`, `confianzaR`, `atencionR`, `afectoR`, `extrovertidaR`, `introvertidaR`, `inteligenteR`, `deprimeR`, `fiestaR`, `fisicoR`, `ejercicioR`, `solitariaR`, `viajarR`, `estacionR`, `emprendedorR`, `elementoR`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    
    datos=(int(_optimista),int(_pesimista),int(_confianza),int(_atencion),int(_afecto),int(_extrovertida),int(_introvertida),int(_inteligente),int(_deprime),int(_fiesta),int(_fisico),int(_ejercicio),int(_solitaria),int(_viajar),int(_estacion),int(_emprendedor),int(_elemento))

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('respuestas/predict.html')

if __name__== '__main__':
    app.run(debug=True)