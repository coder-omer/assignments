number = input("Enter a positive integer number please : ")
if number.isdigit() and int(number) > 0:
     nod = len(number)
     sum = 0
     for i in number:
       i = int(i)
       sum += (pow(i, nod))
     if int(number) == sum:
       print("{} is an Amstrong number".format(number))
     else:
       print("{} is not an Amstrong number".format(number)) 
else:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")