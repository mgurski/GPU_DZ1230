import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule
import pycuda.gpuarray as gpuarray
import numpy
import math

def counting_vowels_in_text(text):
    """Returns the number of vowels found in the text?"""

    mod = SourceModule("""
    __global__ void count_vowels(char *text, int *results, int text_size, int chunk_size, int threads_per_block, int blocks_per_grid)
    {
        int index = blockDim.x * blockIdx.x + threadIdx.x;

        int start = index * chunk_size;
        int end = ( index + 1 ) * chunk_size;

        end = min( end, text_size );
        if (end < start)
        {
            return; 
        }

        int i = 0; 

        start = start * 4;
        end = end * 4;
        
        for(i = start; i <= end; i++){

            if (text[i] == 'a' || text[i] == 'A' || text[i] == 'e' || text[i] == 'E' || text[i] == 'i' 
                || text[i] == 'I' || text[i] =='o' || text[i] =='O' || text[i] == 'u' || text[i] == 'U' || text[i] == 'y' || text[i] == 'Y')
            {
                results[i] = 1;
            }
        }

    }
    """)
    cuda.start_profiler()
    
    max_text_size_in_mb = 100

    text_chunks = []
    text_chunks_count = math.ceil(len(text) / (max_text_size_in_mb*(1024**2)))

    while(len(text) > (max_text_size_in_mb*1024**2)):
        text_chunk = text[:math.ceil(len(text)/(text_chunks_count))]
        text2 = text[math.ceil(len(text)/(text_chunks_count)):]

        text = text2
        text_chunks.append(text_chunk)

    text_chunks.append(text)

    cumulative_results = 0
    for text_chunk in text_chunks:
        device_text = gpuarray.to_gpu(numpy.array([text_chunk], dtype=str))
        device_results = gpuarray.zeros(len(text_chunk)*4, dtype=numpy.int32)
                
        chunk_size = 1000
        threads_per_block = 512
        blocks_per_grid = numpy.int(math.ceil(len(text_chunk) / (chunk_size * threads_per_block)))

        device_text_size = numpy.int32(len(text_chunk))     
        
        function = mod.get_function("count_vowels")       
        function(device_text, device_results, device_text_size, numpy.int32(chunk_size), numpy.int32(blocks_per_grid), block = (threads_per_block, 1, 1), grid = (blocks_per_grid, 1, 1))
        
        host_results = device_results.get() 

        results = numpy.count_nonzero(host_results == 1)
        cumulative_results += results
    
    cuda.stop_profiler()
    return cumulative_results

