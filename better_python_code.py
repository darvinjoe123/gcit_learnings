# import sys
# # iterate with enumerate instead of range(len(x))
# data=[1,2,-3,-4]
# for i in range(len(data)):
#     if data[i] < 0:
#         data[i] =0
# print(data)

# data=[1,2,-3,-4]
# for idx,num in enumerate(data):
#     if data[idx] < 0:
#         data[idx] =0
# print(data)

#use list comprehension instead of raw for loops

# squared_list=[]
# for i in range(10):
#     squared_list.append(i*i)
# print(squared_list)


#sort complex iterables with sorted()

# _list=[9,6,7,3,5]
# sorted_list=sorted(_list)
# sorted_list=sorted(_list,reverse=True)
# print(sorted_list)

# data = [{"name":"Max","age":6},
#         {"name":"Lisa","age":20},
#         {"name":"Ben","age":9}] 
# sorted_data = sorted(data, key=lambda x: x["age"])
# print(sorted_data)

# #store unique values with sets

# my_list = [1,2,3,4,5,3,4,5,6,7,8,8,7,6,5,4,3,2,1]
# my_set = set(my_list)
# print(my_set)

# #save memory with Generators
# import sys

# my_list1 = [i for i in range(10000)]
# print(sum(my_list1))
# print(sys.getsizeof(my_list1), "bytes")

# my_gen = (i for i in range(10000))
# print(sum(my_gen))
# print(sys.getsizeof(my_gen), "bytes")

# #Difine default values in Dictionaries with .get() and .setdefault()
# my_dict = {"item":"football","price":10.00}
# count = my_dict.get("value",0)
# print(count)

# count = my_dict.setdefault("count",0)
# print(count)
# print(my_dict)

# #count hashable objects with collections.Counter
# from collections import Counter

# counter=Counter(my_list)
# print(counter)

# most_common = counter.most_common(2)
# print(most_common)


# #format strings with f-strings

# name = "Alex"
# my_string = f"Hello {name}"
# print(my_string)

# i = 10
# print(f"{i} squred is {i*i}")

# #concatenate Strings with .join()
# #BAD
# list_of_strings = ["Hello", "my", "friend"]
# my_string = ""
# for i in list_of_strings:
#     my_string+=i+" "
# print(my_string)
# #GOOD
# new_string = " ".join(list_of_strings)
# print(new_string)

# #merge Dictionaries with {**d1, **d2}

# d1 = {"name":"Alex","age":25}
# d2 = {"name":"Alex","city":"New York"}
# merged_dict = {**d1,**d2}
# print(merged_dict)

# #simplify if-statement with if x in [a,b,c]

# colors = ["red","blue","green","yellow","violet"]
# c = "red"
# if c in colors:
#     print("this is main colour")