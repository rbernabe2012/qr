# Formulario de Datos de Clientes con Código QR

Este proyecto ofrece una aplicación web sencilla para recolectar datos de clientes (nombre, teléfono y correo electrónico). Cuando un cliente envía el formulario, sus datos se guardan en un archivo `customers.csv` y se envía una notificación por correo electrónico a una dirección preconfigurada.

## Cómo Usarlo

### Prerrequisitos
- Python 3
- pip

### 1. Instalación
Navega al directorio del proyecto en tu terminal e instala las dependencias requeridas desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Configuración de Variables de Entorno (para el Correo)
Esta aplicación utiliza el servidor SMTP de Gmail para enviar notificaciones por correo. Para que funcione, debes configurar tu cuenta de Gmail y establecer las siguientes variables de entorno.

**A. Configura tu Cuenta de Gmail:**
1.  Ve a la configuración de tu Cuenta de Google.
2.  En la sección "Seguridad", busca "Verificación en 2 pasos" y actívala.
3.  Después de activarla, ve a "Contraseñas de aplicaciones", genera una nueva contraseña para esta aplicación y copia la contraseña de 16 caracteres.

**B. Establece las Variables de Entorno:**
Necesitas configurar dos variables de entorno con tus credenciales de correo.

**En macOS/Linux:**
```bash
export EMAIL_USER="tu-email@gmail.com"
export EMAIL_PASS="tu-contraseña-de-aplicacion-de-16-caracteres"
```

**En Windows (Símbolo del sistema):**
```bash
set EMAIL_USER="tu-email@gmail.com"
set EMAIL_PASS="tu-contraseña-de-aplicacion-de-16-caracteres"
```

**Nota:** Reemplaza los valores de ejemplo con tu dirección de Gmail real y la contraseña de aplicación que generaste.

### 3. Ejecuta la Aplicación
Una vez instaladas las dependencias y configuradas las variables de entorno, inicia la aplicación web:

```bash
python3 app.py
```

Esto iniciará un servidor de desarrollo de Flask, normalmente en `http://127.0.0.1:5000`. Para acceder desde otros dispositivos en tu red, utiliza la dirección IP local de tu computadora (ej., `http://192.168.1.10:5000`).

### 4. Usa el Código QR
El archivo `qr_code.png` incluido está configurado para la dirección del servidor por defecto (`http://localhost:5000`). Si necesitas enlazarlo a una dirección diferente (como una URL pública), puedes regenerarlo editando la variable `data` en `generate_qr.py` y ejecutando el script:

```bash
python3 generate_qr.py
```
