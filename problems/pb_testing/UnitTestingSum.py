from pycsp3 import *

x, y, z = VarArray(size=3, dom={0, 1})

try:
    satisfy(Sum([1, 2, 3]) < 5)
except TypeError as e:
    print("Wrong test 1: ", e)

try:
    satisfy(Sum(None) < 5)
except AssertionError as e:
    print("Wrong test 2: ", e)

satisfy(Sum(x) < 5)

try:
    satisfy(Sum(x, [1]) < 10)
except TypeError as e:
    print("Wrong test 3: ", e)

satisfy(Sum(x, y) < 10)

try:
    satisfy(Sum(x))
except AssertionError as e:
    print("Wrong test 4:", e)

try:
    satisfy(Sum(x) > None)
except AssertionError as e:
    print("Wrong test 5:", e)

try:
    satisfy(Sum(x) > {1, 2, 3})
except AssertionError as e:
    print("Wrong test 6:", e)

satisfy(Sum(x) in {1, 2, 3})

try:
    satisfy(Sum(x) in [1, 2, 3])
except AssertionError as e:
    print("Wrong test 7:", e)

try:
    satisfy(Sum(x, condition=[]))
    satisfy(Sum(x, condition=(0)))
except AssertionError as e:
    print("Wrong test 8:", e)

satisfy(Sum(x, condition=("EQ", 0)))
satisfy(Sum(x, condition=["GE", 0]))