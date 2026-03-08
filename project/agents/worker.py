from project.tools.tools import search_products, compare_products

class Worker:
    def __init__(self):
        pass

    def execute(self, plan):
        intent = plan["intent"]
        query = intent["query"]

        products = search_products(query)
        compared = compare_products(products)

        return {
            "products": compared
        }
