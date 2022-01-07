"""
Iterable - __iter__() or __getitem__() : Iterables create Iterator
Iterator - __next__() : the process of Iterators is known as Iteration 
Iteration -

"""
# generators are those iterators which iterate only once 
def gen(n):
    for i in range(n):
        yield i           #yield is a generator to save ram so that i can generate any huge numbers

g = gen(3)

print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__()) here we get error as we did not stopped the iteration even after the value exceeded
# but in for loop it has been designed in such a way that it automatically stops without error when value exceeds


# for i in g:
#     print(i)

h = "harry"
for c in h:
    print(c)  #this is iterable as __iter__ function works here
   

#  orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())