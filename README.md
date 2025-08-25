<!--# Análise de Dados do E-commerce Brasileiro (Olist)

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📄 Sobre o Projeto

[cite_start]Este projeto consiste em uma Análise Exploratória de Dados (EDA) completa sobre um conjunto de dados público de e-commerce brasileiro da Olist[cite: 14]. [cite_start]O objetivo é extrair insights acionáveis sobre o comportamento dos clientes, performance de vendas e eficiência logística, demonstrando o processo de análise de dados do início ao fim[cite: 4, 5].

[cite_start]Este é um projeto de portfólio que consolida habilidades em Python, Pandas, visualização de dados e storytelling[cite: 3, 9].

---

## 🎯 Principais Perguntas e Insights

[cite_start]A análise foi guiada para responder a perguntas de negócio chave, e os principais achados foram[cite: 56]:

* **Insight 1:** (Ex: A grande maioria da receita (75%) concentra-se na região Sudeste, mas a região Nordeste apresenta o maior tempo médio de entrega, impactando negativamente a satisfação do cliente.)
* **Insight 2:** (Ex: Existe uma forte sazonalidade nas vendas de categorias como 'cama_mesa_banho', com picos em maio e junho, sugerindo oportunidades para campanhas de marketing direcionadas.)
* **Insight 3:** (Ex: Atrasos na entrega superiores a 7 dias estão diretamente correlacionados a uma queda drástica nas notas de avaliação (de 4.5 para 1.8, em média).)

*(Esta seção será a última a ser preenchida, com os seus achados mais impactantes)*

---

## 🛠️ Ferramentas Utilizadas

* **Linguagem:** `Python`
* **Bibliotecas:** `Pandas`, `Matplotlib`, `Seaborn`, `Scikit-learn`, `Kaggle API`
* **Ambiente:** `Jupyter Lab`, `Visual Studio Code`
* **Controle de Versão:** `Git` & `GitHub`

---

## 📂 Estrutura do Repositório

O projeto está organizado de forma modular para garantir clareza e reprodutibilidade:

├── data/
│   ├── raw/          <- Dados brutos originais (baixados via script)
│   └── processed/    <- Dados limpos e amostra para análise
├── notebooks/
│   ├── 00_setup_and_load.ipynb       <- Carga, junção e salvamento inicial
│   ├── 01_cleaning_feature_engineering.ipynb <- Limpeza e criação de features
│   ├── 02_eda_kpis_visuals.ipynb     <- Análise Exploratória e KPIs
│   ├── 03_customers_rfm_reviews.ipynb <- Análise de Clientes (RFM) e Reviews
│   ├── 04_modeling_forecasting.ipynb <- Modelagem Preditiva (opcional)
│   └── 05_final_report_for_recruiter.ipynb <- Relatório final narrativo
├── outputs/
│   └── figures/      <- Gráficos e visualizações salvas
├── scripts/
│   └── download_data.py <- Script para baixar os dados do Kaggle
├── src/
│   ├── data_utils.py   <- Funções para carregar e salvar dados
│   ├── features.py     <- Funções para engenharia de features
│   └── viz.py          <- Funções para criar visualizações
├── .gitignore
├── README.md           <- Este arquivo
├── requirements.txt    <- Lista de dependências do projeto
└── run_all.sh          <- Script para gerar o relatório HTML final

---
## 🚀 Como Executar o Projeto

Siga as instruções abaixo para configurar e executar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/projeto-olist-portfolio.git](https://github.com/SEU-USUARIO/projeto-olist-portfolio.git)
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

## ✍️ Autor

* **Lucas Ker Soares Dias**
* **LinkedIn:** `https://www.linkedin.com/in/seu-perfil`
* **GitHub:** `https://github.com/SEU-USUARIO`

-->