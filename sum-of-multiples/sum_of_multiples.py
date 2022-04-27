def sum_of_multiples(limit, multiples):
    multiples = __multiples(limit, multiples)
    return sum(multiples)


def __multiples(limit, multiples):
    return [i for i in range(1, limit)
            if any(i % multiple == 0 for multiple in multiples if multiple != 0)]
