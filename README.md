# Teste de Conhecimento - Roit-Bank

A partir do dataset [Heart Failure Clinical Data](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data) foi feita uma análise e criado um modelo de classificação que compara cinco modelos de machine learning (Logistic Regression, Support Vector, K-Nearest Neighbors, Decision Tree e Random Forest). Usando aquele com maior precisão foi feita uma API que recebe arquivos JSON com os parâmetros do paciente e retorna se irá sobreviver ou não, tanto o dado de entrada e saída são salvos em um banco de dados. Também foi criado o Dockerfile para encapsular a API.

## Instalação
É possível utilizar o arquivo requirements.txt para instalar os pacotes necessários para o api.py e modeling.ipynb.

```bash
pip install -r requirements.txt
```
## Uso
É necessário inicializar a API.

```bash
python api.py
```

A API tem **POST** e **GET** implementados, foi utilizado o Postman para testes e o link é localhost:5000/api.

Um exemplo de um JSON de entrada, via **POST**:
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

E para o **GET** temos esse retorno:
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

