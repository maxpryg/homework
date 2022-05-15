class ReverseIter():
    """Класс принимает список и итерируется по нему в обратном направлении."""
    def __init__(self, data: list):
        self.data = data
        self.index = len(self.data)

    # атрибут data реализован через property, чтобы вынести проверку типа из
    # метода __init__
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if not isinstance(data, list):
            raise TypeError('Argument must be list')
        self._data = data

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.data[self.index]
