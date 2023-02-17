# Desenvolvido por Kairo Trzeciak
# https://github.com/kairodev
from forex_python.converter import CurrencyRates
import platform
import os


class conversao:
    
    def __init__(self):
        sigla_origem = input("Sigla da moeda origem: ")
        sigla_destino = input("Sigla da moeda destino: ")
        quantidade = input("Quantidade (Sem pontuação): ")
        print(self.conversor(sigla_origem, sigla_destino, quantidade))

    def conversor(self, sigla_origem, sigla_destino, valor):

        try:
            valores = CurrencyRates()
            resultado = valores.convert(sigla_origem.upper(), sigla_destino.upper(), int(valor))
            self.limparTerminal()
            return ("Resultado: "+str(round(resultado,2))+"\n-------------------------")
        except:
            self.limparTerminal()
            return "Erro ocorrido ao realizar conversão, verifique se a sigla e o valor estão corretos.\n-------------------------"

    def limparTerminal(self):

        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')

    

if __name__ == "__main__":
    while True:
        conversao()
        continue
        

