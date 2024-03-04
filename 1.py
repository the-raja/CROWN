def matches_template(a, b, c):
    for i in range(len(a)):
        if a[i] == b[i]:
            # If characters in a and b are same, they must match with c
            if c[i] != a[i]:
                return False
        else:
            # If characters in a and b are different, they should differ from c
            if c[i] == a[i] or c[i] == b[i]:
                return False
    return True

def exists_valid_template(n, a, b, c):
    # Check if there exists a template where a and b match but c doesn't
    for i in range(2 ** n):
        template = ""
        for j in range(n):
            if i & (1 << j):
                template += a[j].upper()  # Uppercase character
            else:
                template += a[j].lower()  # Lowercase character

        if matches_template(a, b, template) and not matches_template(c, c, template):
            return True
    return False

# Read input
n = int(input())
a = input().strip()
b = input().strip()
c = input().strip()

# Check if there exists a valid template
if exists_valid_template(n, a, b, c):
    print("YES")
else:
    print("NO")
