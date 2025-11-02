# Brazilian E-Commerce Data Analysis (Olist)

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

**Leia este README em [Português (Brasil) 🇧🇷](README.pt-br.md).**

---

## 📄 About The Project

This project is an end-to-end analysis of the Olist e-commerce ecosystem, covering everything from data cleaning and Exploratory Data Analysis (EDA) to predictive modeling and customer segmentation (RFM and K-Means).

The objective is not just to explore the data, but to build a complete strategic diagnosis, identifying key operational bottlenecks (like logistics) and the greatest growth opportunities (like customer retention). The project culminates in the construction of a Machine Learning model that proactively identifies customers at risk of dissatisfaction.

This portfolio demonstrates skills in Python, Pandas, Feature Engineering, Predictive Modeling (Scikit-learn, Prophet), and data storytelling.

---

## 🎯 Key Questions and Insights

The analysis was guided by key business questions, and the main findings were:

**- Insight 1: It's Not the Delay, It's the Broken Promise.** Statistical analysis (notebook_02) proved that total delivery time is not the primary driver of dissatisfaction. The #1 factor is the **delivery delay** (difference between the estimated and actual delivery dates). Customers are satisfied with a long delivery, as long as the promise is kept.

**- Insight 2: 97.5% of Customers Buy Only Once.** RFM analysis and K-Means (notebook_03) revealed a "leaky bucket" business model. Olist is excellent at acquiring new customers but fails to retain them. The strategic challenge is not to increase the average ticket size, but to **foster the second purchase** and retain the "loyal elite" (2.5% of customers).

**- Insight 3: It's Possible to Predict 68% of Bad Reviews.** We built a Random Forest model (notebook_04) that successfully predicts which orders will receive a 1 or 2-star rating. This model has a **Recall of 68%**, allowing Olist to shift from reactive to proactive customer service, saving dissatisfied customers before they even leave a review.

**- Insight 4: Daily Sales Forecasting is Unreliable.** Our forecasting attempt (notebook_04) proved that high daily volatility and limited historical data (less than 2 years) make daily forecasting inaccurate. The Prophet model did not outperform a simple naive baseline (MAE of 24.37% vs 25.56%). The recommendation is to use **monthly forecasts** for strategic planning.

---

## 🛠️ Tools & Stack

**- Language:** Python
**- Data Analysis:** Pandas
**- Visualization:** Matplotlib, Seaborn
**- Machine Learning:** Scikit-learn, Prophet (fbprophet), Imbalanced-learn (imblearn)
**- Statistical Analysis:** Statsmodels
**- Environment:** Jupyter Lab, Visual Studio Code
**- Other:** Kaggle API, Git & GitHub

---

## 📂 Repository Structure

The project is organized modularly to ensure clarity and reproducibility:

├── data/
│   ├── raw/          <- Raw original data (downloaded via script)
│   └── processed/    <- Cleaned and processed data
├── notebooks/
│   ├── 00_setup_and_load.ipynb       <- Load, merge, and initial save
│   ├── 01_cleaning_feature_engineering.ipynb <- Cleaning and feature engineering
│   ├── 02_eda_kpis_statistical_tests.ipynb <- Exploratory Analysis, KPIs, and Statistical Tests
│   ├── 03_customer_segmentation_rfm_kmeans.ipynb <- RFM Segmentation and Clustering
│   ├── 04_forecasting_predictive_modeling.ipynb <- Forecasting and Classification Model
│   └── 05_final_report_executive_summary.ipynb <- Final narrative report / executive summary
├── outputs/
│   └── figures/      <- Saved charts and visualizations
├── scripts/
│   └── download_data.py <- Script to download data from Kaggle
├── src/
│   ├── data_utils.py   <- Functions for loading/saving data (optional)
│   ├── features.py     <- Functions for feature engineering (optional)
│   └── viz.py          <- Functions for creating visualizations (optional)
├── .gitignore
├── README.md           <- This file
├── README.pt-br.md     <- Portuguese version of the README
├── requirements.txt    <- Project dependency list

---
## 🚀 How to Run This Project

Follow the instructions below to set up and run the project locally.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Lucas-Ker/olist-data-analysis-project.git](https://github.com/Lucas-Ker/olist-data-analysis-project.git)
    cd olist-data-analysis-project
    ```
    *(Nota: Ajustei o nome da pasta `projeto-olist-portfolio` para o nome real do seu repo `olist-data-analysis-project`)*

2.  **Create and activate the virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Get the Data**

    You need the raw data files in the `data/raw` folder. Choose one of the options below.

    <details>
    <summary><strong>Option 1: Via Script (Recommended)</strong></summary>

    This method uses the Kaggle API to download and unzip the data automatically.

    * **a.** Download your `kaggle.json` API token from the 'API' section of your Kaggle account.
    * **b.** Create a `.kaggle` folder in your home directory (`mkdir -p ~/.kaggle`).
    * **c.** Move the file to that folder (`mv ~/Downloads/kaggle.json ~/.kaggle/`) and set permissions (`chmod 600 ~/.kaggle/kaggle.json`).
    * **d.** Run the download script:
        ```bash
        python scripts/download_data.py
        ```
    </details>

    <details>
    <summary><strong>Option 2: Manual Download (Alternative)</strong></summary>

    If you prefer not to use the API, you can download the data manually.

    * **a.** Go to the dataset page on Kaggle: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
    * **b.** Click the "Download" button to get the `brazilian-ecommerce.zip` file.
    * **c.** Unzip the file.
    * **d.** Copy all `.csv` files into the `data/raw/` folder of this project.
    </details>

5.  **Run the Jupyter notebooks:**
    * Start Jupyter Lab:
        ```bash
        jupyter lab
        ```
    * Open and run the notebooks in numerical order, starting with `notebooks/00_setup_and_load.ipynb`.

---

## 📈 Next Steps and Future Improvements

While this project provides a complete strategic diagnosis, data analysis is an iterative process. The following steps could add even more value to the business:

1.  **Text Analysis (NLP) of Bad Reviews:**
    While our model predicts *which* customers will be dissatisfied, it doesn't explain *why* (beyond logistics). The next step would be to use Natural Language Processing (NLP) on the comments of 1 and 2-star reviews to identify product-related root causes (e.g., "broken product," "wrong color," "misleading description").

2.  **Implementation of Monthly Sales Forecasting:**
    We proved that daily forecasting is unfeasible. A valuable next step would be to aggregate the data at a **monthly** level and train a new Prophet model. A reliable monthly forecast would smooth out daily noise and provide real strategic value for inventory and financial planning.

---

## ✍️ Author

* **Lucas Ker Soares Dias**
* **LinkedIn:** `https://www.linkedin.com/in/lucas-ker/`
* **GitHub:** `https://github.com/Lucas-Ker`
