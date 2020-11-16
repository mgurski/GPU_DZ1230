import argparse

import scripts.cpu
import scripts.gpu
import scripts.cpu_tests
import scripts.gpu_tests
import scripts.helpers
import time

if __name__ == "__main__":
    

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group2 = parser.add_mutually_exclusive_group(required=False)


    group.add_argument("-cpu", "--cpu", help="Run the cpu version of the algorithm", action="store_true")
    group.add_argument(
        "-gpu", "--gpu", help="Run the gpu version of the algorithm", action="store_true")
    group.add_argument(
        "-cpu_test", "--cpu_test", help="Run the gpu version of the algorithm", action="store_true")
    group.add_argument(
        "-gpu_test", "--gpu_test", help="Run the gpu version of the algorithm", action="store_true")
    
    group2.add_argument("-path", "--path", help="Path to the text file", type=str, required=False, default='')
    group2.add_argument("-auto", "--autogenerate", help="Autogenerate text of given size", type=int, required=False, default=50)

    args = parser.parse_args()

    text = ''

    if(args.cpu_test):
        scripts.cpu_tests.cpu_test()
    elif(args.gpu_test):
        scripts.gpu_tests.gpu_test()
    elif(args.path != ''):
        text = scripts.helpers.load_text_from_file(args.path)
    else:
        text = scripts.helpers.generate_text_in_mb(args.autogenerate)

    if(args.cpu):
        start = time.perf_counter()
        scripts.cpu.counting_vowels_in_text(text)
        print(time.perf_counter()-start)
        
    elif(args.gpu):
        start = time.perf_counter()
        scripts.gpu.counting_vowels_in_text(text)
        print(time.perf_counter()-start)




