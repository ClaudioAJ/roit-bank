# Teste de Conhecimento - Roit-Bank

A partir do dataset [Heart Failure Clinical Data](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) foi feita uma análise e criado um modelo de classificação que compara cinco modelos de machine learning (**modeling.ipynb**), sendo eles: Logistic Regression, Support Vector, K-Nearest Neighbors, Decision Tree e Random Forest. Usando aquele com maior precisão foi criada uma API (**api.py**) que recebe arquivos JSON com os parâmetros do paciente e retorna se irá sobreviver ou não, tanto os dados de entrada e o de saída são salvos em um banco de dados (**pacientes.bd**). Também foi criado o **Dockerfile** para encapsular a API.

## Instalação
É possível utilizar o arquivo requirements.txt para instalar os pacotes necessários para o api.py e modeling.ipynb.

```bash
pip install -r requirements.txt
```

## Uso
#### **-> Modeling.ipynb**

O uso desse arquivo é via jupyter notebook.

#### **-> API.py**

```bash
python api.py
```

A API tem os comandos **POST** e **GET** implementados, foi utilizado o Postman para testes.

O Link da API é: localhost:5000/api

Um exemplo de um JSON de entrada, via comando **POST**:
```json
[
    {"age": 15, "ejection_fraction": 44, "serum_creatinine": 3, "time": 200},
    {"age": 90, "ejection_fraction": 66, "serum_creatinine": 0.5, "time": 5}
]
```
O JSON de saída:
```json
{
    "Previsao": "['Sobreviveu', 'Morreu']"
}
```

E para o comando **GET** temos o retorno dos dados salvos no banco de dados, por exemplo:
```json
[
    {
        "age": 15,
        "death_event": 0,
        "ejection_fraction": 44,
        "id": 1,
        "serum_creatinine": 3.0,
        "time": 200
    },
    {
        "age": 90,
        "death_event": 1,
        "ejection_fraction": 66,
        "id": 2,
        "serum_creatinine": 0.5,
        "time": 5
    }
]
```

