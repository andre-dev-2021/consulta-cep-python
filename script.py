import requests
import os

def consulta_cep():
    os.system("cls")
    cep = input("Informe um CEP para consulta (sem hífen): ")
    r = requests.get(f"https://viacep.com.br/ws//{cep}/json/")
    if r.status_code == 200:
        res = dict(r.json())
        try:
            print(f"{chr(9989)} Resultado: {res['logradouro']}, {res['bairro']}, {res['localidade']} - {res['uf']}")
        except KeyError:
            print(f"{chr(9888)} CEP inexistente!!")
    else:
        print(f"{chr(9888)} Formato de CEP incorreto!!")

def consulta_endereco():
    os.system("cls")
    uf = input("Informe o UF: ").upper()
    cidade = input("Informe o nome da cidade: ").capitalize()
    rua = input("Informe o nome da rua: ").capitalize()
    r = requests.get(f"https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/")
    if r.status_code == 200:
        res = r.json()
        if res == []:
            print(f"{chr(9888)} Nenhum resultado encontrado!!")
        else:
            print(f"{chr(9989)} Pesquisa realizada com sucesso!!")
            i = 0
            while i < len(res):
                print(f"{res[i]['cep']}: {res[i]['logradouro']} - {res[i]['localidade']}")
                i += 1
    else:
        print(f"{chr(9888)} Nenhum resultado encontrado!!")

os.system("cls")
print(f"Consulta CEP {chr(128269)}")
print("1 - Consulta por CEP")
print("2 - Consulta por endereço")
print("3 - Encerrar o programa")
opcao = input("Selecione uma opção: ")
if opcao == "3":
    exit()
elif opcao == "1":
    consulta_cep()
elif opcao == "2":
    consulta_endereco()
else:
    print("Opção inválida!")