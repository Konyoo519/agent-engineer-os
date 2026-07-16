import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import agent

if __name__ == '__main__':
    goal = 'Please read the file tools.py using the read_file tool and tell me what you find'
    print(f'[start] goal = {goal}')
    final = agent.run(goal)
    print(f'[final] {final}')