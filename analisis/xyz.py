"""Clasificacion XYZ por coeficiente de variacion (encargo 2).

Serie: ventas MENSUALES 2026 (datos/ex2_monthly_sales.csv, 20 SKU x 12 meses).
Desviacion tipica POBLACIONAL (divide entre n = 12).
Umbrales: X: cv <= 0,25 · Y: 0,25 < cv <= 0,5 · Z: cv > 0,5.
"""
import csv
import math
import os

BASE = os.path.join(os.path.dirname(__file__), "..")
ENTRADA = os.path.join(BASE, "datos", "ex2_monthly_sales.csv")
SALIDA = os.path.join(BASE, "resultados", "xyz.csv")


def clase(cv):
    return "X" if cv <= 0.25 else ("Y" if cv <= 0.5 else "Z")


def main():
    filas = []
    with open(ENTRADA, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        meses = [c for c in lector.fieldnames if c != "sku"]
        for r in lector:
            ventas = [float(r[m]) for m in meses]
            media = sum(ventas) / len(ventas)
            desv = math.sqrt(sum((v - media) ** 2 for v in ventas) / len(ventas))
            cv = desv / media
            filas.append((r["sku"], media, desv, cv))

    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    with open(SALIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sku", "media_mensual", "desv_tipica", "cv", "clase_xyz"])
        for sku, media, desv, cv in filas:
            w.writerow([sku, round(media, 2), round(desv, 2), round(cv, 4), clase(cv)])

    for c in "XYZ":
        print(c, sum(1 for _, _, _, cv in filas if clase(cv) == c))


if __name__ == "__main__":
    main()
