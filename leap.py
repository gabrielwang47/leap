def is_leap(year):
    if year % 4 == 0:
        return True
        
    #elif year % 100 != 0:
       #return True
        
    #elif year % 400 != 0:
        #return False

    else:
    	return False
        
year = input('請輸入西元年份: ')
year = int(year)

print(is_leap(year))
 

if is_leap(year) == True:
	print(year, '年為閏年')

else:
	print(year, '年為平年')



 
