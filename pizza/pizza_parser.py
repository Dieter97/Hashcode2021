import numpy as np
from pizza.pizza import Pizza
import threading
from multiprocessing import Process, Value, Array
def calculateUnion(union_map, idx, pizzas):
    for k in range(len(pizzas)):
        if union_map[idx,k] == 0:
            union_map[k,idx] = union_map[idx,k] = len(pizzas[idx].ingredient_list.union(pizzas[k].ingredient_list)) 
class PizzaParser:

    def __init__(self):
        super().__init__()

    def parse_file(self,input_file):
        f = open(input_file)
        
        n_pizza, n2, n3, n4 = (int(s) for s in f.readline().split())
        pizzas = []
        i = 0
        for line in f:
            info = line.split()
            pizzas.append(Pizza(i, int(info[0]), info[1:]))
            i += 1
        pizzas.sort(key=lambda x: x.n_in, reverse=True)

        
                   # print(idx,"\t",k)

        # Calculate union map
        union_map = Array("d",np.zeros((len(pizzas),len(pizzas))))
        remaining_pizza = len(pizzas)-1
        max_threads = 24
        while remaining_pizza > 0:
            if remaining_pizza > max_threads:
                num_threads = max_threads
            else:
                num_threads = remaining_pizza
            threads = list()
            for index in range(num_threads):
                x = Process(target=calculateUnion, args=(union_map,remaining_pizza-index,pizzas))
                threads.append(x)
                x.start()

            for index, thread in enumerate(threads):
                thread.join()
            
            remaining_pizza -= num_threads
            print(remaining_pizza)
        return n_pizza, n2, n3, n4, pizzas, union_map