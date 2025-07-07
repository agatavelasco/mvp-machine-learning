# 🔮 Previsão de Risco de Burnout no Ambiente de Trabalho

Este projeto é o MVP da pós-graduação em Engenharia de Software para Sistemas Inteligentes e tem como objetivo prever o **risco de burnout de profissionais** com base em fatores como hábitos de trabalho, saúde mental, equilíbrio vida-trabalho, produtividade, entre outros.

Trata-se de um **problema de classificação binária**, onde o modelo deve prever se um indivíduo apresenta **alto risco (1)** ou **baixo risco (0)** de burnout, a partir de variáveis numéricas e categóricas.

---

## 🎯 Objetivos Técnicos

- Realizar a análise exploratória e preparação dos dados do dataset: [Mental Health and Burnout in the Workplace](https://www.kaggle.com/datasets/khushikyad001/mental-health-and-burnout-in-the-workplace)
- Treinar e comparar diferentes algoritmos de machine learning para classificação
- Criar uma aplicação web full stack (backend Flask + frontend HTML/CSS/JS)
- Permitir que o modelo execute previsões com novos dados fornecidos pelo usuário
- Garantir a qualidade do modelo com testes automatizados via PyTest

---

## 🤖 Algoritmos Utilizados

Durante a fase de modelagem no notebook, foram aplicados e comparados os seguintes algoritmos clássicos de classificação, utilizando `Scikit-Learn`:

- **K-Nearest Neighbors (KNN)**
- **Árvore de Decisão**
- **Naive Bayes**
- **Support Vector Machine (SVM)**

O modelo com melhor desempenho (acurácia e generalização) foi escolhido e exportado como `burnout_model.pkl`.

---

## 🧰 Tecnologias e Bibliotecas

### 📊 Ciência de Dados e Machine Learning
- Python 3.x
- Pandas, NumPy
- Scikit-Learn
- Matplotlib e Seaborn (visualização)
- Joblib (para exportação do modelo)
- Google Colab (ambiente de desenvolvimento do notebook)

### 🧪 Testes Automatizados
- PyTest
- Scikit-Learn Metrics (accuracy_score)

### 🌐 Aplicação Web
- Flask (backend)
- HTML5, CSS3, JavaScript (frontend)

---


---

## 🚀 Como executar o projeto

### ✅ 1. Clonar o repositório

git clone https://github.com/agatavelasco/mvp-machine-learning.git
cd mvp-machine-learning/app

### ✅ 2. Instalar dependências
Crie um ambiente virtual e instale os pacotes:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r ../requirements.txt

### ✅ 3. Executar o servidor Flask

python server.py

O backend será iniciado em:

📍 http://127.0.0.1:5000/

### ✅ 4. Abrir o Frontend
Abra o arquivo index.html diretamente no navegador:

frontend/index.html

📌 Insira os dados no formulário e clique em "Prever Risco" para ver o resultado da predição.

### ✅ 5. Rodar os testes automatizados
No terminal:

python -m pytest test_model.py -v

✔ Verifica:

Carregamento do modelo

Formato das predições

Acurácia mínima em dados reais

### 🧠 Modelo de Machine Learning
O modelo foi treinado no Google Colab usando:

Scikit-Learn
Algoritmos: SVM, KNN, Naive Bayes, Árvore de Decisão
Pré-processamento com normalização
Comparação de desempenho entre modelos
Exportação final com joblib

### 🔍 Exemplos de input
Exemplo de payload JSON aceito pela API:

{
  "Age": 30,
  "Gender": 1,
  "YearsAtCompany": 5,
  "WorkHoursPerWeek": 45,
  "RemoteWork": 2,
  "BurnoutLevel": 6.5,
  "CommuteTime": 30,
  "HasMentalHealthSupport": 1,
  "ManagerSupportScore": 4.2,
  "HasTherapyAccess": 1,
  "MentalHealthDaysOff": 2,
  "WorkLifeBalanceScore": 6.0,
  "TeamSize": 10,
  "CareerGrowthScore": 7.5,
  "JobSatisfaction": 7.0,
  "PhysicalActivityHrs": 3.5,
  "ProductivityScore": 8.0,
  "SleepHours": 7.0,
  "StressLevel": 6.0
}

### 🛡️ Considerações de Segurança
Os dados são anônimos e públicos (fonte: Kaggle)

Nenhuma informação sensível é armazenada

O projeto pode ser estendido com autenticação e anonimização, conforme visto na disciplina de Desenvolvimento de Software Seguro
