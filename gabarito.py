#import pandas as pd
#tabela = pd.read_csv("clientes.csv") # importa a base de dados
#display(tabela)

# verificar se temos valores vazios ou valores reconhecidos em formato errado
#print(tabela.info())
#print(tabela.columns)

#from sklearn.preprocessing import LabelEncoder
# vai transformar as colunas de texto em números, ex: profissoes vai sair de cientista, professor, mecanico, etc para 0, 1, 2, etc
#codificador = LabelEncoder()

# só não aplicamos na coluna de score_credito que é o nosso objetivo
#for coluna in tabela.columns:
    #if tabela[coluna].dtype == "object" and coluna != "score_credito":
        #tabela[coluna] = codificador.fit_transform(tabela[coluna])

# verificando se realmente todas as colunas foram modificadas
#print(tabela.info())
# escolhendo quais colunas vamos usar para treinar o modelo
# y é a coluna que queremos que o modelo calcule
# x vai todas as colunas que vamos usar para prever o score de credito, não vamos usar a coluna id_cliente porque ela é um numero qualquer que nao ajuda a previsao
#x = tabela.drop(["score_credito", "id_cliente"], axis=1)
#y = tabela["score_credito"]

#from sklearn.model_selection import train_test_split

# separamos os dados em treino e teste. Treino vamos dar para os modelos aprenderem e teste vamos usar para ver se o modelo aprendeu corretamente
#x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

#from sklearn.ensemble import RandomForestClassifier
#from sklearn.neighbors import KNeighborsClassifier

#modelo_arvore = RandomForestClassifier() # modelo arvore de decisao
#modelo_knn = KNeighborsClassifier() # modelo do KNN (nearest neighbors - vizinhos mais proximos)

# treinando os modelos
#modelo_arvore.fit(x_treino, y_treino)
#modelo_knn.fit(x_treino, y_treino)


# se o nosso modelo chutasse tudo "Standard", qual seria a acurácia do modelo?
#contagem_scores = tabela["score_credito"].value_counts()
#print(contagem_scores['Standard'] / sum(contagem_scores))

#from sklearn.metrics import accuracy_score

# calculamos as previsoes
#previsao_arvore = modelo_arvore.predict(x_teste)
#previsao_knn = modelo_knn.predict(x_teste.to_numpy())

# comparamos as previsoes com o y_teste
# esse score queremos o maior (maior acuracia, mas tb tem que ser maior do que o chute de tudo Standard)
#print(accuracy_score(y_teste, previsao_arvore))
#print(accuracy_score(y_teste, previsao_knn))

# fazendo novas previsões
#novos_clientes = pd.read_csv("novos_clientes.csv")
#display(novos_clientes)
#for coluna in novos_clientes.columns:
    #if novos_clientes[coluna].dtype == "object" and coluna != "score_credito":
        #novos_clientes[coluna] = codificador.fit_transform(novos_clientes[coluna])

#previsoes = modelo_arvore.predict(novos_clientes)
#print(previsoes)

# quais as caracteristicas mais importantes para definir o score de credito?
#colunas = list(x_teste.columns)
#importancia = pd.DataFrame(index=colunas, data=modelo_arvore.feature_importances_)
#importancia = importancia * 100
#print(importancia)