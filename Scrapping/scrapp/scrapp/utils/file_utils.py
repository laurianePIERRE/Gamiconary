import os

def create_output_file(path_file, content):
    """

    :param path_file:
    :param content:
    :return:
    """

    with open(path_file, 'w') as f:
        f.write(content+"\n")
    print ("File",path_file,"create successfully")

def remove_duplicates_list(my_list) :
    """

    :param liste:
    :return:
    """
    unique_list = []
    seen = set()
    for item in my_list :
        if item is not seen :
            unique_list.append(item)
            seen.add(item)
    return unique_list

