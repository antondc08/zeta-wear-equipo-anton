# Auditoría del borrador de Gemini (paso 6.2 de la guía)

**Encargo a Gemini:** memo de 5 líneas al director de operaciones con las 5 referencias que más atención de gestión merecen, citando la celda de la matriz y una cifra en euros, solo con los datos de `clasificacion.csv`.

**Referencias que propuso:** ZW-CAZ-002, ZW-VES-001, ZW-VES-003, ZW-VES-002 y ZW-DEN-002.

## Qué comprobamos y qué salió

| # | Afirmación del borrador | Contraste con los datos | Tipo de fallo |
|---|---|---|---|
| 1 | «ZW-CAZ-002 … refleja en los datos una cifra de **0,7340 €**» | 0,734 es el **CV** de ZW-CAZ-002 en `clasificacion.csv` (coeficiente de variación, sin unidad). No son euros. Su margen anual real es **25.470 €** | Dato mal etiquetado (cifra con unidad inventada) |
| 2 | Pedía una cifra en euros por referencia | El borrador no da ninguna cifra en euros verdadera | Incumple el encargo |
| 3 | Las cinco «combinan el **mayor valor estratégico** con demanda fluctuante» | Tres de las cinco son de clase B (ZW-CAZ-002 es la 13.ª por margen con 25.470 €, ZW-VES-003 la 12.ª con 25.720 €, ZW-VES-001 la 8.ª con 39.525 €). Las dos de mayor margen, ZW-TEE-001 (411.000 €) y ZW-DEN-001 (369.000 €), no aparecen | Error de criterio: ordena por volatilidad e ignora el valor |
| 4 | «Como **máxima prioridad**, ZW-CAZ-002» | Es una referencia de margen bajo dentro del catálogo; los datos no justifican esa prioridad | Afirmación sin respaldo |
| 5 | Cita «la celda BZ y la celda AY» en bloque | Las celdas son correctas (CAZ-002, VES-001, VES-003 en BZ; VES-002 y DEN-002 en AY), pero no indica la celda de cada referencia, como pide el encargo | Forma incompleta |
| 6 | «sobrecostes de inventario», «riesgo crítico de roturas», «gestión exhaustiva» | Ninguna cifra respalda esos términos: son adjetivos | Adjetivos sin datos |

**Lo que hizo bien:** no inventó ningún «benchmark del sector» ni dato externo; las cinco referencias existen y sus celdas son correctas.

## Veredicto
**RECHAZAR el borrador.** El error más grave es la cifra de 0,7340 € (un CV presentado como dinero), seguido de una selección incoherente con la matriz. Se mantiene el `memo.md` del equipo, cuyas cifras se recalcularon a mano (margen de ZW-TEE-001 = 60.000 × (9,95 − 3,10) = 411.000 €, etc.).

## Comparación de las dos selecciones
- Coinciden en 2 de 5: **ZW-DEN-002** (AY) y **ZW-VES-001** (BZ).
- Nuestro memo incluye las referencias de mayor margen (ZW-TEE-001, ZW-DEN-001, ZW-TEE-002); el borrador de Gemini las deja fuera.
- Nuestro memo cita en cada línea la celda y una cifra en euros verificada; el de Gemini no.
