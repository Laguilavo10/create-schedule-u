# University Schedule Creator

Este proyecto permite crear un archivo `.ics` para gestionar el horario de la universidad, así como otros eventos personalizados.

## Descripción

El script en `main.py` toma una lista de clases con sus respectivos días, horas y ubicaciones, y genera un archivo `.ics` que puede ser importado en cualquier calendario compatible con el formato iCalendar.

## Requisitos

- Python 3.x
- Paquetes de Python: `ics`, `pytz`

Puedes instalar los paquetes necesarios utilizando `pip`:

```sh
pip install ics pytz
```

## Uso
1. Clona el repositorio o descarga los archivos.
```sh
git clone https://github.com/tu-usuario/university-schedule-creator.git
cd university-schedule-creator
```
2. Asegúrate de tener los paquetes necesarios instalados.
3. Modifica la lista de clases en el archivo `main.py`.
4. Ejecuta el script `py main.py` para generar el archivo `university-schedule.ics.`

5. Importa el archivo `university-schedule.ics` en tu calendario preferido.

## Personalizacion

Puedes agregar más eventos personalizados modificando la lista classes en `main.py`. Cada evento debe tener el siguiente formato:
```sh
{
    "name": "Nombre del Evento",
    "days": [
        {
            "day": "Día de la Semana (Monday, Tuesday, Wednesday, Thursday, Friday)",
            "start_time": "Hora de Inicio (HH:MM)",
            "end_time": "Hora de Fin (HH:MM)",
            "location": "Ubicación"
        }
    ]
}

```
 
## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.