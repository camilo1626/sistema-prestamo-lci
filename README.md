# Sistema de préstamo de equipos del LCI

Proyecto académico de Programación Orientada a Objetos. Implementa un sistema de consola para gestionar préstamos, devoluciones y reservas de equipos de laboratorio.

## Estructura del proyecto

- `Modelo/`: equipos, usuarios, préstamos y excepciones.
- `Controlador/`: datos iniciales y lógica de negocio (`PrestamoController`).
- `Vista/`: interacción por consola.
- `main.py`: punto de entrada del programa.
- `pruebas.py`: pruebas automatizadas.
- `INFORME_PRUEBAS.txt`: resultados de la verificación incluida.
- `docs/`: diagrama UML, tablas, documentación y guía de Git/GitHub.

## Requisitos

- Python 3 instalado.
- Git instalado para consultar y conservar el historial de cambios.

## Ejecución

Abre una terminal dentro de esta carpeta (`TALLER1`) y ejecuta:

```bash
python main.py
```

Para ejecutar las pruebas automáticas:

```bash
python pruebas.py
```

La ejecución de las pruebas puede crear `log.txt`; el archivo está excluido del repositorio mediante `.gitignore`.

## Arquitectura

El proyecto separa responsabilidades con MVC: el Modelo contiene las entidades y reglas, la Vista solicita y muestra información, y el Controlador coordina las operaciones. Se utilizan clases abstractas, herencia, polimorfismo y excepciones personalizadas.

## Entregables complementarios

Consulta la carpeta `docs/`: incluye el diagrama UML en PNG y PDF, las tablas de casos de prueba y del taller, la documentación del proyecto y la guía para publicar el repositorio en GitHub.

**Estudiante:** Camilo  
**Asignatura:** Programación 2
