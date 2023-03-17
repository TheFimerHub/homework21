from homework21.classes.store import Store
from homework21.printing_func import printing


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._items = {}
        self.capacity = 20

    def add(self, name: str, count: int):
        if self.get_free_space > count:
            if name in [i for i in self._items.keys()]:
                self._items[name] += count
            else:
                self._items[name] = count
            printing(f"{name.title()} везет курьер в место назаначения")
            printing(f"{name.title()} был(и) успешно доставлен(ы)")
        else:
            printing(f"Товар {name} не может быть добавлен, потому что на складе осталось мест: {self.get_free_space}")
            raise ValueError

    @property
    def get_free_space(self):
        return self.capacity - sum(self._items.values())

    def get_unique_items_count(self):
        return len(self._items.keys())

    def print_info(self):
        for k, v in self._items.items():
            print(k, v)