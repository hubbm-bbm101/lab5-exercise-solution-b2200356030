def sum_odd_numbers(number):
    x = 0
    
    for i in range(1, number + 1):
        
        if i % 2 == 1:
            x += i
    
    return x

def average_of_even(number):
    
    sum_even = 0
    even_numbers = 0
    
    for i in range(1,number+1):
        
        if i % 2 == 0:
            
            sum_even += i
            even_numbers +=1
    
    return sum_even / even_numbers            

a = int(input("tell me your number: " ))
print("first calculation ",sum_odd_numbers(a))
print("second calculation ",average_of_even(a))

              