color1 = input("Enter the first primary color (red/blue/yellow): ")
color2 = input("Enter the second primary color (red/blue/yellow): ")

if color1 == "red" or color1 == "blue" or color1 == "yellow":
    print("Color 1:", color1)
else:
    print("Invalid input for color1")

if color2 == "red" or color2 == "blue" or color2 == "yellow":
    print("Color 2:", color2)
else:
    print("Invalid input for color2")

if color1 == color2:
    print("Error: The two colours you entered are the same.")

if color1 == "red" and color2 == "yellow":
    print("red and yellow: Orange")
    
elif color1 == "red" and color2 == "blue":
    print("red and blue: Purple")
    
elif color1 == "blue" and color2 == "yellow":
    print("blue and yellow: Green") 
    
elif color1 == "blue" and color2 == "red":
    print("blue and red: Purple")
