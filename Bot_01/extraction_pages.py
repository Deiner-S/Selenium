from bs4 import BeautifulSoup

class ExtractionPages():
    def __init__(self):
        self.data = {}

    def register(self,html):

        soup = BeautifulSoup(html,"html.parser")
        self.dados = {
        "chave_nota" : soup.find("span", class_="access_key_nfe").text,
        "numero da nota" : soup.find("span", class_="number_nfe").text,
        "cpf" : soup.find("input", class_="form-control mask_cpf_cnpj")["value"],
        "valor da nota": soup.find("span", id="total_produto_valor").text,
        "CFOP":soup.find("input", id="auto_natureza")["value"]}

    def products(self):
        pass
    def financial(self):
        pass
