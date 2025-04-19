def largestnumber(list_of_integer):
    try:
        largest=list_of_integer[0]
        for i in list_of_integer:
            if i>largest:
                largest=i
        return largest
    except ValueError:
        print("Enpty list")
        
result=largestnumber([1,2,3,4,5,20,18])
print(result)