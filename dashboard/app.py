import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px

# Database connection function
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Lakhan@123",
        database="Project_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# Function to fetch data from MySQL
def fetch_data(query):
    connection = get_connection()
    df = pd.DataFrame()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data)
    finally:
        connection.close()
    return df

# Streamlit App Layout
st.set_page_config(page_title="Multi-Source Integration Hub", layout="wide")
st.sidebar.title("🔗 Multi-Source Integration Hub")
st.sidebar.markdown("---")

# Sidebar Navigation
option = st.sidebar.radio("📌 Select Analysis:", [
    "🎯 Sales Performance",
    "📦 Product Analysis",
    "📊 Aggregation",
    "📑 Business Metrics",
    "📆 Date-Based Trends"
])

if option == "🎯 Sales Performance":
    st.title("📊 Sales Performance Analysis")
    if st.button("Fetch Sales Data"):
        df = fetch_data("SELECT * FROM dm_sales_performance ORDER BY total_revenue DESC LIMIT 20")
        st.dataframe(df)
        fig = px.bar(df, x='customer_state', y='total_revenue', color='total_revenue', 
                     title='State-wise Revenue', color_continuous_scale='sunset')
        st.plotly_chart(fig, use_container_width=True)

elif option == "📦 Product Analysis":
    st.title("📦 Product Category Analysis")
    if st.button("Fetch Product Data"):
        df = fetch_data("SELECT * FROM dm_product_category_analysis ORDER BY total_revenue DESC LIMIT 10")
        st.dataframe(df)
        fig = px.treemap(df, path=['product_category_name'], values='total_revenue', 
                         title='Revenue Contribution by Product Category', color='total_revenue',
                         color_continuous_scale='viridis')
        st.plotly_chart(fig, use_container_width=True)
        
        fig_pie = px.pie(df, names='product_category_name', values='total_revenue',
                         title='Revenue Share by Category', color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig_pie, use_container_width=True)

elif option == "📊 Aggregation":
    st.title("📈 Aggregated Data Analysis")
    selected_option = st.selectbox("Select Aggregation Type:", 
                                   ["Total Sales by Customer", "Revenue by Category", 
                                    "Monthly Sales Summary", "Daily Sales Summary"])
    if st.button("Fetch Aggregated Data"):
        if selected_option == "Daily Sales Summary":
            df = fetch_data("SELECT * FROM daily_sales_summary")
            st.dataframe(df)
        elif selected_option == "Monthly Sales Summary":
            df = fetch_data("SELECT * FROM monthly_sales_summary WHERE year=2017")
            st.dataframe(df)
            fig = px.area(df, x='month', y='total_revenue', title='Monthly Sales Trend', 
                          markers=True, color_discrete_sequence=['#33A1C9'])
            st.plotly_chart(fig, use_container_width=True)
        elif selected_option == "Revenue by Category":
            df = fetch_data("SELECT * FROM revenue_by_category")
            st.dataframe(df)
            fig = px.line(df, x='product_category_name', y='total_revenue', title='Revenue by Category',
                          markers=True, color_discrete_sequence=['#FF5733'])
            st.plotly_chart(fig, use_container_width=True)
        elif selected_option == "Total Sales by Customer":
            df = fetch_data("SELECT * FROM total_sales_by_customer")
            st.dataframe(df)

elif option == "📑 Business Metrics":
    st.title("📑 Business Metrics Overview")
    if st.button("Fetch Business Metrics"):
        df = fetch_data("SELECT * FROM business_metrics_view")
        st.dataframe(df)

        # Bar Chart for Business Metrics
        fig_bar = px.bar(df, x='metric_name', y='metric_value', text='metric_value',
                         title='📊 Business Metrics Breakdown',
                         color='metric_value', color_continuous_scale='viridis')
        st.plotly_chart(fig_bar, use_container_width=True)

        # Pie Chart for Business Metrics
        fig_pie = px.pie(df, names='metric_name', values='metric_value',
                         title="🎯 Business Metrics Distribution",
                         hole=0.3,  # Donut-style chart
                         color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig_pie, use_container_width=True)

        # Line Chart for Business Metrics Trend
        fig_line = px.line(df, x='metric_name', y='metric_value', 
                           title="📈 Business Metrics Trend Over Time",
                           markers=True, line_shape='spline',
                           color_discrete_sequence=['#FF4500'])
        st.plotly_chart(fig_line, use_container_width=True)

        # Scatter Plot with Vertical Lines
        fig_vline = px.scatter(df, x='metric_name', y='metric_value', size=[10]*len(df),
                               title="📌 Business Metrics with Vertical Lines",
                               color='metric_value', color_continuous_scale='bluered')

        # Adding vertical lines for each metric
        for metric in df['metric_name']:
            fig_vline.add_vline(x=metric, line_width=2, line_dash="dash", line_color="gray")

        st.plotly_chart(fig_vline, use_container_width=True)

elif option == "📆 Date-Based Trends":
    st.title("📆 Sales Trends Over Time")

    if st.button("Fetch Sales Trends"):
        df = fetch_data("SELECT * FROM date_sales_trends")

        st.subheader("📊 Data Preview")
        st.dataframe(df)

        # ✅ Convert `purchase_date_id` safely
        try:
            df['purchase_date_id'] = pd.to_datetime(df['purchase_date_id'], errors='coerce')
        except Exception as e:
            st.error(f"Error converting date: {e}")

        # ✅ Drop invalid date values
        df = df.dropna(subset=['purchase_date_id'])

        # 📈 Scatter Plot - Sales Trend Over Time (Only Points)
        st.subheader("📍 Sales Trend Over Time (Point Plot)")
        fig_scatter = px.scatter(df, x='purchase_date_id', y='total_sales',
                                 title='📍 Daily Sales Trend (Points Only)',
                                 labels={'purchase_date_id': 'Purchase Date', 'total_sales': 'Total Sales'},
                                 color_discrete_sequence=['#32CD32'])
        st.plotly_chart(fig_scatter, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.info("🚀 Developed by Ram Mishra")