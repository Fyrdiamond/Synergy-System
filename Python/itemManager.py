import item


class ItemManager:
    def __init__(self, num_items):
        self.global_identity = 0
        self.items = {}

    def create_item(self):
        ID = self.global_identity
        self.items[ID] = item.Item(ID)
        self.global_identity += 1

    def delete_item(self, ID):
        del self.items[ID]

    def get_item(self, ID):
        return self.items[ID]
