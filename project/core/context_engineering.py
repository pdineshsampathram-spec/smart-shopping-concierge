def build_planner_context(user_input, memory):
    return {
        "user_input": user_input,
        "history": memory.get_history(),
        "preferences": memory.get_preferences()
    }


def build_worker_context(plan):
    return {
        "plan": plan
    }


def build_evaluator_context(worker_output):
    return {
        "worker_output": worker_output
    }
