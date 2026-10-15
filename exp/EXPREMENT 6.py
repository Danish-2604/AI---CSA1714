import random

def run_vacuum_world():
    # Initialize locations and their status ('DIRTY' or 'CLEAN')
    locations = ['A', 'B']
    environment = {
        'A': random.choice(['DIRTY', 'CLEAN']),
        'B': random.choice(['DIRTY', 'CLEAN'])
    }
    
    # Random initial position of the vacuum cleaner
    agent_location = random.choice(locations)
    
    print("=== Vacuum Cleaner World Setup ===")
    print(f"Initial status: Room A = {environment['A']}, Room B = {environment['B']}")
    print(f"Agent starting position: Room {agent_location}\n")
    
    cost = 0  # Track number of actions taken
    
    # Run loop until both rooms are clean
    while environment['A'] == 'DIRTY' or environment['B'] == 'DIRTY':
        print(f"Agent is at Room {agent_location}.")
        
        # Action 1: If current room is dirty, clean it
        if environment[agent_location] == 'DIRTY':
            print(f"--> Room {agent_location} is dirty. Cleaning now...")
            environment[agent_location] = 'CLEAN'
            cost += 1
            print(f"--> Room {agent_location} is now clean.\n")
        
        # Action 2: Move to the other room if current room is clean
        else:
            print(f"--> Room {agent_location} is already clean.")
            if agent_location == 'A':
                agent_location = 'B'
                print("--> Moving Right to Room B.\n")
            else:
                agent_location = 'A'
                print("--> Moving Left to Room A.\n")
            cost += 1

    print("=== Cleaning Complete ===")
    print(f"Final status: Room A = {environment['A']}, Room B = {environment['B']}")
    print(f"Total actions taken: {cost}")

if __name__ == "__main__":
    run_vacuum_world()
