# Encargo 4 · KPIs adicionales — no calculables con los datos del repo

No se genera `resultados/kpis.csv`: **los dos indicadores pedidos necesitan datos que no existen en este repo**, y no se van a sustituir por valores «típicos del sector».

## Rotación anual por SKU
Fórmula del encargo: `demanda anual / stock medio`.
- La demanda anual sí existe (`datos/ex2_sku_master.csv`, columna `annual_demand`).
- **El stock medio no existe**: ninguno de los ficheros de `datos/` trae stock, ni inicial ni final ni mensual. Con la demanda sola no se puede calcular.

## Días con rotura de stock por SKU en 2026
- `datos/ex1_demand_daily.csv` tiene una columna `stockout_flag`, pero corresponde a **una sola referencia de Fast&City** (otra empresa), con 120 días desde el 2026-09-01. No es el catálogo de Zeta Wear ni cubre el año 2026.
- `datos/ex2_monthly_sales.csv` trae ventas mensuales, no roturas.

## Qué haría falta para calcularlos
1. Historial de stock por SKU (fin de mes o diario) para obtener el stock medio.
2. Un registro diario de roturas por SKU para 2026, o stock diario para derivarlas (días con stock = 0).

Cuando esos datos estén en `datos/`, el cálculo es directo: `rotacion = annual_demand / mean(stock)` y `dias_rotura = count(stock == 0)`.
