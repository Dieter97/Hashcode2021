from pizza.pizza_optimizer import PizzaOptimizer
from streets.street_parser import StreetParser


def work(input_file: str, output_file: str):
    parser = StreetParser()
    problem = parser.parse_file(input_file)
    #optimizer = PizzaOptimizer(problem[0],problem[1],problem[2],problem[3],problem[4], problem[5])
    #solution = optimizer.calculate_solution()
    #write_solution(solution, output_file)

def write_solution(solution, file):
    f = open(file, "w")
    # TODO
    f.close()

if __name__ == "__main__":
    inputs = ["inputs\\a.txt", "inputs\\b.txt","inputs\\c.txt", "inputs\\d.txt", "inputs\\e.txt", "inputs\\f.txt"]
    outputs = ["outputs\\out.a", "outputs\\out.b", "outputs\\out.c", "outputs\\out.d", "outputs\\out.e", "outputs\\out.f"]
    for i in range(len(inputs)):
        work(inputs[i], outputs[i])
