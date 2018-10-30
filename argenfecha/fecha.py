import datetime as dt

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


class Fecha(dt.date):

    # TODO: This could be done cleaner
    def fromString(dateString):
        """Create Fecha using Argentina's common way to write dates DD/MM/YYYY"""
        date = dt.datetime.strptime(dateString, "%d/%m/%Y").date()
        return Fecha(date.year, date.month, date.day)

    def __str__(self):
        """Return Fecha using Argentina's common way to write dates DD/MM/YYYY"""
        return self.strftime("%d/%m/%Y")

    def isDate(self, day, month):
        """Validates if a Fecha is an specified Date without year"""
        return self.day == day and self.month == month

    # TODO: Get a better name for this method
    def printableDateString(self):
        """Get Fecha as an specified Date without year"""
        return "{dia} de {mes}".format(dia=self.day, mes=meses[self.month-1])
