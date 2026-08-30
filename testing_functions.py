# program for bmi calculator
def bmi_calculator(name, height, weight):
    '''this fuction calculates your BMI'''
    bmi = weight / (height**2 )
    print('bmi: ')
    print(bmi)
    if bmi < 25:
        return (name) + " not overweight"
    else:
        return (name) + " overweight"
    
    # calling the function
name1 = "stanley:"
height1 = 3
weight1 = 70

name2 = "royalty"
height2 = 4
weight2 = 60

name3 = "samuel"
height3 = 3
weight3 = 80
print (bmi_calculator  (name1, height1, weight1))
print (bmi_calculator  (name2, height2, weight2))
print (bmi_calculator  (name3, height3, weight3 ))
