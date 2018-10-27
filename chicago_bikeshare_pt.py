# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

print("Lendo o documento...")
with open('chicago.csv') as f: #lendo o csv utilizando a dica sugerida: uma lista de dicionários :)
    data_list = [{k: v for k, v in row.items()}
         for row in csv.DictReader(f, skipinitialspace=True)]
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[0])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for index in range(20):
    gender = data_list[index]['Gender']
    print(gender)

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data: list, index: int) -> list:
    """"
    Função para criar uma lista com todos os dados de uma coluna, dada uma outra lista
    :param:
        data: o esquema de dados a partir do qual iremos extrair a nova lista
        index: indice do data_set que queremos transformar em uma nova lista
    :return:
        Uma lista contendo apenas os valores da coluna indicada como indice
    """
    keys_list = list(data_list[0].keys()) #extraio as chaves do dicionário e coloco-as em uma lista
    column_list = []
    for item in data:
        column_list.append(item[keys_list[index]])
    return column_list

print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
for item in data_list:
    gender = item['Gender']
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
def count_gender(data_list: list) -> list:
    """
    Função para contar o número de homens e mulheres dada uma amostra
    :param data_list:
        data_list: lista contendo as amostras para extração dos dados
    :return:
        Uma lista contendo, respectivamente, a quantidade de homens e mulheres da amostra
    """
    male = 0
    female = 0
    for item in data_list:
        gender = item['Gender']
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list: list) -> str:
    """
    Função que calcula qual é o gênero com maior número de ocorrências
    :param data_list:
        data_list: lista contendo as amostras para extração dos dados
    :return:
        Uma string contendo apenas um dos valores: 'Male', 'Female' ou 'Equal'
    """
    array_genders = count_gender(data_list)
    male, female = array_genders
    if male > female:
        answer = 'Male'
    elif female > male:
        answer = 'Female'
    else:
        answer = 'Equal'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
def count_user_types(data_list: list) -> list:
    """
    Função para contar a quantidade de usuário dado 2 tipos
    :param data_list:
        data_lista: lista contendo as amostras para extração dos dados
    :return:
        Uma lista contendo, respectivamente, as quantidades de assinantes e clientes.
    """
    subscribers = 0
    customers = 0
    for item in data_list:
        if item == 'Subscriber':
            subscribers += 1
        elif item == 'Customer':
            customers += 1
    return [subscribers, customers]

print("\nTAREFA 7: Verifique o gráfico!")
user_types_list = column_to_list(data_list, -3)
quantity = count_user_types(user_types_list)
types = ['Subscriber', 'Customer']
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.xticks(y_pos, types)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.title('Quantidade por tipo de usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A condição é false porque existem registros que possuem o campo 'Gênero' vazio"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
trip_duration_list = column_to_list(data_list, 2) #acessa a 3a coluna da lista
new_list =[int(i) for i in trip_duration_list] #transforma todos os items da lista em inteiros e retorna uma nova lista
new_list.sort() #ordena a lista para facilitar o calculo da mediana
max_trip = new_list[-1]
min_trip = new_list[0]
mean_trip = sum(new_list)/len(new_list)
if len(new_list) % 2 == 1: #se o número de elementos for impar
    index = (len(new_list))/2
    median_trip = new_list[int(index)]
else: #se o número de elementos for par
    index1, index2 = (len(new_list) / 2) - 1, len(new_list) / 2
    value1, value2 = new_list[int(index1)], new_list[int(index2)]
    median_trip = (value1 + value2)/2

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set()
start_stations_list = column_to_list(data_list,3)
for stations in start_stations_list:
    #como a estrutura de set não permite elementos duplicados
    #não precisamos fazer a verificação se o elemento já existe no conjunto, apenas adiciona-lo
    start_stations.add(stations)
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# Utilizei o formato em inglês para documentar as funções

input("Aperte Enter para continuar...")

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos

print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list: list) -> list:
    """
    Função para contar items de uma lista, sem a necessidade de especificar qual o dominio
    do conjunto de dados
    :param column_list:
        colum_list: lista que contém os dados para serem analisados
    :return:
        Retorna uma lista contendo, respectivamentes, os tipos de dados e a quantidade de vezes que cada um aparece
    """
    item_dict = dict() #crio um dicionário para me auxiliar
    for item in column_list:
        if item in item_dict: #se a chave já existe no dicionário acrescento 1 em seu valor
            item_dict[item] += 1
        else: #se a chave não existe no dicionário, crio ela com o valor de 1
            item_dict[item] = 1

    item_types = list(item_dict.keys()) #lista de chaves do dicionários
    count_items = list(item_dict.values()) #lista de valores do dicionário

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
