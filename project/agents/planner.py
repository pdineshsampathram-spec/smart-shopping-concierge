class Planner:
    def __init__(self):
        pass

    def create_plan(self, user_input, memory):
        intent = {
            "query": user_input,
            "category": "product_search",
            "budget": None
        }

        plan = {
            "tasks": [
                "search_products",
                "compare_products",
                "rank_products"
            ],
            "intent": intent
        }

        return plan
