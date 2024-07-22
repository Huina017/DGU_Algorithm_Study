n = int(input())

for _ in range(n):
    
    stack = []
    ps = input()
    
    for p in ps:
        if p == '(':
            stack.append(p)
            
        elif p == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
            
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
