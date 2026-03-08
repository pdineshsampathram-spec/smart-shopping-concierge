class Evaluator:
    def __init__(self):
        pass

    def evaluate(self, worker_output):
        products = worker_output.get("products", [])

        if not products:
            return {"response": "No products found."}

        best = sorted(products, key=lambda x: (-x["rating"], x["price"]))[0]

        response = f"""
Top Recommendation:
{best['name']}

Price: ${best['price']}
Rating: {best['rating']}/5

Reason:
Best balance of price and rating among the searched products.
"""

        return {"response": response}
