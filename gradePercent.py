#Program to read the marks in five subjects and compute the percentage and grade.
sub1 = int(input("Input the first subject marks"))
sub2 = int(input("Input the second subject marks"))
sub3 = int(input("Input the third subject marks"))
sub4 = int(input("Input the fourth subject marks"))
sub5 = int(input("Input the fifth subject marks"))
totalP=(sub1+sub2+sub3+sub4+sub5)/5
if(totalP>90):
  print("Grade is A and percentage is", totalP)
elif(totalP>80):
  print("Grade is B and percentage is", totalP)
elif(totalP>70):
  print("Grade is C and percentage is", totalP)
elif(totalP>60):
  print("Grade is D and percentage is", totalP)
else:
  print("Grade is E and percentage is", totalP)
