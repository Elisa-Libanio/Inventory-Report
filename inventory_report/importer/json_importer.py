import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.__contains__("json"):
            with open(path) as file:
                data = json.load(file)
            return data
        else:
            raise ValueError("Arquivo inválido")

# class JsonImporter(Importer):
#     @classmethod
#     def import_data(cls, path):
#         if path.__contains__("json"):
#             with open(path) as file:
#                 response = json.load(file)
#             return response
#         else:
#             raise ValueError("Arquivo inválido")
