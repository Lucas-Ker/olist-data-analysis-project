# Análise de Dados do E-commerce Brasileiro (Olist)

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

**Read this README in [English 🇺🇸](README.md).**

## 📄 Sobre o Projeto

Este projeto é uma análise de ponta a ponta do ecossistema de e-commerce da Olist, indo desde a limpeza de dados e Análise Exploratória (EDA) até a modelagem preditiva e segmentação de clientes (RFM e K-Means).

O objetivo não é apenas explorar os dados, mas construir um diagnóstico estratégico completo, identificando os principais gargalos operacionais (como logística) e as maiores oportunidades de crescimento (como retenção de clientes). O projeto culmina na construção de um modelo de Machine Learning que identifica proativamente clientes em risco de insatisfação.

Este portfólio demonstra habilidades em Python, Pandas, Engenharia de Features, Modelagem Preditiva (Scikit-learn, Prophet) e storytelling de dados.

---

## 🎯 Principais Perguntas e Insights

A análise foi guiada para responder a perguntas de negócio chave, e os principais achados foram:

**- Insight 1:** O problema não é a demora, é a promessa quebrada. A análise estatística (notebook_02) provou que o tempo total de entrega não é o principal motor de insatisfação. O fator nº 1 é o **atraso na entrega** (diferença entre o estimado e o real). Clientes ficam satisfeitos com uma entrega longa, desde que o prazo seja cumprido.

**- Insight 2:** **97.5% dos clientes compram apenas uma vez**. A análise RFM e o K-Means (notebook_03) revelaram um modelo de negócio de "balde furado". A Olist é excelente em adquirir novos clientes, mas falha em retê-los. O desafio estratégico não é aumentar o ticket médio, mas sim fomentar a segunda compra e reter a "elite leal" de 2.5% dos clientes.

**- Insight 3:** **É possível prever 68% das avaliações ruins**. Construímos um modelo de Random Forest (notebook_04) que prevê com sucesso quais pedidos receberão uma nota 1 ou 2. Este modelo tem um Recall de 68%, permitindo que a Olist mude de um atendimento reativo para um atendimento ao cliente proativo, salvando clientes insatisfeitos antes que eles deixem a avaliação.

**- Insight 4:** **Previsão diária de vendas não é confiável**. Nossa tentativa de forecasting (notebook_04) provou que a alta volatilidade diária e os dados históricos limitados (menos de 2 anos) tornam a previsão diária imprecisa. O modelo Prophet não superou um baseline ingênuo (MAE de 24.37% vs 25.56%). A recomendação é usar previsões mensais para planejamento estratégico.

---

## 🛠️ Ferramentas Utilizadas

**- Linguagem:** Python

**- Análise de Dados:** Pandas

**- Visualização:** Matplotlib, Seaborn

**- Machine Learning:** Scikit-learn, Prophet (fbprophet), Imbalanced-learn (imblearn)

**- Análise Estatística:** Statsmodels

**- Ambiente:** Jupyter Lab, Visual Studio Code

**- Outros:** Kaggle API, Git & GitHub

---

## 📂 Estrutura do Repositório

O projeto está organizado de forma modular para garantir clareza e reprodutibilidade:

```

├── data/
│   ├── raw/          <- Dados brutos originais (baixados via script)
│   └── processed/    <- Dados limpos e processados
├── notebooks/
│   ├── 00_setup_and_load.ipynb             <- Carga, junção e salvamento inicial
│   ├── 01_cleaning_feature_engineering.ipynb <- Limpeza e engenharia de features
│   ├── 02_eda_kpis_statistical_tests.ipynb <- Análise Exploratória, KPIs e Testes Estatísticos
│   ├── 03_customer_segmentation_rfm_kmeans.ipynb <- Segmentação RFM e Clusterização
│   ├── 04_modeling_forecasting.ipynb       <- Forecasting e Modelo de Classificação
│   └── 05_final_report_executive_summary.ipynb <- Relatório final narrativo
├── outputs/
│   └── figures/      <- Gráficos e visualizações salvas
├── scripts/
│   └── download_data.py <- Script para baixar os dados do Kaggle
├── src/
│   ├── data_utils.py <- Funções para carregar e salvar dados (opcional)
│   ├── features.py   <- Funções para engenharia de features (opcional)
│   └── viz.py        <- Funções para criar visualizações (opcional)
├── .gitignore
├── README.md         <- Este arquivo
└── requirements.txt  <- Lista de dependências do projeto

```

