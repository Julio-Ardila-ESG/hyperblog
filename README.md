# hyperblog

Ejemplo de script en Python para registrar usuarios en ESGSuit utilizando datos
adicionales en un archivo XLSX.

## Requisitos

- Python 3.8 o superior
- Paquetes listados en `requirements.txt`

Instalación de dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
python esgsuit_register.py \
    --username <usuario> \
    --password <contrasena> \
    --apikey <apikey> \
    --url <url_del_servicio> \
    --xlsx datos.xlsx
```

El script leerá el archivo Excel y enviará una petición HTTP por cada fila
utilizando los datos del usuario y los de la fila como parámetros de la URL.

Puedes publicar este proyecto en GitHub de forma gratuita y ejecutar el script
de manera local para realizar pruebas.
