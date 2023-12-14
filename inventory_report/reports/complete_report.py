from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, file):
        simple_report = SimpleReport.generate(file)
        company_name = [item["nome_da_empresa"] for item in file]
        result = ""
        for name in company_name:
            quantity = company_name.count(name)
            if not result.__contains__(name):
                result += f"- {name}: {quantity}\n"
        return (f"{simple_report}\n" +
                "Produtos estocados por empresa: \n" + f"{result}")
