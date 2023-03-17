from homework21.printing_func import printing
from homework21.classes.abs_storage import Storage

class Store(Storage):
    def __init__(self):
        self._items = {}
        self.capacity = 100

    def add(self, name: str, count: int):
        if self.get_free_space() > count:
            if name in [i for i in self._items.keys()]:
                self._items[name] += count
            else:
                self._items[name] = count
            printing(f"{name.title()} везет курьер в место назаначения")
            printing(f"{name.title()} был(и) успешно доставлен(ы)")
        else:
            return printing(f"Товар {name} не может быть добавлен, потому что на складе осталось мест: {self.get_free_space}")
            raise ValueError

    def remove(self, name: str, count: int):
            if name in [i for i in self._items.keys()]:
                if self._items[name] - count >= 0:
                    printing("Нужное количество есть на складе")

                    self._items[name] = self._items[name] - count
                    printing(f"{name.title()} были забраны со склада курьером")
                else:
                    printing(f"Слишком мало {name} на складе")
                    raise ValueError
            else:
                printing(f"{name.title()} - нет на складе")
                raise ValueError

    def get_free_space(self):
        return self.capacity - sum(self._items.values())

    @property
    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items.keys())

    def print_info(self):
        for k, v in self._items.items():
            print(k, v)