from ics import Calendar, Event
from datetime import datetime, timedelta
from ics.grammar.parse import ContentLine
import pytz

# Crear un nuevo calendario
cal = Calendar()

# Detalles de las clases
classes = [{
    "name": "Clase de Ejemplo",
    "days": [
        {
            "day": "Monday",
            "start_time": "09:00",
            "end_time": "10:30",
            "location": "Campus Central | Salon 101"
        },
        {
            "day": "Wednesday",
            "start_time": "11:00",
            "end_time": "12:30",
            "location": "Campus Norte | Salon 202"
        },
        {
            "day": "Friday",
            "start_time": "15:00",
            "end_time": "16:30",
            "location": "Campus Sur | Salon 303"
        }
    ]
}]


# Mapa de días de la semana a valores numéricos
days_map = {
    "Monday": 'MO',
    "Tuesday": 'TU',
    "Wednesday": 'WE',
    "Thursday": 'TH',
    "Friday": 'FR',
}

# Fecha de inicio y fin del semestre
start_date = datetime(2024, 8, 5)
end_date = datetime(2024, 12, 1)

# Zona horaria de Colombia
colombia_tz = pytz.timezone('America/Bogota')


def get_calendar_week():
    for cls in classes:
        for day in cls["days"]:
            days = days_map[day["day"]]

            # Crear el evento
            event = Event()

            # Convertir las horas locales a UTC
            start_datetime_local = colombia_tz.localize(datetime.combine(
                start_date, datetime.strptime(day["start_time"], "%H:%M").time()))
            end_datetime_local = colombia_tz.localize(datetime.combine(
                start_date, datetime.strptime(day["end_time"], "%H:%M").time()))

            start_datetime_utc = start_datetime_local.astimezone(pytz.utc)
            end_datetime_utc = end_datetime_local.astimezone(pytz.utc)

            # Establecer propiedades del evento
            event.name = cls["name"]
            event.begin = start_datetime_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
            event.end = end_datetime_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
            event.location = day["location"]
            event.description = f"{cls['name']} en {day['location']}"

            # Definir la regla de repetición
            start_date_formatted = start_date.strftime('%Y%m%dT%H%M%SZ')
            end_date_formatted = end_date.strftime('%Y%m%dT%H%M%SZ')
            event.extra.append(ContentLine(
                name="RRULE", value=f"FREQ=WEEKLY;BYDAY={days};UNTIL={end_date_formatted}"))

            cal.events.add(event)

        # Guardar el archivo .ics
    ics_file = "university-schedule.ics"
    with open(ics_file, "w") as f:
        f.writelines(cal)
    print("Archivo .ics creado:", ics_file)


get_calendar_week()
