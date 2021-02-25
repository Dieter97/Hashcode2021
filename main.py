from naive_algorithm.NaiveSovler import NaiveIntersectionOptimizer as Solver


def work(input_file: str, output_file: str):   
    optimizer = Solver(input_file)
    solution = optimizer.calculate_solution()
    write_solution(solution, output_file)


def write_solution(intersections, file):
    valid_intersections = []
    for intersection in intersections.values():
        if intersection.schedule:
            valid_intersections.append(intersection)

    f = open(file, "w")
    f.write(str(len(valid_intersections)) + '\n')
    # Solution is list of intersections with a schedule object
    for intersection in valid_intersections:
        f.write(f"{intersection.index}\n")
        f.write(f"{len(intersection.schedule)}\n")
        for s in intersection.schedule:
            if s.duration != 0:
                f.write(f"{s.street.name} {s.duration}\n")
    f.close()


if __name__ == "__main__":
    inputs = ["inputs/a.txt", "inputs/b.txt","inputs/c.txt", "inputs/d.txt", "inputs/e.txt", "inputs/f.txt"]
    outputs = ["outputs/out.a", "outputs/out.b", "outputs/out.c", "outputs/out.d", "outputs/out.e", "outputs/out.f"]
    for i in range(len(inputs)):
        work(inputs[i], outputs[i])
