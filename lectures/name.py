import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    # Print name tags
    print("Hello, my name is ", sys.argv[1])
