# ask user for valid height
while True:
    try:
        height = int(input("Height : "))
    except ValueError:
        print("Please Enter a valid height.")
        continue
    else:
        if height > 0 and height < 9:
            break
        else:
            print("Height should be greater than 0!")

# create pyramid
for i in range(1, height+1):
    spaces = " " * (height - i)
    blocks = "#" * i
    line = spaces + blocks + "  " + blocks
    print(line)