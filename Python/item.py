import text


class Item:
    def __init__(self, ID):
        self.name = text.Text()
        self.information = text.Text()
        self.id = ID

    def set_name(self, name):
        self.name = text.Text(name)

    def set_information(self, information):
        self.information = text.Text(information)

    def get_name(self):
        return self.name

    def get_information(self):
        return self.information

    def get_id(self):
        return self.id

    def __hash__(self):
        return hash((self.id))
