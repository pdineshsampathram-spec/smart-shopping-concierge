def search_products(query):
    sample_products = [
        {"name": "Sony WH-1000XM4", "price": 198, "rating": 4.7},
        {"name": "Bose QuietComfort 45", "price": 210, "rating": 4.6},
        {"name": "Sennheiser Momentum 4", "price": 199, "rating": 4.5},
        {"name": "JBL Tune 760NC", "price": 129, "rating": 4.3}
    ]
    return sample_products


def compare_products(products):
    for p in products:
        p["value_score"] = p["rating"] / p["price"]
    return products


def calculator(a, b):
    return a + b


def summarizer(text):
    return text[:200]


def search(query):
    return f"Search results for: {query}"
