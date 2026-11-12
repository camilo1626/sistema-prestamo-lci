# Lista de verificación final del taller

**Proyecto:** Sistema de préstamo de equipos del LCI  
**Asignatura:** Programación 2

## 1. Entregables preparados

| Entregable | Archivo | Estado |
|---|---|---|
| 1. Diagrama de clases | `docs/01_Diagrama_UML/Diagrama_UML_clases.png` y `.pdf` | Preparado |
| 2. Tabla de casos de prueba | `docs/02_Tablas/Tabla_casos_prueba.xlsx` | Preparada: 51 casos |
| Tablas de apoyo del taller | `docs/02_Tablas/Todas_las_tablas_del_taller.xlsx` | Preparadas: equipos, usuarios, peticiones, códigos, criterios y entregables |
| 3. Código fuente | `Modelo/`, `Controlador/`, `Vista/`, `main.py` | Está en la carpeta `TALLER1` del estudiante |
| Pruebas automatizadas | `pruebas.py` e `INFORME_PRUEBAS.txt` | Preparadas; deben ejecutarse en el computador del estudiante |
| Documentación y sustentación | `docs/03_Documentacion/Documentacion_y_sustentacion.docx` | Preparada |
| 4. Historial Git | Historial local de `TALLER1` | Tres commits ya creados; falta el commit de documentación |
| Publicación GitHub | Repositorio remoto | Pendiente de crear y publicar |

## 2. Antes de realizar el cuarto commit

1. Extrae el paquete de complementos dentro de la carpeta `TALLER1` donde está `main.py`. No reemplaces `Modelo/`, `Controlador/`, `Vista/` ni `main.py`; no borres `.git`.
2. El `README.md` ya incluye el nombre de pila indicado para la entrega; si prefieres otro formato, puedes cambiarlo antes de publicar.
3. Conserva el `.gitignore` incluido. Comprueba que contiene `.env`, `log.txt`, `__pycache__/`, `venv/`, `.venv/` y `*.zip`.
4. Ejecuta `python pruebas.py` desde `TALLER1`. La copia de revisión utilizada para preparar el paquete pasó 60 pruebas; verifica el resultado en tu propio computador.
5. Ejecuta `python main.py` y confirma que aparece el menú.
6. Crea el cuarto commit con los comandos de `docs/04_Git_y_GitHub/Comandos_Git_y_GitHub.md`. **No repitas los tres commits que ya existen.**

## 3. Historial ya registrado en tu computador

La evidencia enviada muestra estos tres commits:

- `e4cbf10` — Etapa 1: modelo del sistema con clases abstractas, herencia y excepciones.
- `da5b61c` — Etapa 2: implementar controlador y logica de prestamos.
- `5411d13` — Etapa 3: integrar vista de consola y programa principal.

Después de agregar la documentación, el historial esperado tendrá un cuarto commit. Compruébalo con `git log --oneline -5`.

## 4. Publicación en GitHub

1. Crea un repositorio vacío, sin README, `.gitignore` ni licencia inicial.
2. Configura `origin` con la URL HTTPS real de tu repositorio.
3. Ejecuta `git push -u origin main`.
4. Abre el repositorio en el navegador y verifica que los archivos y commits estén visibles.
5. Copia el enlace del repositorio para entregarlo. Si el repositorio es privado, agrega al profesor como colaborador.

## 5. Verificaciones realizadas al preparar este paquete

- Se ejecutó `python pruebas.py` en una copia temporal integrada con el código del proyecto recibido: **60 pruebas OK** y `TODAS LAS PRUEBAS PASARON`.
- Las 25 peticiones del mostrador coincidieron con los resultados esperados incluidos en el taller.
- Se verificaron los casos adicionales de rollback, códigos inválidos, fechas, polimorfismo y excepciones.
- Esta ejecución no sustituye la comprobación en el computador del estudiante. Guarda una captura de tu propia ejecución.

## 6. Puntos que conviene confirmar con el profesor

- Qué mensaje mostrar cuando no existe un código de usuario o equipo. El proyecto lo registra como `SYS-00`, aunque el taller no define un código específico para ese escenario.
- Cuánto dura una reserva y quién tiene prioridad cuando varias personas reservan el mismo equipo. El taller no define esos criterios.
- Qué pasa con una reserva cuando el equipo se presta o se devuelve.
- Si el profesor exige que el repositorio GitHub sea público o privado y si requiere el enlace como parte de la entrega.

## 7. Orden de entrega

Según la guía, organiza los entregables así: (1) diagrama de clases, (2) tabla de casos de prueba, (3) código fuente, (4) historial de Git y (5) sustentación oral de cinco minutos. Adjunta además la documentación y las tablas complementarias si el profesor las solicita.
