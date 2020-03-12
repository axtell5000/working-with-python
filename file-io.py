# my_file = open("test.txt")
# print(my_file.read())
# my_file.seek(
#     0
# )  # moves cursor to beginning of file, have to do this if we want to print again
# print(my_file.read())
# print(my_file.readlines())
# # print(my_file.readline())
# # print(my_file.readline())
# my_file.close()

# Better way to do it
try:
    with open("test.txt", mode="a") as my_file:
        text = my_file.write("Singing in the rain")
        print(text)
except FileNotFoundError as err:
    print("file does not exist")
    raise err
except IOError as err:
    print("IO error")
    raise err
