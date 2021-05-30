"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import functools

def sum_of_multiples(x,y,limit):
    multiples = [_ for _ in range(limit) if _%x == 0 or _%y==0]
    return functools.reduce(lambda x,y: x + y, multiples)

    return (x_multiples, y_multiples)

def optimized_solution(x,y,limit):
    pass

if __name__ == "__main__":
    print(sum_of_multiples(3,5,10))
    print(sum_of_multiples(3, 5, 1000))

