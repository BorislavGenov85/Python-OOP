from pythonProject.python_oop.static_and_class_methods_lab.static_and_class_methods_exercise.document_management_03.category import Category
from pythonProject.python_oop.static_and_class_methods_lab.static_and_class_methods_exercise.document_management_03.document import Document
from pythonProject.python_oop.static_and_class_methods_lab.static_and_class_methods_exercise.document_management_03.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        storage_category = self.__find_category_by_id(category.id)
        if storage_category is None:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        storage_topic = self.__find_topic_by_id(topic.id)
        if storage_topic is None:
            self.topics.append(topic)

    def add_document(self, document: Document):
        storage_document = self.__find_document_by_id(document.id)
        if storage_document is None:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        current_category = [c for c in self.categories if c.id == category_id][0]
        current_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = [t for t in self.topics if t.id == topic_id][0]
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = [d for d in self.documents if d.id == document_id][0]
        current_document.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(current_document)

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.documents])

    def __find_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def __find_topic_by_id(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def __find_document_by_id(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document
