"""
Bubble sort is a simple sorting algorithm.
This sorting algorithm is comparison-based algorithm
in which each pair of adjacent elements is compared
and the elements are swapped if they are not in order.
This algorithm is not suitable for large data sets as
its average and worst case complexity are of Ο(n2) where
n is the number of items.
"""


class Service(object):

    def bubble_sort(list_of_objects):
        number_of_steps = 0
        for i in range(0, len(list_of_objects)):
            for j in range(0, len(list_of_objects)):
                number_of_steps += 1
                outer = list_of_objects[i]
                if outer < list_of_objects[j]:
                    list_of_objects[i] = list_of_objects[j]
                    list_of_objects[j] = outer

        # number of steps is represented by O(n*n)
        print(number_of_steps)
        print(len(list_of_objects) * len(list_of_objects) == number_of_steps)
        return list_of_objects
