import time


def compare_speed_of_functions(input_to_func, function_list, exp_output):
    speed_dict = dict()
    longest_name = 0
    for func in function_list:
        name = func.__name__
        size = len(name)
        if size > longest_name:
            longest_name = size
        print("Applying {}".format(name))
        t0 = time.time()
        output = func(input_to_func)
        t1 = time.time()
        if output == exp_output:
            total = round(t1-t0, 8)
            speed_dict[name] = total
        else:
            print("{}: Incorrect Output Found: {}".format(name, output))
        print()
    display_results(speed_dict, longest_name)


def display_results(speed_dict, longest_name):
    sorted_pairs = sorted(speed_dict.items(), key=lambda x: x[1])
    pos = 1
    for pair in sorted_pairs:
        name = pair[0]
        t = pair[1]
        print("{:<2} | {:<{}} | {:<10}".format(pos, name, longest_name, t))
        pos += 1
