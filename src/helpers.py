def format_currency(x):
    """Format numbers as currency."""
    return f"${x:,.2f}"


def add_path():
    """Add src folder to Python path."""
    import sys
    sys.path.append('../src')
