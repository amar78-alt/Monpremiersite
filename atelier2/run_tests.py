"""Script pour exécuter un run depuis une tâche planifiée."""
import json
from atelier2.tester.runner import run_and_store

if __name__ == "__main__":
    print(json.dumps(run_and_store(), ensure_ascii=False, indent=2))
