# Historial de Git y publicación en GitHub

**Proyecto:** Sistema de préstamo de equipos del LCI  
**Entregable:** historial de commits con al menos tres avances por etapas.

## 1. Estado actual del repositorio local

Los tres primeros commits ya fueron creados en el computador del estudiante desde la terminal de VS Code. La evidencia compartida muestra estos registros:

| Etapa | Hash corto | Mensaje registrado |
|---|---|---|
| 1. Modelo | `e4cbf10` | `Etapa 1: modelo del sistema con clases abstractas, herencia y excepciones` |
| 2. Controlador | `da5b61c` | `Etapa 2: implementar controlador y logica de prestamos` |
| 3. Vista y programa principal | `5411d13` | `Etapa 3: integrar vista de consola y programa principal` |

**No vuelvas a ejecutar `git init` ni repitas los commits 1, 2 y 3.** El repositorio ya está inicializado en la carpeta `TALLER1` y los tres commits existen.

## 2. Incorporar documentación y pruebas

Extrae los archivos de este paquete dentro de la carpeta `TALLER1`, donde está `main.py`. No reemplaces `Modelo/`, `Controlador/`, `Vista/` ni `main.py`, y no borres la carpeta oculta `.git`.

Completa el campo `[Completar nombre]` del archivo `README.md`. El `.gitignore` incluido conserva la exclusión de `.env`, además de `log.txt`, `__pycache__`, entornos virtuales y archivos `.zip`.

Abre la terminal de VS Code en `TALLER1` y revisa los archivos nuevos:

```powershell
git status
```

Ejecuta las pruebas en tu propio computador:

```powershell
python pruebas.py
```

La copia revisada de este paquete mostró **60 pruebas OK** y `TODAS LAS PRUEBAS PASARON`. Ejecuta el comando tú también y conserva una captura como evidencia de tu equipo.

## 3. Cuarto commit: documentación, UML, tablas y pruebas

Cuando confirmes que `pruebas.py` funciona y que los archivos complementarios están dentro de `TALLER1`, ejecuta:

```powershell
git add README.md pruebas.py INFORME_PRUEBAS.txt docs .gitignore
git status
git commit -m "Etapa 4: agregar documentacion, UML, tablas y pruebas"
```

Este cuarto commit agrega los documentos y pruebas que no estaban incluidos en los tres commits anteriores. Si Git dice `nothing to commit`, revisa `git status` y confirma que los archivos sí fueron extraídos dentro de `TALLER1`.

## 4. Verificar el historial y el estado

```powershell
git log --oneline -5
git status
```

Debes ver los tres commits anteriores y el cuarto commit de documentación. `git status` debe indicar que el árbol de trabajo está limpio (`nothing to commit, working tree clean`). Los hashes pueden tener diferencias si se hizo algún otro cambio; los mensajes y los commits son lo importante.

## 5. Crear el repositorio en GitHub

1. Entra en [https://github.com](https://github.com) e inicia sesión.
2. Pulsa el botón `+` y selecciona `New repository`.
3. Usa un nombre como `sistema-prestamo-lci`.
4. Selecciona `Public` o `Private` según lo indique el profesor. Si es privado, agrega al profesor como colaborador.
5. Crea el repositorio **vacío**: no marques `Add a README`, `.gitignore` ni licencia.
6. GitHub mostrará la dirección del repositorio. Copia la URL HTTPS que termina en `.git`.

En la terminal, todavía dentro de `TALLER1`, conecta el repositorio (reemplaza la dirección de ejemplo por la URL real):

```powershell
git remote add origin https://github.com/TU-USUARIO/sistema-prestamo-lci.git
git push -u origin main
```

Si aparece `remote origin already exists`, no agregues otro: revisa `git remote -v`. Si la URL está incorrecta, usa `git remote set-url origin https://github.com/TU-USUARIO/sistema-prestamo-lci.git` y después vuelve a ejecutar `git push -u origin main`.

Para autenticarte, usa el inicio de sesión de GitHub que ofrece VS Code o Git Credential Manager. Nunca escribas ni compartas tu contraseña o un token dentro de un archivo del proyecto.

## 6. Comprobación final

- Abre el enlace del repositorio en el navegador y confirma que aparecen `Modelo`, `Controlador`, `Vista`, `main.py`, `pruebas.py`, `README.md` y `docs/`.
- En la pestaña `Commits`, verifica que estén los avances registrados.
- Copia la dirección del repositorio desde el navegador y entrégala al profesor junto con los archivos, si así lo solicita.
- No publiques archivos `.env`, contraseñas, tokens ni datos privados.
