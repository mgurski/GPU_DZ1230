import numpy as np
import lorem
from numba import cuda
from numba import *
import helpers
import time

@cuda.jit()
def counting_vowels_in_text(an_array, text):

    index = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    if index < an_array.size:
        if(text[index] == 115):
            an_array[index] += 1



text = 'sssasssasss'*10000000

print(helpers.get_file_size(text))

text = str.encode(text)
start = time.perf_counter()

dText = cuda.to_device(np.array(list(text), dtype=np.int8))
results = np.zeros(len(dText))
print(time.perf_counter() - start)

# d = np.array(c, dtype=np.uint8)

threadsperblock = 512
# blockspergrid = numpy.int(math.ceil(len(c) / (1.0 * 512000)))
blockspergrid = (dText.size + (threadsperblock - 1)) // threadsperblock

counting_vowels_in_text[blockspergrid, threadsperblock](results, dText)

results2 = np.count_nonzero(results == 1)

print(results2)

results3 = 0

start = time.perf_counter()

for a in text:
    if a == 's':
        results3+=1

print(time.perf_counter() - start)


    
# print(dText)

# blockdim = (32, 1, 1)
# griddim = (64,32)

# increment_by_one[blockdim, 32](an_array, dText)

# print(an_array)

# threadsperblock = 32
# blockspergrid = (an_array.size + (threadsperblock - 1)) // threadsperblock
# counting_vowels_in_text[blockspergrid, threadsperblock](an_array)
