#recursion function
def root(dividend_number, dividend_list, divisor, nums_before_pt):
    
    #for first dividend
    if divisor==0:

        #finding the divisor
        for i in range(dividend_number//2+2):
            
            a=i
            b=i+1
            
            if a**2<=dividend_number and b**2>dividend_number:
                
                remainder=dividend_number-a**2
                
                next_dividend= remainder*100 + dividend_list.pop(0) #next dividend

                next_divisor=i*2*10 #base of next divisor
                
                #the quotient
                return 10**(nums_before_pt-1)*i + root(next_dividend, dividend_list, next_divisor, nums_before_pt-1)
            
    #for all the other dividend
    else:
        #finding the divisor
        for i in range(10):
            
            a=divisor+i
            b=divisor+i+1
            
            if a*i<=dividend_number and b*(i+1)>dividend_number:
                
                remainder=dividend_number-a*i

                #condition for ending recursion
                if dividend_list==[]:
                    
                    return 10**(nums_before_pt-1)*i
                
                next_dividend= remainder*100 + dividend_list.pop(0) #next dividend

                next_divisor=(divisor+(i*2))*10 #base of next divisor

                #the quotient
                return 10**(nums_before_pt-1)*i + root(next_dividend, dividend_list, next_divisor, nums_before_pt-1)
            
dividend_list=[0,0,0,0,0,0,0,0,0,0]

#getting the number
number=input()

#list of dividend numbers
for i in range(-1,-len(number)-1,-2):
    dividend_list.insert(0,int(number[i:i-2:-1][::-1]))
    
length_dividend_list=len(dividend_list)

#first dividend number
dividend_number=dividend_list.pop(0)

#number of numbers before the point (this is to know when to add the point in the quotient)
nums_before_pt=length_dividend_list-10

#calling the function
square_root=round(root(dividend_number, dividend_list, 0, nums_before_pt),10)

#printing the root
print(f'square root of {number} = {square_root}')
