from project.main_agent import run_agent

def start_app():
    print("Smart Shopping Concierge")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = run_agent(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    start_app()
