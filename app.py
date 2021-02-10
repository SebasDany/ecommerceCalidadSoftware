from flask import Flask, session, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql
# from werkzeug import generate_password_hash, check_password_hash
from time import time
import bcrypt
from datetime import date
import numpy as np

tiempo = []
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '7k8v5pkOX8'
app.config['MYSQL_DATABASE_PASSWORD'] = 'iXJJQQUilu'
app.config['MYSQL_DATABASE_DB'] = '7k8v5pkOX8'
app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'
mysql.init_app(app)
cont_chat = 0;
cont_web = 0;
start_time = 0
cont_chat_array = []
cont_web_array = []
tiempo1 = []
nombre = ''
productos_globales=[]

@app.route('/add', methods=['POST'])
def add_product_to_cart():
    start_time = time()
    #print(start_time)

    cursor = None
    try:
        _quantity = int(request.form['quantity'])
        _code = request.form['code']
        # validate the received values
        if _quantity and _code and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM product WHERE code=%s", _code)
            row = cursor.fetchone()

            itemArray = {
                row['code']: {'name': row['name'], 'code': row['code'], 'quantity': _quantity, 'price': row['price'],
                              'image': row['image'], 'total_price': _quantity * row['price']}}

            all_total_price = 0
            all_total_quantity = 0

            session.modified = True
            if 'cart_item' in session:
                if row['code'] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row['code'] == key:
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row['price']
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)

                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                all_total_price = all_total_price + _quantity * row['price']

            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            print(productos_globales.append(session['all_total_price']))
            return redirect(url_for('.products'))
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        elapsed_time = time() - start_time
        tiempo.append(elapsed_time)
        #print(tiempo)


@app.route('/')
def products():
    start_time = time()
    fecha = date.today()
    q_n = "INSERT INTO abandono_pagina (id, c_abandono, fecha) VALUES (NULL, " + str(1) + ",'" + str(fecha) + "');"
    print(q_n)
    try:

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()

        cursor.execute(q_n)
        conn.commit()
        return render_template('products.html', products=rows)
    except Exception as e:
        print(e)
    finally:

        cursor.close()
        conn.close()
        elapsed_time = time() - start_time
        tiempo.append(elapsed_time)
        print(tiempo)


@app.route('/empty')
def empty_cart():
    try:
        session.clear()
        return redirect(url_for('.products'))
    except Exception as e:
        print(e)


@app.route('/delete/<string:code>')
def delete_product(code):
    start_time = time()
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True

        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

        return redirect(url_for('.products'))
        elapsed_time = time() - start_time
        tiempo.append(elapsed_time)
        print(tiempo)
    except Exception as e:
        print(e)


def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array + second_array
    elif isinstance(first_array, dict) and isinstance(second_array, dict):
        return dict(list(first_array.items()) + list(second_array.items()))
        return first_array.union(second_array)
    return False


@app.route('/index', methods=['GET', 'POST'])
def formulario():
    start_time = time()
    tiempo1.append(time())
    for i in range(2000):
        print("Hola ", end="")
    print()
    elapsed_time = time() - start_time
    tiempo.append(elapsed_time)
    print(tiempo)

    return render_template('index.html')


