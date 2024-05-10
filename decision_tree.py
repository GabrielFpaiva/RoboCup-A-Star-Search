from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dados para treinamento e teste do algoritmo de árvore de decisão
X_train = [
    [10, 20, 30, 25, 35], 
    [5, 15, 25, 20, 40],  
    [12, 18, 35, 22, 45],  
    [8, 22, 28, 18, 38],   
    [15, 25, 40, 20, 50]   
]

y_train = ["Chutar", "Esperar", "Chutar", "Esperar", "Chutar"] 

# Criar e treinar o modelo de árvore de decisão
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Dados para prever a ação do jogador
X_test = [
    [10, 20, 30, 25, 35],  
    [5, 15, 25, 20, 40],   
    [5, 15, 25, 20, 40]    
]

# Fazer previsões
predictions = model.predict(X_test)

# Exibir previsões
for i, pred in enumerate(predictions):
    print(f"Para a instância {i+1}, a ação do jogador prevista é: {pred}")
