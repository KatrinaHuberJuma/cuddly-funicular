
print("heeyyyyyyyyyyyy")
def add_nums(x, y):
    """Return sum of x and y."""
    
    print(x + y)
    return x + y

print(add_nums(4,5))

def print_evens(n):
    """Print first n even numbers."""

    for i in range(n):
        print(i * 2)


def process_file(path):
    """Print file until line starting with STOP HERE."""

    for line in open(path):
        line = line.rstrip()
        if line.startswith("STOP HERE"):
            break
        print(line)

    print("Entire file was printed")

process_file("poem.txt")


def print_items(items):
    """Print items."""

    for item in items:
        print(item)


def get_melon_order_price(price, quantity):
    """Calculate the cost for an order of melons."""

    tax = 0.075

    return(price * quantity + (tax * price * quantity))
