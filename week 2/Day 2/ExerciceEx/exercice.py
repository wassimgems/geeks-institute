 # Exercise 1

   #   output : ['a', 'b', 'c']

 # Exercise 2


def sum_numbers(list):
          variable = 0
          for i in list:
             if not isinstance(i, (int, float)):
               continue
             variable += i
          return variable
my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
print(sum_numbers(my_list))