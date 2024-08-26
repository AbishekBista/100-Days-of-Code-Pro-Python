# FileNotFoundError
# with open('afile.txt') as file:
#     file.read()

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Banana", "Apple", "Mango"]
# fruit  = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

# try -> runs code that may actually cause an error
# except -> do this if an exception occurs
# else -> do the thing if no exception
# finally -> do any task which do not care if exception occurred or not

try:
    file = open('a_file.txt')
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Something')
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File was closed')
