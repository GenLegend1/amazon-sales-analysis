def missing_values(df):
    """Return missing values per column."""
    return df.isnull().sum()


def summarize_numeric(df):
    """Return descriptive statistics for numeric columns."""
    return df.describe()


def revenue_by_category(df):
    """Group revenue by product category."""
    return df.groupby('product_category')['total_revenue'].sum().sort_values(ascending=False)


def revenue_by_region(df):
    """Group revenue by customer region."""
    return df.groupby('customer_region')['total_revenue'].sum().sort_values(ascending=False)
