# 1. Gerenciador de Tarefas Melhorado
import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description, deadline):
        task = {'description': description, 'deadline': deadline, 'completed': False}
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x['deadline'])
        for t in sorted_tasks:
            status = '✅' if t['completed'] else '❌'
            print(f"{status} {t['description']} (Prazo: {t['deadline']})")

    def mark_completed(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
        self.save_tasks()