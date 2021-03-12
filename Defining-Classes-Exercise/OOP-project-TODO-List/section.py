from Library.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []


    def add_task(self, task: Task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"


    def complete_task(self, task_name):
        tasks = [p for p in self.tasks if p.name == task_name]
        if tasks:
            tasks[0].completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"


    def clean_section(self):
        new_tasks = [p for p in self.tasks if p.completed != True]
        cleared_tasks = len(self.tasks) - len(new_tasks)
        self.tasks = new_tasks
        return f"Cleared {cleared_tasks} tasks."


    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details()+"\n"
        return result




