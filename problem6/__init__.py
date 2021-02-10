def sum_of_squares(n_list):
    return sum([x**2 for x in n_list])


def square_of_sum(n_list):
    return sum(n_list)**2


if __name__ == '__main__':
    numbers = list(range(1, 101))
    print(square_of_sum(numbers) - sum_of_squares(numbers))
