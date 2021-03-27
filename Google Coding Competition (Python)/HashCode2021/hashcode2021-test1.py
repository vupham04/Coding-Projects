

def get_input(filename):
    ret_string = ""
    with open(filename, "r") as f:
        lines = f.readlines()

    firstLine = lines[0].split(" ")
    simulationTime = int(firstLine[0])
    intersections = int(firstLine[1])

    ret_string += str(intersections) + "\n"

    streetNum = int(firstLine[2])
    car = int(firstLine[3])
    score = int(firstLine[4])

    lineNo = 1
    street = {}
    graph = [[0 for _ in range(intersections)]
             for _ in range(intersections)]
    for _ in range(streetNum):
        line = lines[lineNo].split(" ")
        street[(int(line[0]), int(line[1]))] = line[2]
        graph[int(line[0])][int(line[1])] = int(line[3])
        lineNo += 1

    # print(intersections)
    for i in range(intersections):
        # print(i)

        ret_string += str(i) + "\n"

        count = 0
        light = []
        for j in range(intersections):
            if graph[j][i]:
                count += 1
                light.append(street[(j, i)]+" 1")
        # print(count)
        ret_string += str(count) + "\n"
        for n in light:
            # print(n)
            ret_string += n + "\n"
    return ret_string


def write_output(filename, string):
    with open(filename, "w+") as f:
        f.write(string)


# write_output("outcome_f.txt", get_input("f.txt"))

files = ["a", "b", "c", "d", "e", "f"]

for f in files:
    write_output("outcome_"+f+".txt", get_input(f+".txt"))
    print("DONE ", f)

# print("Aaaaaaaaaaaaaaaa")
# print(ret_string)
