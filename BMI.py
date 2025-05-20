weight = float( input("Enter weight(kg): "))
height = float(input ("Enter height(cm): "))
BMI = weight / ((height/100)**2)
print (f" Your BMI is: {BMI: .2f} kg/m²")

if BMI < 18.5:
    print ("You are underweight!")
elif BMI >= 18.5 and BMI <= 24.9 :
    print ("You are of Normal weight")
elif BMI >= 25.0 and BMI <= 29.9:
    print ("You are Overweight!")
elif BMI >=30.0 and BMI <= 34.9 :
    print ("You have Obesity class I") 
elif BMI >= 35.0 and BMI <= 39.9 :
    print ("You have obesity class II")
else :
    print ("You have Obesity class III")

