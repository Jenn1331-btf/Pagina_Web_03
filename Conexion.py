from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)

def obtener_conexion():
    return pyodbc.connect(
                          'DRIVER = {ODBC Driver 17 for SQL Server};'
                          'SERVER = .;'
                          'DATABASE = usuario'
                          'Trusted_Connection = yes;'
                        )

@app.route("/")
def mostrar_registro():
    return render_template("Crear_Cuenta.html")

@app.route("/registro", methods = ["POST"])
def registrar():
    nombre = request.form["nombre"]
    ap_paterno = request.form["apellido_p"]
    ap_materno = request.form["apellido_m"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    fecha_nac = request.form["fecha_nac"]

    try: 
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "INSERT INTO usuario (correo, contraseña, fecha_registro, nomb_usu, apem_usu, apep_usu) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (correo, contrasena, fecha_nac, nombre, ap_paterno, ap_materno))
        conexion.commit()
        print("USUARIO GUARDADO EXITOSAMENTE")
    except Exception as e:
        print(f"Error al registrar el usuario: {e}")
    finally:
        cursor.close()
        conexion.close()

    return "<h1>¡Cuenta creada con éxito!</h1>"

if __name__ == "__main__":
    app.run(debug=True)