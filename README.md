# Multi-source Retail Data Integration Hub

## 📌 Project Overview
The **Multi-source Retail Data Integration Hub** is an end-to-end ETL (Extract, Transform, Load) pipeline that integrates **retail datasets from Kaggle** into a structured **MySQL data warehouse**. This hub enables **data-driven decision-making** through interactive dashboards and insightful analytics.

## 🛠️ Technologies Used
- **Python** 🐍 (for ETL, data processing, and visualization)
- **SQL** (for data transformation and warehouse structuring)
- **MySQL** 🗄️ (as the primary database for storing processed data)
- **Pandas** 📊 (for data manipulation and cleaning)
- **Matplotlib & Plotly** 📈 (for data visualization)
- **Streamlit** 🚀 (for building interactive dashboards)
- **Git** 🔄 (for version control and collaboration)
- **🔌PyMySQL** (Connects Python scripts to MySQL for database interactions)
- **🔗 MySQL Connector** (Alternative MySQL connection library for seamless queries)

## 🏗️ ETL Pipeline Workflow
1. **Extract** 📥
   - Load raw data from Kaggle CSV files
2. **Transform** 🔄
   - Data cleansing (handling nulls, duplicates, inconsistencies)
   - Aggregation of key metrics (sales, revenue, product performance)
   - Implementation of **Slowly Changing Dimension Type 2 (SCD Type 2)** for historical tracking
3. **Load** 📤
   - Store transformed data into a **MySQL data warehouse**

## 📊 Data Warehouse Design
- **Fact Table**
  - `fact_orders`
- **Dimension Tables**
  - `dim_products`
  - `dim_customers`
  - `dim_dates`
  - `dim_payments`
  - `dim__sellers`
  - **Data marts Tables**
  - `dm_product_category`
  - `dm_sales_performence`
  - `dm_sales_trends`

## 🌟 Streamlit Dashboard Features
### 📌 Sidebar Navigation
- 🎯 **Sales Performance**: State-wise revenue analysis
- 📦 **Product Analysis**: Revenue breakdown by product category
- 📊 **Aggregation**: Daily, monthly, and category-wise revenue trends
- 📑 **Business Metrics**: KPI insights from `business_metrics_view`
- 📆 **Date-Based Trends**: Time-series analysis of sales trends

### 📊 Key Visualizations
- **Bar Charts** (State-wise revenue, Business KPIs)
- **Treemaps** (Revenue by product category)
- **Line & Area Charts** (Sales trends over time)
- **Scatter Plots** (Daily sales variations)

## 🚀 How to Run the Project
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo-url.git
cd multi-source-retail-hub
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Set Up MySQL Database
- Create a MySQL database (`Project_db`)
- Load pre-processed data using `data_loader.py`

### 4️⃣ Run the Streamlit Dashboard
```bash
streamlit run app.py
```

## 📢 Contributions & Feedback
We welcome contributions! Feel free to submit **issues, pull requests, or feature suggestions**.

🔗 **Developed by Ram Mishra** 🚀

