import datetime as dt
import abc


class Fecha(dt.date):
    """el convertstring """
    """Re cabeza"""

    def fromString(dateString):
        date = dt.datetime.strptime(dateString, "%d/%m/%Y").date()
        return Fecha(date.year, date.month, date.day)

    def __str__(self):
        return self.strftime("%d/%m/%Y")
