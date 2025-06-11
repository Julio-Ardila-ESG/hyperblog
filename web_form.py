#!/usr/bin/env python3
"""Aplicación web simple para registrar usuarios en ESGSuit utilizando un formulario HTML."""

from flask import Flask, request, render_template_string
import openpyxl
import requests


HTML_FORM = """
<!doctype html>
<title>Registro ESGSuit</title>
<h1>Enviar datos a ESGSuit</h1>
<form method=post enctype=multipart/form-data>
  <label>Usuario:<br><input type=text name=username required></label><br>
  <label>Contraseña:<br><input type=password name=password required></label><br>
  <label>API key:<br><input type=text name=apikey required></label><br>
  <label>URL del servicio:<br><input type=text name=url required></label><br>
  <label>Archivo XLSX:<br><input type=file name=xlsx accept=.xlsx required></label><br><br>
  <input type=submit value=Enviar>
</form>
"""

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        apikey = request.form['apikey']
        service_url = request.form['url']
        xlsx_file = request.files['xlsx']

        wb = openpyxl.load_workbook(xlsx_file)
        sheet = wb.active
        rows = list(sheet.iter_rows(values_only=True))
        headers = rows[0]
        for row in rows[1:]:
            row_data = dict(zip(headers, row))
            params = {
                'username': username,
                'password': password,
                'apikey': apikey,
            }
            params.update({k: v for k, v in row_data.items() if v is not None})
            response = requests.get(service_url, params=params)
            print('Petición realizada con código:', response.status_code)
        return 'Datos enviados. Revisa la consola para obtener detalles.'
    return render_template_string(HTML_FORM)


if __name__ == '__main__':
    app.run(debug=True)
