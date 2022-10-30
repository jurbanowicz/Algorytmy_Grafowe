from dimacs import *
import os
import time


def run_all_graphs(folder_path, solution):

    counter = 0
    passed = 0
    failed = 0
    total_s = time.time()
    for i, file_name in enumerate(os.listdir(folder_path)):


        print("Test number - ", i)
        corr_res = readSolution(folder_path + file_name)
        print("Correct result: ", corr_res)
        (V,L) = loadWeightedGraph(folder_path + file_name)

        time_s = time.time()
        my_res = solution(V, L)
        time_e = time.time()
        print("My result: ", my_res)

        test_time = time_e - time_s
        print("Time: %.4f seconds" % test_time)

        if my_res == int(corr_res):
            passed += 1
            print("Test Passed")
        else:
            failed += 1
            print("TEST FAILED")

        counter += 1

        print("-----------------------------")

    total_e = time.time()

    total_time = total_e - total_s

    print("Passed ", passed, "/", counter, "tests")
    print("Estimated running time: %.4f seconds" % total_time)