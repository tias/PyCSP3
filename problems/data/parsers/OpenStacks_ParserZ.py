from pycsp3.problems.data.dataparser import *

next_line(repeat=2)

data.orders = [numbers_in(line) for line in remaining_lines()]
