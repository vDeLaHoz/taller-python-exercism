def square_of_sum(number):
    r = range(1, number+1) 
    return sum(r)**2


def sum_of_squares(number):
    r = range(1, number+1) 
    return sum(x**2 for x in r)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

	


	
