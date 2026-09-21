"""Clasificacion ABC por margen anual (encargo 1).

Criterio de valor: MARGEN = annual_demand * (price - cost).
Cortes: A hasta el 80 % acumulado (inclusive), B hasta el 95 %, C el resto.
"""
import csv
import os

BASE = os.path.join(os.path.dirname(__file__), "..")
ENTRADA = os.path.join(BASE, "datos", "ex2_sku_master.csv")
SALIDA = os.path.join(BASE, "resultados", "abc.csv")


def main():
    with open(ENTRADA, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    for r in filas:
        r["margen_anual"] = float(r["annual_demand"]) * (float(r["price"]) - float(r["cost"]))

    filas.sort(key=lambda r: r["margen_anual"], reverse=True)
    total = sum(r["margen_anual"] for r in filas)

    acumulado = 0.0
    for r in filas:
        acumulado += r["margen_anual"]
        pct = 100.0 * acumulado / total
        r["pct_acumulado"] = pct
        r["clase_abc"] = "A" if pct <= 80 else ("B" if pct <= 95 else "C")

    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    with open(SALIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sku", "margen_anual", "pct_acumulado", "clase_abc"])
        for r in filas:
            w.writerow([r["sku"], round(r["margen_anual"], 2), round(r["pct_acumulado"], 2), r["clase_abc"]])

    print(f"Margen total: {total:,.2f} EUR")
    for clase in "ABC":
        print(clase, sum(1 for r in filas if r["clase_abc"] == clase))


if __name__ == "__main__":
    main()
