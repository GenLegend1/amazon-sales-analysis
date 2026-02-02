import pandas as pd

def convert_dates(df):
    """Convert order_date to datetime and create date features."""
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['day_of_week'] = df['order_date'].dt.day_name()
    df['year_month'] = df['order_date'].dt.to_period('M').astype(str)
    return df


def calculate_discounts(df):
    """Recalculate discounted price and total revenue."""
    df['calculated_discounted_price'] = df['price'] * (1 - df['discount_percent'] / 100)
    df['calculated_total_revenue'] = df['calculated_discounted_price'] * df['quantity_sold']
    return df


def handle_missing_values(df):
    """Fill or drop missing values."""
    if 'rating' in df.columns:
        df['rating'] = df['rating'].fillna(df['rating'].median())
    if 'review_count' in df.columns:
        df['review_count'] = df['review_count'].fillna(0)
    df = df.dropna(subset=['price', 'quantity_sold'])
    return df