---
## 🚀 Como Executar o Projeto

Siga as instruções abaixo para configurar e executar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Lucas-Ker/olist-data-analysis-project.git](https://github.com/Lucas-Ker/olist-data-analysis-project.git)
    cd projeto-olist-portfolio
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Obtenha os Dados**

    Você precisa dos arquivos de dados brutos na pasta `data/raw`. Escolha uma das opções abaixo.

    <details>
    <summary><strong>Opção 1: Via Script (Recomendado)</strong></summary>

    Este método usa a API do Kaggle para baixar e descompactar os dados automaticamente.

    * **a.** Faça o download do seu token `kaggle.json` na seção 'API' da sua conta no Kaggle.
    * **b.** Crie uma pasta `.kaggle` no seu diretório home (`mkdir -p ~/.kaggle`).
    * **c.** Mova o arquivo para essa pasta (`mv ~/Downloads/kaggle.json ~/.kaggle/`) e ajuste as permissões (`chmod 600 ~/.kaggle/kaggle.json`).
    * **d.** Execute o script de download:
        ```bash
        python scripts/download_data.py
        ```
    </details>

    <details>
    <summary><strong>Opção 2: Download Manual (Alternativa)</strong></summary>

    Se preferir não usar a API, você pode baixar os dados manualmente.

    * **a.** Vá para a página do dataset no Kaggle: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
    * **b.** Clique no botão "Download" para baixar o arquivo `brazilian-ecommerce.zip`.
    * **c.** Descompacte o arquivo.
    * **d.** Copie todos os arquivos `.csv` para a pasta `data/raw/` deste projeto.
    </details>

5.  **Execute os notebooks Jupyter:**
    * Inicie o Jupyter Lab:
        ```bash
        jupyter lab
        ```
    * Abra e execute os notebooks na ordem numérica, começando por `notebooks/00_setup_and_load.ipynb`. O projeto pode ser avaliado rapidamente usando apenas o arquivo de amostra, mas para rodar a análise completa, os dados brutos são necessários.


---

## 📈 Próximas Etapas e Melhorias Futuras

Embora este projeto forneça um diagnóstico estratégico completo, a análise de dados é um processo iterativo. As seguintes etapas poderiam agregar ainda mais valor ao negócio:

1. **Análise de Texto (NLP) das Avaliações Ruins:** Enquanto nosso modelo prevê *quais* clientes ficarão insatisfeitos, ele não explica o *porquê* (além da logística). O próximo passo seria usar Processamento de Linguagem Natural (NLP) nos comentários das avaliações de 1 e 2 estrelas para identificar as causas-raiz da insatisfação relacionadas ao produto (ex: "produto quebrado", "cor errada", "descrição enganosa").

2. **Implementação da Previsão Mensal de Vendas:** Nós provamos que o forecasting diário é inviável. Uma próxima etapa valiosa seria agregar os dados em nível **mensal** e treinar um novo modelo Prophet. Uma previsão mensal confiável suavizaria o ruído diário e forneceria um valor estratégico real para o planejamento de inventário e financeiro.



---

## ✍️ Autor

* **Lucas Ker Soares Dias**
* **LinkedIn:** [`https://www.linkedin.com/in/lucas-ker/`](https://www.linkedin.com/in/lucas-ker/)
* **GitHub:** [`https://github.com/Lucas-Ker`](https://github.com/Lucas-Ker)

