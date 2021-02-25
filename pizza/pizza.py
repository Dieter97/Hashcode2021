

class Pizza:

    def __init__(self, index, n_in, ingeredients):
        super().__init__()
        self.index = index
        self.n_in = n_in
        self.ingredient_list = set(ingeredients)