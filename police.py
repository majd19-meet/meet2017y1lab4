speed = 55
is_birthday = True

##if is_birthday==True:
##    
##    if speed<36:
##        print ('no ticket')
##    elif speed>55:
##        print ('big ticket')
##    elif speed<56:
##        print ('small ticket')
##    elif speed>35:
##        print ('small ticket')
##   
##else:
##    if speed<31:
##        print ('no ticket')
##    elif speed>52:
##        print ('big ticket')
##    elif speed<51:
##        print ('small ticket')
##    elif speed>30:
##        print ('small ticket')




if is_birthday:
    extra = 5
else:
    extra = 0

if speed<31+extra:
    print('no ticket')
elif speed>50+extra:
    print ('big ticket')
else:
    print ('small ticket')
        




    

    
    
