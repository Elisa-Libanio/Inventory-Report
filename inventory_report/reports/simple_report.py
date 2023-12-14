from datetime import datetime
from collections import Counter


class SimpleReport:

    @classmethod
    def generate(cls, file):
        fabricate_date = [item["data_de_fabricacao"] for item in file]
        expiration_date = [item["data_de_validade"] for item in file
                           if datetime.fromisoformat(item["data_de_validade"])
                           > datetime.now()]
        company_name = [item["nome_da_empresa"] for item in file]
        name_company = Counter(company_name).most_common(1)
        return(
            f"Data de fabricação mais antiga: {min(fabricate_date)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com maior quantidade de "
            f"produtos estocados: {name_company[0][0]}\n"
        )
