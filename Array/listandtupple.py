# movies=[]
# movies.append(input("enter the first movie:- "))
# movies.append(input("enter the second movie:- "))
# movies.append(input("enter the third movies:- "))
# print(movies)

#check list is a palindrome or not 
list1 =[1,2,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()
if(list1 ==copy_list1):
    print(" palindrome ")
else:
    print(" not palindrome ")