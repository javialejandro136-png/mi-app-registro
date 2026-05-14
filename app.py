from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    datos = request.json
    nombre = datos.get('nombre', '').strip()
    contraseña = datos.get('contraseña', '').strip()
    correo = datos.get('correo', '').strip()
    telefono = datos.get('telefono', '').strip()
    
    # Validaciones
    if not nombre:
        return jsonify({'error': 'Por favor ingresa tu nombre'}), 400
    
    if not contraseña or len(contraseña) < 6:
        return jsonify({'error': 'La contraseña debe tener al menos 6 caracteres'}), 400
    
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not correo or not re.match(patron_correo, correo):
        return jsonify({'error': 'Por favor ingresa un correo válido'}), 400
    
    if not telefono or not telefono.isdigit() or len(telefono) < 7:
        return jsonify({'error': 'Por favor ingresa un teléfono válido'}), 400
    
    return jsonify({
        'success': True,
        'mensaje': f'¡Bienvenido {nombre}!'
    })

if __name__ == '__main__':
    app.run(debug=True)