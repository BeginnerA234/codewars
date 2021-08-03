# https://www.codewars.com/kata/5abab55b20746bc32e000008/train/python

generation0 = [
    {'x': 0, 'y': 4, 'size': True},
    {'x': 0, 'y': 7, 'size': 5},
    {'x': 2, 'y': 0, 'size': 2},
    {'x': 3, 'y': 7, 'size': 2},
    {'x': 4, 'y': 3, 'size': 4},
    {'x': 5, 'y': 6, 'size': 2},
    {'x': 6, 'y': 7, 'size': 1},
    {'x': 7, 'y': 0, 'size': 3},
    {'x': 7, 'y': 2, 'size': 1}
]


class Blobservation:

    def __init__(self, quantity: int):
        """
        Создаем игровое квадратное игровое поле
        """
        self.blobs = []
        self.quantity = quantity
        for i in range(quantity):
            self.blobs.append([0 for i in range(quantity)])

    def populate(self, blobs: list):
        """
        Размещаем на начальные позиции капли.
        НУЖНО ИСПРАВИТЬ СОГЛАСНО ТЗ
        """
        for blob in blobs:
            x = blob.get('x')
            y = blob.get('y')
            size = blob.get('size')
            try:
                if isinstance(size, int) and not isinstance(size, bool):
                    self.blobs[x][y] = size
            except Exception:
                ValueError('Bool syka')



    def print_state(self):
        """
        Выводит текущую позиции капли/каплей
        """
        state = []
        vertical = 0
        horizontal = 0
        if self.blobs:
            for blob in self.blobs:
                for size in blob:
                    if size > 0:
                        state.append([vertical, horizontal, size])
                    horizontal += 1
                horizontal = 0
                vertical += 1
            return state
        return state

    def move(self, iter: int):
        """
        Каждая капля делает 1 шаг в сторону ближайшей
        """
        pass


test = Blobservation(8)
test.populate(generation0)
# print(test.print_state())
print(test.blobs)
