n1 = int( input("Please enter value for P: "))  
n2 = int( input("Please enter value for Q: "))  
   
# To swap the value of two variables  
# we will user third variable which is a temporary variable  
temp = n1
n1 = n2
n2 = temp 
   
print ("The Value of P after swapping: ", n1)  
print ("The Value of Q after swapping: ", n2)  