@app.route('/facturacion', methods=['GET', 'POST'])
def facturacion():
    fecha = date.today()
    print(fecha)
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    print(nombre, apellido)
    query1 = "INSERT INTO horario (id_horario, id_materia, id_docente, hora_entrada, hora_salida, dia, grupo, aulab) VALUES (NULL, " + "');"
    print(query1)
    print(start_time)
    print("vchsvdhvdhv")

    elapsed_time = time() - start_time
    print(elapsed_time)
    laSuma = 0
    for i in tiempo:
        laSuma = laSuma + i
    print("el tempo total requerido es ", laSuma)
    q = 'select * from eficiencia order by id desc limit 1'


    #q = "INSERT INTO eficiencia (id, cliente, tiempo_req, trasac_complet,fecha) VALUES (NULL, '" + nombre + "'," + str(round(laSuma, 2)) + ",1,'" + str(fecha) + "');"
    print(q)
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(q)
    eficie = cursor.fetchone()

    qqq= "UPDATE eficiencia set trasac_complet= 1 where id=" + str(eficie['id']) + ";"

    cursor.execute(qqq)
    conn.commit()

    print("2datos ingresados")

    cursor.execute('SELECT * FROM eficiencia where trasac_complet=1')
    data = cursor.fetchall()

    cursor.execute('SELECT * FROM eficiencia where trasac_complet=0')
    data1 = cursor.fetchall()
    print(data1)

    cursor.execute('SELECT AVG(tiempo_req) FROM eficiencia WHERE trasac_complet=1')
    data2 = cursor.fetchall()
    prom = data2[0]
    val = round(prom['AVG(tiempo_req)'], 2)
    print(type(val))
    print(prom['AVG(tiempo_req)'])
    print('SELECT * FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    cursor.execute(
        'SELECT * FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    data3 = cursor.fetchall()

    cursor.execute(
        'SELECT COUNT(*) FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    print(
        'SELECT COUNT(*) FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    num = cursor.fetchall()[0]

    data4 = num['COUNT(*)']

    print(data3)

    cursor.execute('SELECT COUNT(*) FROM abandono_pagina WHERE c_abandono=1')

    num_ap = cursor.fetchall()[0]

    can_aban = num_ap['COUNT(*)']

    dapa = cursor.execute('SELECT * FROM abandono_pagina')
    print(dapa)

    if (len(tiempo1) == 0):
        fintiempo = 0;

    else:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        fintiempo = round(time() - tiempo1[0], 2)
        print("holllllllllllllllll",fintiempo)
        q1 = "INSERT INTO tiempo_pagina (id, cliente, tiempo_req) VALUES (NULL, '" + nombre + "'," + str(fintiempo) + ");"

        cursor.execute(q1)
        conn.commit()
        tiempo1.clear()
    cursor.execute('SELECT * FROM tiempo_pagina')
    data5 = cursor.fetchall()

    b = 'SELECT COUNT(fecha) FROM `eficiencia` WHERE trasac_complet=1'
    c = 'SELECT COUNT(fecha),fecha FROM `eficiencia` WHERE trasac_complet=0 GROUP by fecha'
    cursor.execute(c)
    data6 = cursor.fetchall()
    print(data6)

    sql = 'select * from sesion order by id desc limit 1'
    #sqlc = 'select * from ayuda order by id desc limit 1'
    cursor.execute(sql)
    sesion = cursor.fetchone()
    print(sesion['id'])

    sql1 = "UPDATE sesion set abandono=0 where id=" + str(sesion['id']) + ";"
    print(sql1)
    #cursor.execute(sqlc)
    #ayuda = cursor.fetchone()

    #sql_chat = "UPDATE ayuda set veces_ayuda="+ str(sum(cont_chat_array)) +" where id=" + str(ayuda['id']) + ";"
    #print(sql_chat)

    cursor.execute(sql1)
    #cursor.execute(sql_chat)
    conn.commit()

    c1 = 'SELECT COUNT(fecha) ,fecha FROM `sesion` WHERE abandono=1 GROUP by fecha'
    c_chat = 'SELECT * FROM ayuda where veces_ayuda >=1'
    cursor.execute(c1)
    data7 = cursor.fetchall()
    cursor.execute(c_chat)
    dfchat = cursor.fetchall()
    #cursor.execute('SELECT * FROM tiempo_pagina')
    #dft = cursor.fetchall()
    titular = request.form['titular']
    tarjeta = request.form['tarjeta']
    
    print ("INSERT INTO `pago_pruebas`(`Titular`, `Numero de tarjeta`, `Fecha de caducidad`, `CVC`, `Total`) VALUES 'hol',1,2,45,45454.25)")  
    print('holaaaaaaaaaaaaaaaaaaa ',productos_globales)
    ipq='''INSERT INTO `pago_pruebas` (`Titular`, `Numero de tarjeta`, `Fecha de caducidad`, `CVC`, `Total`) 
    VALUES ('Fabian garrido', '465468486', '2021', '852', '851.63');'''
    cursor.execute(ipq)
    conn.commit()

    cursor.close()
    conn.close()

    # b='SELECT COUNT(fecha) FROM `eficiencia` WHERE trasac_complet=1'
    # c='SELECT COUNT(fecha) as cantidad,fecha FROM `eficiencia` WHERE trasac_complet=0 GROUP by fecha'
  
    
    
   
    return render_template('facturacion.html', contacts=data, prom=val, contacts3=data3, numero=data4, tiempo=fintiempo,
                           timePage=data5, conFecha=data6, sesion_aban=data7, dfchat=dfchat, can_aban=can_aban)


@app.route('/cancelar', methods=['GET', 'POST'])
def cancelar():
    fecha = date.today()
    print(fecha)
    if request.method == "GET":
        nombre1 = nombre

        print("vchsvdhvdhv")

        elapsed_time = time() - start_time
        print(elapsed_time)
        '''
        laSuma = 0
        for i in tiempo:
            laSuma = laSuma + i
        print("el tempo total requerido es ", laSuma)
        q = "INSERT INTO eficiencia (id, cliente, tiempo_req, trasac_complet,fecha) VALUES (NULL, '" + nombre1 + "'," + str(
            round(laSuma, 2)) + ",0,'" + str(fecha) + "');"
        print(q)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(q)
        conn.commit()
        print("2datos ingresados")
        conn.close()'''
        return redirect(url_for('products'))


@app.route('/docente')
def docente():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM eficiencia')
    data = cursor.fetchall()
    cursor.close()
    return render_template('facturacion.html', contacts=data)


# @app.route('/es', methods=['GET','POST'])
# def j('/index'):
# return render_template('index.html')

@app.route('/en')
def info() -> 'html':
    return render_template('segundo.html')


@app.route('/fr')
def fran() -> 'html':
    return render_template('tercero.html')


# define app routes
@app.route("/contacto")
def index():
    return render_template("contacto.html")


@app.route("/get")
# function para que responda el bot

def get_bot_response():
    global cont_chat
    cont_chat_array.append(1)
    print(sum(cont_chat_array))
    userText = request.args.get('msg')

    if userText == "1":
        userText = '''Visualiza un producto y 
        mueve el mouse sobre el producto hasta que 
        salga el botón de añadir a su vez puedes poner la cantidad 
        del producto que requieres también, por último dale clic añadir, presiona 1, 2 o 3 si querias otra opción'''
        return str(userText)
    elif userText == "2":
        userText = '''Una vez tienes añadido  tus productos que vas
        a comprar puedes eliminarlos con el botón de eliminar
        o puede pasar a la siguiente paso de pago dando clic en pagar, presiona 1, 2 o 3 si querias otra opción
        '''
        return str(userText)
    elif userText == "3":
        userText = '''Si los datos de tu tarjeta son correctos y salió el mensaje gracias por su compra el proceso
         ha sido un éxito caso contrario tal vez sea un problema con el
        banco, o también los puedes contactar a este correo: fgarridom@ecomtop.com 
        o a este número de claro 
        +593982800451 en cual te brindaremos 
        una solución más personalizada a tu inconveniente gracias por confiar en  nosotros, presiona 1, 2 o 3 si querias otra opción'''
        return str(userText)
    else:
        userText = '''Escriba el número 1 o el 2 o el 3 de las opciones 
        presentes para que lo podamos ayudar en la navegación de nuestro sistema si desea que lo ayudemos en algo en particular por favor
        contactenos al número claro +593982800451  o a nuestro correo: fgarridom@ecomtop.com  para una ayuda más personalizada, muchas gracias , presiona 1, 2 o 3 si querias otra opción'''
        return str(userText)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)", (name, email, hash_password,))
        conn.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']

        cursor.close()

        conn.close()
        return redirect(url_for('products'))


@app.route('/login', methods=["GET", "POST"])
def login():
    fecha = date.today()
   

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        conn = mysql.connect()

        curl = conn.cursor(pymysql.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']

                qq = "INSERT INTO eficiencia (id, cliente, tiempo_req, trasac_complet,fecha) VALUES (NULL, '" + session[
                    'name'] + "'," + str(round(sum(tiempo), 2)) + ",0,'" + str(fecha) + "');"

                q1 = "INSERT INTO sesion (id, cliente, abandono,fecha) VALUES (NULL, '" + session[
                    'name'] + "'," + "1,'" + str(fecha) + "');"
                q2 = "INSERT INTO `ayuda`(`id`, `cliente`, `veces_ayuda`, `fecha`) VALUES (NULL, '" + session[
                    'name'] + "'," + str(sum(cont_chat_array)) + ",'" + str(fecha) + "');"
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                sql_ap = 'select * from abandono_pagina order by id desc limit 1'
                cursor.execute(sql_ap)
                sesion_ap = cursor.fetchone()

                sqlqu = "UPDATE abandono_pagina set c_abandono=0 where id=" + str(sesion_ap['id']) + ";"

                cursor.execute(q1)
                cursor.execute(q2)
                cursor.execute(sqlqu)
                cursor.execute(qq)
                conn.commit()
                print("Datos ingresados")
                conn.close()
                return redirect(url_for('formulario'))
            else:
                var = "Error password and email not match"
                return render_template("login.html", mes=var)
        else:
            return "Error user not found"
    else:
        return render_template("login.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    productos_globales.clear()
    cont_chat_array.clear()
    return redirect(url_for('.products'))

@app.route('/estadistica', methods=["GET", "POST"])
def estadistica():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)


    cursor.execute('SELECT * FROM eficiencia where trasac_complet=1')
    data = cursor.fetchall()

    cursor.execute('SELECT * FROM eficiencia where trasac_complet=0')
    data1 = cursor.fetchall()
    print(data1)

    cursor.execute('SELECT AVG(tiempo_req) FROM eficiencia WHERE trasac_complet=1')
    data2 = cursor.fetchall()
    prom = data2[0]
    val = round(prom['AVG(tiempo_req)'], 2)
    print(type(val))
    print(prom['AVG(tiempo_req)'])
    print('SELECT * FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    cursor.execute(
        'SELECT * FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    data3 = cursor.fetchall()

    cursor.execute(
        'SELECT COUNT(*) FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    print(
        'SELECT COUNT(*) FROM eficiencia WHERE trasac_complet=1 and ( tiempo_req>0 and tiempo_req <=' + str(val) + ')')
    num = cursor.fetchall()[0]

    data4 = num['COUNT(*)']

    print(data3)

    cursor.execute('SELECT COUNT(*) FROM abandono_pagina WHERE c_abandono=1')

    num_ap = cursor.fetchall()[0]

    can_aban = num_ap['COUNT(*)']

    dapa = cursor.execute('SELECT * FROM abandono_pagina')
    print(dapa)

    cursor.execute('SELECT * FROM tiempo_pagina')
    data5 = cursor.fetchall()

    b = 'SELECT COUNT(fecha) FROM `eficiencia` WHERE trasac_complet=1'
    c = 'SELECT COUNT(fecha),fecha FROM `eficiencia` WHERE trasac_complet=0 GROUP by fecha'
    cursor.execute(c)
    data6 = cursor.fetchall()
    print(data6)

    c1 = 'SELECT COUNT(fecha) ,fecha FROM `sesion` WHERE abandono=1 GROUP by fecha'
    c_chat = 'SELECT * FROM ayuda where veces_ayuda >=1'
    cursor.execute(c1)
    data7 = cursor.fetchall()
    cursor.execute(c_chat)
    dfchat = cursor.fetchall()
    # cursor.execute('SELECT * FROM tiempo_pagina')
    # dft = cursor.fetchall()
    cursor.close()

    conn.close()

    return render_template("estadistica.html",contacts=data, prom=val, contacts3=data3, numero=data4,
                           timePage=data5, conFecha=data6, sesion_aban=data7, dfchat=dfchat, can_aban=can_aban)
    
  
   

if __name__ == '__main__':
    app.run(port=8119, debug=True)