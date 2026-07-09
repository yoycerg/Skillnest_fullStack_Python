from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def hola_mundo():

   return '¡Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/contacto')     

def contacto():

   return '¡Conócenos un poco más!'

@app.route('/personas') 

def personas():

   return '¡Conoce a las personas!'

@app.route('/pagina') 

def pagina():

   return '¡Conoce sobre esta pagina!'

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente   

   app.run(debug=True)    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo