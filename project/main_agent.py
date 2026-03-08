from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.memory.session_memory import SessionMemory
from project.core.context_engineering import build_planner_context
from project.core.observability import Logger

class MainAgent:
    def __init__(self):
        self.planner = Planner()
        self.worker = Worker()
        self.evaluator = Evaluator()
        self.memory = SessionMemory()
        self.logger = Logger()

    def handle_message(self, user_input: str):
        self.logger.log("USER", user_input)

        self.memory.add_message(user_input)

        planner_context = build_planner_context(user_input, self.memory)

        plan = self.planner.create_plan(user_input, self.memory)
        self.logger.log("PLANNER", str(plan))

        worker_output = self.worker.execute(plan)
        self.logger.log("WORKER", str(worker_output))

        evaluation = self.evaluator.evaluate(worker_output)
        self.logger.log("EVALUATOR", str(evaluation))

        return evaluation


def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
