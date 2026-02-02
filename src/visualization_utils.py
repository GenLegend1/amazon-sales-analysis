import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_revenue(df):
    daily = df.groupby('order_date')['total_revenue'].sum().reset_index()
    plt.figure(figsize=(12, 5))
    plt.plot(daily['order_date'], daily['total_revenue'])
    plt.title('Daily Total Revenue Over Time')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_monthly_revenue(df):
    monthly = df.groupby('year_month')['total_revenue'].sum().reset_index()
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=monthly, x='year_month', y='total_revenue', marker='o')
    plt.title('Monthly Total Revenue')
    plt.xlabel('Year-Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_category_sales(df):
    category_sales = df.groupby('product_category')['total_revenue'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=category_sales.index, y=category_sales.values)
    plt.title('Total Revenue by Product Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
