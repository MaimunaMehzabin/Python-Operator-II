c = input("Enter a Letter: ")

if c >= "a" and c <= "z":
    print(f"The character {c} is a Lowercase alphabet")
    
elif c >= "A" and c <= "Z":
    print(f"The character {c} is an Uppercase alphabet")
    
else: 
    print(f"The character {c} is a Not an alphabet")