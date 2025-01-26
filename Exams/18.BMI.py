def BMI():
    weight=int(input("Enter the weight: "))  #input values 
    height=int(input("Enter the height: "))
    return (weight,height)
#using farmula to check bmi and condition cheking
def pll(weight,height):
    bmi=weight/(height**2)
    if(bmi<=18):
        return "Underweight"
    elif(18<= bmi >=25):
        return "normal"
    elif(25<= bmi >=29):
        return "overweight"
    else:
        return "obese"
    #call the functions and main function
def main():

    weight,height=BMI()
    result=pll(weight,height)
    print(f"your BMI category is: {result}") 
main()       
    
