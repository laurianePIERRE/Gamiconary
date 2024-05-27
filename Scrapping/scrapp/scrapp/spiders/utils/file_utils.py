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