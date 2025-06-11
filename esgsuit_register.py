#!/usr/bin/env python3
"""Herramienta de línea de comandos para registrar usuarios en ESGSuit.

Lee un archivo Excel con datos adicionales y envía peticiones HTTP
al servicio especificado con esos datos y la información de autenticación
proporcionada por el usuario.
"""
import argparse
import openpyxl
import requests


def parse_args():
    parser = argparse.ArgumentParser(description="Registro en ESGSuit")
    parser.add_argument("--username", required=True, help="Nombre de usuario")
    parser.add_argument("--password", required=True, help="Contraseña")
    parser.add_argument("--apikey", required=True, help="API key")
    parser.add_argument("--url", required=True, help="URL del servicio")
    parser.add_argument("--xlsx", required=True, help="Ruta al archivo XLSX")
    return parser.parse_args()


def read_excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    rows = list(sheet.iter_rows(values_only=True))
    headers = rows[0]
    for row in rows[1:]:
        yield dict(zip(headers, row))


def main():
    args = parse_args()
    for row_data in read_excel(args.xlsx):
        params = {
            "username": args.username,
            "password": args.password,
            "apikey": args.apikey,
        }
        params.update({k: v for k, v in row_data.items() if v is not None})
        response = requests.get(args.url, params=params)
        print("Petición realizada con código:", response.status_code)
        if response.content:
            print("Respuesta:", response.text)


if __name__ == "__main__":
    main()
