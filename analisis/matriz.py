"""Matriz ABC x XYZ y politicas de gestion (encargo 3).

Cruza resultados/abc.csv y resultados/xyz.csv. Solo se escribe politica para
las celdas OCUPADAS: una celda vacia no recibe politica.
"""
import csv
import os

BASE = os.path.join(os.path.dirname(__file__), "..")
RES = os.path.join(BASE, "resultados")

POLITICAS = {
    "AX": "Reposición automática por punto de pedido, servicio alto (~98 %), colchón bajo y conteo cíclico frecuente. Decide el sistema; una persona solo revisa excepciones.",
    "AY": "Revisión periódica corta con previsión suavizada y colchón medio (servicio 95-97 %). Decide una persona (planificador) apoyada por el sistema.",
    "AZ": "Atención máxima de una persona: colchón alto y seguimiento semanal; no automatizar.",
    "BX": "Reposición automática con lotes medios y servicio ~95 %; conteo trimestral. Decide el sistema.",
    "BY": "Revisión periódica estándar con colchón medio y lotes medios; el sistema propone y una persona supervisa cada mes.",
    "BZ": "Sin regla automática: pedidos en lotes pequeños ligados a demanda confirmada y colchón limitado; la decisión se toma con Comercial.",
    "CX": "Política simple: lotes grandes, servicio ~90 % y conteo anual. Decide el sistema.",
    "CY": "Revisión poco frecuente, lotes grandes y colchón mínimo; sin análisis fino.",
    "CZ": "Mínima atención: pedir bajo demanda o dejar agotar, sin colchón; candidata a revisar el catálogo.",
}


def leer(nombre):
    with open(os.path.join(RES, nombre), newline="", encoding="utf-8") as f:
        return {r["sku"]: r for r in csv.DictReader(f)}


def main():
    abc, xyz = leer("abc.csv"), leer("xyz.csv")
    filas = []
    for sku, a in abc.items():
        x = xyz[sku]
        filas.append({"sku": sku, "clase_abc": a["clase_abc"], "cv": x["cv"],
                      "clase_xyz": x["clase_xyz"], "celda": a["clase_abc"] + x["clase_xyz"]})

    with open(os.path.join(RES, "clasificacion.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["sku", "clase_abc", "cv", "clase_xyz", "celda"])
        w.writeheader()
        w.writerows(filas)

    cuenta = {}
    for r in filas:
        cuenta.setdefault(r["celda"], []).append(r["sku"])

    with open(os.path.join(RES, "politicas.md"), "w", encoding="utf-8") as f:
        f.write("# Políticas de gestión por celda ABC×XYZ\n\n")
        for celda in sorted(cuenta):
            f.write(f"## {celda} ({len(cuenta[celda])} referencias)\n")
            f.write(f"{POLITICAS[celda]}\n\n")
            f.write("Referencias: " + ", ".join(cuenta[celda]) + "\n\n")

    for celda in sorted(cuenta):
        print(celda, len(cuenta[celda]))


if __name__ == "__main__":
    main()
