# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_valid_float(s):
    try:
        # Try converting to float
        float(s)
        
        # Ensure there's exactly one decimal point
        if s.count('.') == 1:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        print(is_valid_float(s))
