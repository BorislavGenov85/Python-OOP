from pythonProject.python_oop.encapsulation_lab.encapsulation_exercise.wild_cat_zoo_01.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money = 0
        for worker in self.workers:
            money += worker.salary

        if money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money = 0
        for animal in self.animals:
            money += animal.money_for_care
        if money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_iterable_str(self.animals, "Lion")
        result += self.__build_iterable_str(self.animals, "Tiger")
        result += self.__build_iterable_str(self.animals, "Cheetah")
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__build_iterable_str(self.workers, "Keeper")
        result += self.__build_iterable_str(self.workers, "Caretaker")
        result += self.__build_iterable_str(self.workers, "Vet")
        return result.strip()

    def __build_iterable_str(self, iterable, iterable_type):
        counter = 0
        result = ""
        for obj in iterable:
            if obj.__class__.__name__ == iterable_type:
                counter += 1
                result += repr(obj) + '\n'
        return f"----- {counter} {iterable_type}s:\n" + result
