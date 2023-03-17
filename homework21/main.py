from homework21.classes.request import Request
from homework21.classes.shop import Shop
from homework21.classes.store import Store
from printing_func import printing


def main():
    shop = Shop()
    store = Store()
    store.add("печеньки", 5)
    store.add("бананы", 5)
    store.add("груши", 5)
    shop.add("коробки", 1)
    shop.add("чипсы", 5)
    shop.add("огурцы", 10)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    printing("Приветствую! Здесь вы можете заказать товар!")
    user = '\033[1m' + '\nUser:' + '\033[0m'
    printing("Сейчас хранится:")
    printing("В складе хранится:")
    store.print_info()
    printing("В магазине хранится:")
    shop.print_info()
    while True:
        printing("Заказ должен выглядеть так:\nДоставить 3 печеньки из склад в магазин")
        user_order = input(user)
        request = Request(user_order)
        try:
            request.get_info()
        except IndexError:
            printing("Вы ввели запрос не так как в примере!")
        if request.order_length() == 7:
            if request.order[0].lower() == "доставить":
                try:
                    count = int(request.amount)
                except ValueError:
                    print("Вы не ввели количество продукта, попробуйте снова")
                    continue

                if request.from_place.lower() != "склад":
                    print("Вы не ввели откуда доставить товар, попробуйте снова")
                    continue

                if request.to_place.lower() != "магазин":
                    print("Вы не ввели куда доставить товар, попробуйте снова")
                    continue

                try:
                    store.remove(request.product, count)
                except Exception:
                    continue

                try:
                    shop.add(request.product, count)
                except Exception:
                    continue
                break
        else:
            printing("Вы ввели запрос не так как в примере!")

    printing("В складе хранится:")
    store.print_info()

    printing("В магазине хранится:")
    shop.print_info()



if __name__ == "__main__":
    main()