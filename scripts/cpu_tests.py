import csv
import time
import copy
from . import cpu
from . import helpers

def cpu_test():
    """Returns csv"""
    
    test_sizes = [5, 10, 15]

    final_performance_test_list = []
    current_performance_test_list = []

    final_result_list = []
    current_result_list = []

    for i in range(len(test_sizes)):
        print('generowanie tekstu nr ' + str(i))
        text = helpers.faker_text(test_sizes[i])

        current_performance_test_list.clear()
        current_result_list.clear()

        current_performance_test_list.append(str(test_sizes[i]) + " MB")
        current_result_list.append(str(test_sizes[i]) + " MB")

        for i in range(2):
            print('test nr ' + str(i))
            start = time.perf_counter()
            result = cpu.counting_vowels_in_text(text)
            end = time.perf_counter()-start

            current_result_list.append(result)
            current_performance_test_list.append(end)


        final_result_list.append(copy.deepcopy(current_result_list))
        final_performance_test_list.append(copy.deepcopy(current_performance_test_list))


    f = open('tests/cpu_performance_test_results.csv', 'w')

    with f:
        writer = csv.writer(f)

        for row in final_performance_test_list:
            writer.writerow(row)

    f = open('tests/cpu_results.csv', 'w')

    with f:
        writer = csv.writer(f)

        for row in final_result_list:
            writer.writerow(row)

