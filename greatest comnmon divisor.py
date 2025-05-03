def gcd(a,b):
    """
    compute the greatest common divisor(gcd)of two numbers using the euclidean algoithm.


    :param a :first number(integer).
    :param b:second number(integer).
    :return:GCD of a and b/
    """

    while b!=0:
        a,b=b,a%b
    return abs(a)#ensure the GCD is always non negative
#example usage
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))


result=gcd(num1,num2)
print(f"THE GCD of {num1} and{num2} is:{result}")
