def calculate_simularity_score(left_list, right_list):

    right_counter = {val: right_list.count(val) for val in right_list}

    simularity_score = 0

    for val in left_list:
        if val in right_counter:
            simularity_score += val * right_counter[val]

    return simularity_score


def main():
    left_list = []
    right_list = []

    with open("input.txt", "r") as f:
        for line in f:
            left_val, right_val = map(int, line.split())
            left_list.append(left_val)
            right_list.append(right_val)

    print(calculate_simularity_score(left_list, right_list))


if __name__ == "__main__":
    main()
