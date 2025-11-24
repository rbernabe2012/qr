# Formulario de Confirmación de Asistencia con Código QR

Este proyecto ofrece una aplicación web sencilla para que los asistentes confirmen su participación en la "Charla Axis Brokers". Cuando un asistente envía el formulario, sus datos se guardan en un archivo `customers.csv` y se envía una notificación por correo electrónico a una dirección preconfigurada.

## Cómo Usarlo

### Prerrequisitos
- Python 3
- pip

### 1. Instalación
Navega al directorio del proyecto en tu terminal e instala las dependencias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Configuración de Variables de Entorno (para el Correo con SendGrid)
Esta aplicación utiliza SendGrid para enviar notificaciones por correo. Para que funcione, necesitas una clave de API de SendGrid y configurar una variable de entorno.

**A. Obtén una Clave de API de SendGrid:**
1.  Crea una cuenta en [SendGrid](https://sendgrid.com/).
2.  Ve a **Settings -> API Keys** en el panel de SendGrid.
3.  Crea una nueva clave de API con permisos para enviar correos ("Mail Send").
4.  Copia la clave de API generada. **No la podrás ver de nuevo.**

**B. Establece la Variable de Entorno:**
Necesitas configurar una variable de entorno con tu clave de API de SendGrid.

**En macOS/Linux:**
```bash
export SENDGRID_KEY="tu-clave-de-api-de-sendgrid"
```

**En Windows (Símbolo del sistema):**
```bash
set SENDGRID_KEY="tu-clave-de-api-de-sendgrid"
```

**Nota:** Reemplaza el valor de ejemplo con tu clave de API real de SendGrid.

### 3. Ejecuta la Aplicación
Una vez instaladas las dependencias y configurada la variable de entorno, inicia la aplicación web:

```bash
python3 app.py
```

Esto iniciará un servidor de desarrollo de Flask, normalmente en `http://127.0.0.1:5000`.

### 4. Genera y Usa el Código QR
Para que el código QR funcione en tu red local (y no solo en tu máquina), necesitas generarlo usando la dirección IP de tu computadora.

**A. Encuentra tu Dirección IP Local:**
-   **En macOS/Linux:** Usa el comando `ifconfig` o `ip a`.
-   **En Windows:** Usa el comando `ipconfig`.
-   Busca una dirección que se parezca a `192.168.x.x`, `10.x.x.x`, etc.

**B. Genera el Código QR:**
Ejecuta el script de generación y pásale tu dirección IP como argumento:

```bash
python3 generate_qr.py tu-direccion-ip-local
```
*Ejemplo:*
```bash
python3 generate_qr.py 192.168.1.10
```

Esto creará un archivo `qr_code.png` que apunta a tu servidor. Ahora, los asistentes pueden escanear este código desde sus dispositivos para acceder al formulario.
