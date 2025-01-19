class Connection:
    def __init__(self, item1, item2):
        self.ids = {item1.get_id(), item2.get_id()}
        self.items = {item1, item2}
        self.name = ""
        self.information = ""

    def set_name(self, name):
        self.name = name

    def set_information(self, information):
        self.information = information

    def get_name(self):
        return self.name

    def get_information(self):
        return self.information

    def get_item_names(self):
        return {item.name for item in self.items}

    def __contains__(self, item):
        return item.get_id() in self.ids

    def __hash__(self):
        return hash(tuple(sorted(self.ids)))
