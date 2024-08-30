# Proyecto Urban Grocers

Este proyecto contiene una serie de pruebas automatizadas diseñadas para validar la funcionalidad de una API que gestiona la creación de kits para usuarios. Las pruebas están implementadas utilizando Pytest y cubren varios casos de prueba, incluyendo tanto escenarios positivos como negativos.

## Estructura del Proyecto

- **configuration.py**: Almacena las rutas y configuraciones necesarias para las pruebas.
- **create_kit_name_kit_test.py**: Contiene las pruebas que validan la creación de kits utilizando diferentes configuraciones de cuerpo de solicitud.
- **data.py**: Almacena los cuerpos de las solicitudes POST utilizados en las pruebas.
- **sender_stand_request.py**: Define las funciones que envían solicitudes a la API, incluyendo la creación de nuevos usuarios y kits.
- **README.md**: Este archivo, que proporciona una visión general del proyecto y su propósito.

## Requisitos

- Python 3.x
- Pytest
- Requests

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
3. Ejecuta las pruebas con `pytest` para verificar la funcionalidad de la API.


