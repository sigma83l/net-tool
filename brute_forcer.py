import random
import math
import numpy as np
import time
from itertools import permutations

class random_brute_forcer:
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    charecters = r'!@#$%^&*()_+=-`~?/[]{}>.<:;'
    
    def fisrt_step(self):
            randnlow = [i for i in range(1, 26)]
            randup = [i for i in range(1, 26)]
            randnum = [i for i in range(1, 10)]

            for i in randnlow:
                for j in randup:
                    for k in randnum:
                        print(i,j,k)
                        
    def optimized(self):
            all_chars = self.lower_letters+self.upper_letters
            res = []
            result_list = []
            for idx in range(len(all_chars) + 1):
        
            # getting overlap strings
                res.append([all_chars[j: j + idx] for j in range(len(all_chars) - idx + 1)]) 
            for index, i in enumerate(res) :
                while index <= 5:
                    result_list.append([''.join(p) for p in permutations(i)])
            print(result_list)  

        # fisrt_step()
    # start = time.time
    # end = time.time()


 
# perms = [''.join(p) for p in permutations('stack')]
res = random_brute_forcer()
result = res.optimized()
# print(len(result))
# for i in result:
#     print(i)