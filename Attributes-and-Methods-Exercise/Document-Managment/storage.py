class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []


    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)


    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)


    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)


    def edit_category(self, category_id: int, new_name: str):
        category_to_edit = [c for c in self.categories if c.id == category_id]
        if category_to_edit:
            category_to_edit = category_to_edit[0]
            category_to_edit.name = new_name


    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_to_edit = [t for t in self.topics if t.id == topic_id]
        if topic_to_edit:
            topic_to_edit = topic_to_edit[0]
            topic_to_edit.storage_folder = new_storage_folder
            topic_to_edit.topic = new_topic


    def edit_document(self, document_id: int, new_file_name: str):
        document_to_edit = [d for d in self.documents if d.id == document_id]
        if document_to_edit:
            document_to_edit = document_to_edit[0]
        document_to_edit.file_name = new_file_name


    def delete_category(self, category_id):
        category_to_delete = [c for c in self.categories if c.id == category_id]
        if category_to_delete:
            self.categories.remove(category_to_delete[0])


    def delete_topic(self, topic_id):
        topic_to_delete = [t for t in self.topics if t.id == topic_id]
        if topic_to_delete:
            self.topics.remove(topic_to_delete[0])


    def delete_document(self, document_id):
        document_to_delete = [d for d in self.documents if d.id == document_id]
        if document_to_delete:
            self.documents.remove(document_to_delete[0])


    def get_document(self, document_id):
        show_document = [d for d in self.documents if d.id == document_id]
        if show_document:
            return show_document[0]

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += f"{doc}"
        return result