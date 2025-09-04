import pandas as pd
import os

arquivo = "corretores.csv"

#entrada de dados

print("Sobre o corretor:")
nome = input("Insira nome e sobrenome do corretor: ")
genero = input("Insira genero do corretor: ")
creci = int(input("Insira o creci, (apenas números): "))
data = input("Insira a data de início do corretor: ")

print("Sobre o desempenho: ")

captacoes = int(input("Captações do corretor: "))
vendas = int(input("Vendas do corretor: "))
gestoes = int(input("Gestoes do corretor: "))
alugados = int(input("Alugados do corretor: "))

#criando o dataframe
df_novo = pd.DataFrame ([{

    "NOME": nome,
    "GENERO": genero,
    "CRECI": creci,
    "DATA": data,
    "CAPTAÇÕES": captacoes,
    "VENDAS": vendas,
    "ALUGADOS": alugados,
    "GESTÃO": gestoes
}])

if os.path.exists(arquivo):
    df_existente = pd.read_csv(arquivo)
    df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)
    df_atualizado.to_csv(arquivo, index=False, encoding="utf-8-sig")
    print("Arquivo atualizado com sucesso!")

else:
    df_novo.to_csv(arquivo, index=False, encoding="utf-8-sig")
    print("Arquivo salvo com sucesso!")
