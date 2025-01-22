import connection


class ConnectionManager:
    def __init__(self):
        self.connections = {}

    def create_connection(self, item1, item2):
        new_connection = connection.Connection(item1, item2)
        self.connections[new_connection.get_items()] = new_connection

    def delete_connection(self, item1, item2):
        del self.connections[{item1, item2}]

    def get_connection(self, item1, item2):
        return self.connections[{item1, item2}]

    def has_connection(self, item1, item2):
        return {item1, item2} in self

    def __contains__(self, value):
        return value in self.connections
