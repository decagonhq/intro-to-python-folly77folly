# lambda function
# A function that multiply a list by 2
my_new_value = lambda x : x + 2

print(my_new_value(5))

my_value = lambda num,num2 : (num % 4) * num2

print(my_value(9,10))

#filter functions

#filer numbers greater than 2
my_filters=list(filter(lambda x : x > 2,[1, 2, 3, 4, 5, 6]))

print(my_filters)

#filter names that start with letter b
my_list=['bayo', 'kemi', 'tunde', 'bail', 'zero', 'bang', 'fail', 'Blow']
my_filtered_list=filter(lambda y : y[0:1].lower()=='b',my_list)

print(my_filtered_list)

#map functions

#Capitalize all the first character in a list of names
my_names=['gbolahan akeem eniodunmo', 'fatai ojuola tunde', 'olamide badoo jagaban', 'tunde ednut kolawole']
my_map_list=map(lambda *names : [name.title() for name in names],my_names)

print(my_map_list)

#reverse the names in a list of names
my_names2=['gbolahan', 'fatai', 'olamide', 'tunde']
my_map_list2=map(lambda name : ''.join(reversed(name)), my_names2)

print(my_map_list2)

my_list_new=[1, 2, 4, 5, 6, 7]
filter(lambda x : x > 3, my_list_new)
my_new_map=map( lambda y : y * 2,filter(lambda x : x > 3, my_list_new) )

print(my_new_map)

#reduce functions
my_list_new2=[1, 2, 8]
my_reduce=reduce(lambda x, y: x+y, my_list_new2)
print(my_reduce)

#reduce functions For Acronym
my_list_new2=['Public', 'Service', 'Announcement']
my_reduce=reduce(lambda x, y: x+y, map(lambda z : z[0:1],my_list_new2))
print(my_reduce)

# enumerate functions
# my_obj_new={'name':'aqim', 'surname':'eniodunmo', 'age':20, 'address':'no 18, komolafe street ipaja',}
#serial number of a list
my_list_new=[1, 2, 4, 5, 6, 7]
for b,a in enumerate(my_list_new):
    print b+1,a

#zip functions
zip_list2=[1, 2, 4, 5, 6, 7]
zip_list1=[3, 2, 4, 5, 6, 7]
zip_list3=[6, 2, 4, 5, 6, 7]

for a,b,c in zip(zip_list1, zip_list2, zip_list3):
    print a,b,c