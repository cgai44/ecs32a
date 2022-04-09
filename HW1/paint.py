print("Paint coverage estimator")
l = int(input("Length of room in inches:"))
w = int(input("Width of room in inches:"))
h = int(input("Average height of room in inches:"))
squinches = (l * h * 2) + (w * h * 2)
float_cans = squinches / 14400
int_cans = int(float_cans) + 1
print("You'll want", int_cans, "cans.")
