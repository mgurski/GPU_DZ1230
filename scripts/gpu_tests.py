import csv
import time
import copy
from . import gpu
from . import helpers

def gpu_test():
    """Returns csv"""
    
    test_sizes = [1, 2, 5, 10, 15, 25, 50, 75, 100, 125, 150, 200, 250, 300, 350]

    final_performance_test_list = []
    current_performance_test_list = []

    final_result_list = []
    current_result_list = []
    
    clearing_text = helpers.generate_text_in_mb(350)

    for i in range(len(test_sizes)):
        print('generowanie tekstu nr ' + str(i) + '.0' + ' - ' + str(test_sizes[i]) + ' MB')
        text = helpers.generate_text_in_mb(test_sizes[i])

        current_performance_test_list.clear()
        current_result_list.clear()

        current_performance_test_list.append(str(test_sizes[i]) + " MB")
        current_result_list.append(str(test_sizes[i]) + " MB")

        for j in range(10):
            print('test nr ' + str(j))
            start = time.perf_counter()
            result = gpu.counting_vowels_in_text(text)
            end = time.perf_counter()-start
            
            gpu.counting_vowels_in_text(clearing_text)
            print('generowanie tekstu nr ' + str(i) + '.' + str(j+1))
            text = helpers.generate_text_in_mb(test_sizes[i])
            
            current_result_list.append(result)
            current_performance_test_list.append(end)


        final_result_list.append(copy.deepcopy(current_result_list))
        final_performance_test_list.append(copy.deepcopy(current_performance_test_list))


    f = open('tests/gpu_performance_test_results.csv', 'w')

    with f:
        writer = csv.writer(f)

        for row in final_performance_test_list:
            writer.writerow(row)

    f = open('tests/gpu_results.csv', 'w')

    with f:
        writer = csv.writer(f)

        for row in final_result_list:
            writer.writerow(row)