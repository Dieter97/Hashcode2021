import collections
import copy
import time
class PizzaOptimizer:

    def __init__(self, n_pizza, n2, n3, n4, pizzas, union_map):
        self.n_pizzas = n_pizza
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.pizzas = pizzas
        self.union_map = union_map

    def calculate_solution(self):
        n2_pizzas = []
        n3_pizzas = []
        n4_pizzas = []

        while self.n_pizzas >= 2:
            if len(self.pizzas) >= 4 and self.n4 > 0: 
                print('Looking for 4 pizzas...')
                pizzas = self.find_n(4)
                if len(pizzas) == 4:
                    self.n4 -= 1
                    self.n_pizzas -= 4
                    n4_pizzas.append("4 {} {} {} {}".format(pizzas[0].index, pizzas[1].index, pizzas[2].index, pizzas[3].index))
            elif len(self.pizzas) >= 3 and self.n3 > 0:
                print('Looking for 3 pizzas...')
                pizzas =self.find_n(3)
                if len(pizzas) == 3:
                    self.n3 -= 1
                    self.n_pizzas -= 3
                    n3_pizzas.append("3 {} {} {}".format(pizzas[0].index, pizzas[1].index, pizzas[2].index))
            elif len(self.pizzas) >= 2 and self.n2 > 0:
                print('Looking for 2 pizzas...')
                pizzas =self.find_n(2)
                if len(pizzas) == 2:
                    self.n2 -= 1
                    self.n_pizzas -= 2
                    n2_pizzas.append("2 {} {}".format(pizzas[0].index, pizzas[1].index))
            else:
                break
            print("Pizza remaining: ", self.n_pizzas)
        return n2_pizzas, n3_pizzas, n4_pizzas    


    def find_n(self, n):
        ingredients = set()
        pizzas = []
        best = 0
        #start_time = time.time()
        tmp_pizzas = copy.copy(self.pizzas)
        #print("--- Deep copy Pizza took: %s seconds ---" % (time.time() - start_time))
        for k in range(n):
            pizza, best  = self.find_next_improving(best, tmp_pizzas, ingredients, best)
            if pizza is not None:
                ingredients.update(pizza.ingredient_list)
                
                tmp_pizzas = [i for i in tmp_pizzas if i.index!=pizza.index]
                
                pizzas.append(pizza)
                
        print(best)
        if len(pizzas) == n:
            self.pizzas = tmp_pizzas 
        del tmp_pizzas    
        return pizzas           

    def find_next_improving(self, best, pizzas, used_ingredients, current_score):
        best_pizza = None
        last_n_in = 0
        strike = 0 
        #if len(used_ingredients) > 0:
        #    pizzas.reverse()
        for pizza in pizzas:
            score = len(pizza.ingredient_list.symmetric_difference(used_ingredients)) + current_score
            if (pizza.n_in < last_n_in and pizza.n_in == score) or strike == 100000:
                #print("skipping")
                break
            # print("score: ", score, "\tIn: ", pizza.n_in)
            last_n_in = pizza.n_in
            if score >= best:
                best = score
                best_pizza = pizza
                strike = 0
            else:
                strike += 1
        return best_pizza, best

