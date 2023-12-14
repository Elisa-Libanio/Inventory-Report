import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.__contains__("csv"):
            with open(path) as file:
                data = csv.DictReader(file)
                data2 = list(data)
                return data2
        else:
            raise ValueError("Arquivo inválido")
