class Request():
    def __init__(self, order: str):
        self.order = order.split()
        self.from_place = ""
        self.to_place = ""
        self.amount = ""
        self.product = ""

    def get_info(self):
        self.amount = self.order[1]
        self.product = self.order[2]
        self.from_place = self.order[4]
        self.to_place = self.order[6]

    def order_length(self):
        return len(self.order)