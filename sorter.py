from sys import argv


def text_read(input_file_name):
    f = open(input_file_name)
    r = str(f.read())
    f.close
    return r

def str_to_arr(t):
    a = t.split(', ')
    return a


def sortt(arr):
    arr_copy = arr.copy()  # Make a copy of the input list
    l = len(arr_copy)
    for j in range(l-1):
        for i in range(l-1-j):
            if len(arr_copy[i]) > len(arr_copy[i+1]):
                arr_copy[i], arr_copy[i+1] = arr_copy[i+1], arr_copy[i]
    return arr_copy  # Return the sorted copy


def write_text(data, file_name):
    f = open(file_name, "a")
    f.write(data)
    f.close()

def main():
    script, inp, out = argv
    input_file = text_read(inp)
    my_list = str_to_arr(input_file)
    sorted_file = sortt(my_list)
    write_text(', '.join(sorted_file),out)

main()