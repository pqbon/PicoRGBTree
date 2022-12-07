from xmas_tree_rg import xmas_tree_redgreen 
from xmas_tree_rg_chase import xmas_tree_redgreen_bright
from xmas_tree_colours import xmas_tree_colours 
from xmas_tree_pastel import xmas_tree_pastel 
from xmas_tree_solid import xmas_tree_solid 
from xmas_tree_waves import xmas_tree_waves
from xmas_tree_random import xmas_tree_random

import random


if __name__ == '__main__':
    while True :
        run_len = random.choice(range(100, 10000))
        xmas_tree_redgreen(run_len)
        run_len = random.choice(range(100, 10000))
        xmas_tree_colours(run_len)
        run_len = random.choice(range(100, 10000))
        xmas_tree_pastel(run_len)
        run_len = random.choice(range(100, 10000))
        xmas_tree_redgreen_bright(run_len)
        run_len = random.choice(range(100, 10000))
        xmas_tree_solid(run_len)
        run_len = random.choice(range(100, 10000))
        xmas_tree_waves(run_len)
        run_len = random.choice(range(100, 10000))
        xmas_tree_random(run_len)