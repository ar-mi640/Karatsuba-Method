def karatsuba(number1,number2):
    l1=int(len(number1))
    l2=int(len(number2))
    if l2>l1:
        limit=l2
        number1=number1.zfill(limit)
    elif l1>l2 :
        limit=l1
        number2=number2.zfill(limit)
    else :
        limit=l1 
    if limit%2==0 : 
       limit=limit//2      
       digits1_number1=int(number1[0 :limit])
       digits2_number1=int(number1[limit:])
       digits1_number2=int(number2[0 : limit])
       digits2_number2=int(number2[limit:]) 
    else :
       limit=limit//2 
       digits1_number1=int(number1[0 :limit +1])
       digits2_number1=int(number1[limit +1: ])
       digits1_number2 = int(number2[0:limit +1])
       digits2_number2=int(number2[limit +1:])      
    z1=digits1_number1*digits1_number2
    z2=digits2_number1*digits2_number2
    z0=((digits1_number1+digits2_number1)*(digits1_number2+digits2_number2) )-z1-z2
    result=(z1*(10**limit))+(z0*100)+z2
    return result


number1 = input ("number1 ? ")
number2 = input ("number2 ? ")
print(karatsuba(number1,number2))


    





    
