try:
        value=float(input("Enter the value: "))

        if choice=="1":
            result=value/1000
            print("Result:",result,"kilometers")

        elif choice=="2":
            result =value*1000
            print("Result:",result,"meters")

        elif choice=="3":
            result=value*3.28084
            print("Result:",result,"feet")

        elif choice=="4":
            result = value/3.28084
            print("Result:",result,"meters")

        elif choice=="5":
            result =value*1000
            print("Result:",result,"grams")

        elif choice=="6":
            result = value/1000
            print("Result:",result,"kilograms")

        elif choice=="7":
            result = value*2.20462
            print("Result:",result,"pounds")

        elif choice=="8":
            result = (value*9/5)+32
            print("Result:",result,"°F")

        elif choice=="9":
            result = (value-32)*5/9
            print("Result:",result,"°C")

        elif choice=="10":
            result = value+273.15
            print("Result:",result,"K")

      

  
