while True:
    while True:
        num1 = input("Enter a number (or a letter to exit): ")
        if num1.isdigit():
                    num1 = int(num1)
                    break
        else:
            exit()
      
   
    operator = input("Enter an operation: ")
    num2 = int(input("Enter an other number: "))

    if operator == "+" :
        osszeadas = num1 + num2
        print("Result:", osszeadas)

    if operator == "-" :
        kivonas = num1 - num2
        print("Result:", kivonas)

    if operator == "/" :
        osztas = num1 / num2
        print("Result:", osztas)

    if operator =="*" :
        szorzas = num1 * num2
        print("Result:", szorzas)