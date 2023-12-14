from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(InventoryIterator):
    def __init__(self, importer=JsonImporter, data=[]):
        self.importer = importer
        self.data = []
        self.data.extend(data)

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type_report):
        report_dict = {
            'simples': SimpleReport.generate,
            'completo': CompleteReport.generate
        }
        new_data = self.importer.import_data(path)
        self.data.extend(new_data)
        return report_dict[type_report](new_data)
