list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")

list3=[1,"abc","abc",1] 
list4=[2,"pqr",3,"abc"]
copy_list3=list3.copy()
copy_list3.reverse()
if(copy_list3==list3):
    print("palindrome")
else:
    print("not palindrome")
