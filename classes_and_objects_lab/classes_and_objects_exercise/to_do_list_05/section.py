from pythonProject.python_oop.classes_and_objects_lab.classes_and_objects_exercise.to_do_list_05.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        for section_task in self.tasks:
            if section_task.name == task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for task in self.tasks:
            result += "\n" + task.details()
        return result

