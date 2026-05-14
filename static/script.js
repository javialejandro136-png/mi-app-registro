document.getElementById('formulario').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const nombre = document.getElementById('nombre').value;
    const contraseña = document.getElementById('contraseña').value;
    const correo = document.getElementById('correo').value;
    const telefono = document.getElementById('telefono').value;
    const mensaje = document.getElementById('mensaje');
    
    try {
        const response = await fetch('/registrar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre,
                contraseña,
                correo,
                telefono
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            mensaje.textContent = `¡Bienvenido ${nombre}! Tu cuenta ha sido creada.`;
            mensaje.className = 'mensaje success';
            document.getElementById('formulario').reset();
        } else {
            mensaje.textContent = data.error;
            mensaje.className = 'mensaje error';
        }
    } catch (error) {
        mensaje.textContent = 'Error en la conexión';
        mensaje.className = 'mensaje error';
    }
});