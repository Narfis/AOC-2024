def pair_distance_sum(left_list, right_list):

    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)

    distance_list = []

    for left, right in zip(sorted_left_list, sorted_right_list):
        distance_list.append(abs(left - right))

    return sum(distance_list)


def main():
    left_list = []
    right_list = []

    with open("./input.txt", "r") as f:
        for line in f:
            left_val, right_val = map(int, line.split())
            left_list.append(left_val)
            right_list.append(right_val)

    print(pair_distance_sum(left_list, right_list))


if __name__ == "__main__":
    main()
