class Text(str):
    def __add__(self, other):
        return Text(str(self) + other)

    def __sub__(self, other):
        return Text(self[:-other])
