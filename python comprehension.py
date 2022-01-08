# Comprehension: list comprehension, dictionary comprehension, set comprehension, generator comprehension

#list comprehension
ls = []
for i in range(100):
    if i%3 == 0:
        ls.append(i)

print(ls) 

#orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

ls = [i for i in range(100) if i%3==0]
print(ls)



#dictionary comprehension

dict1 = {
    i:f"item{i}" for i in range(101) if i%10== 0
}
dict2 = {value:key for key, value in dict1.items()}   #reversing the key pairs in dictionary

print(dict1)
print(dict2)




#set comprehension

dresses = {dress for dress in ["dress1", "dress2", "dress1"]}

print(dresses)



# generator comprehension

evens = (i for i in range(100) if i%2==0)

print(evens)