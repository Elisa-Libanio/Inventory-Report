import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as data:
            if path.__contains__("xml"):
                a = data.read()
                dadosx = xmltodict.parse(a)
                return dadosx["dataset"]["record"]
            else:
                raise ValueError("Arquivo inválido")
