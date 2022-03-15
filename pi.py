# Pi Calculator
# After running, type "pi(n)" where n is the number of decimals for pi. For
# example, if you would like to calculate 1000 decimals for pi, type "pi(1000)".

# import python libraries
from decimal import Decimal, getcontext
from time import perf_counter_ns
import datetime

# arccot function using power formula arccot = 1/x - 1/(3x^3) + 1/(5x^5) ...
def arccot(x, digits):
    # set precision and starting values
    getcontext().prec = digits
    total = 0
    n = 1
    # loop while new term is large enough to actually change the total
    while True:
        sub_term = Decimal((2 * n - 1) * x ** (2 * n - 1))
        # exit if new term is too large
        if sub_term >= Decimal(10 ** digits):
            # return the sum
            return total
        # find value of new term, and add the new term to the total
        total += ((-1)**(n - 1)) * 1 / sub_term
        # next n
        n += 1

# pi function
def pi(decimals):
    # start timer
    start_time = perf_counter_ns()

    # find pi using Machin's Formula pi = (16 * arccot(5) - 4 * arccot(239))
    #  and the power formula for arccot (see arccot function above)
    pi = Decimal(
        16 * arccot(5, decimals + 3) -
        4 * arccot(239, decimals + 3)
    ).quantize(Decimal(10) ** -decimals)
    print(f"π = {pi}")

    # display elapsed time
    end_time = perf_counter_ns()
    elapsed_time = (end_time - start_time) / 1_000_000_000
    delta_time = datetime.timedelta(seconds = elapsed_time)
    print(f"Runtime: {delta_time} or {elapsed_time} seconds")

pi(1000)
