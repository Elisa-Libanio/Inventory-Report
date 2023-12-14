import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def readCSV(path):
    report = []
    with open(path) as data:
        data = csv.DictReader(data)
        for row in data:
            report.append(row)
    return report


def reader_xml(path):
    xml_var = ET.parse(path)
    root = xml_var.getroot()
    dict_list = []
    for item in root:
        dict = {}
        for element in item:
            dict[element.tag] = element.text
    dict_list.append(dict)
    return dict_list


def inventory_report(type, data):
    if type == "simples":
        return SimpleReport.generate(data)
    return CompleteReport.generate(data)


class Inventory():
    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            response = json.load(file)
        return response

    @classmethod
    def reader_xml(cls, path):
        xml_var = ET.parse(path)
        root = xml_var.getroot()
        dict_list = []
        for item in root:
            dict = {}
            for element in item:
                dict[element.tag] = element.text
            dict_list.append(dict)
        return dict_list

    @classmethod
    def import_data(cls, path, type):
        if path.endswith("csv"):
            data = readCSV(path)

        if path.endswith("json"):
            data = cls.read_json(path)

        if path.endswith("xml"):
            data = cls.reader_xml(path)
        return inventory_report(type, data)
