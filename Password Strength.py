def measure(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    m = n
    num = 0
    P = ""

    countn = 0
    countl = 0
    countu = 0
    counts = 0
    for i in range(0,m):
            P = password[i]
            if(P in numbers):
                countn+=1
            if(P in lower_case):
                countl+=1
            if(P in upper_case):
                countu+=1
            if(P in special_characters):
                counts+=1

    if countn==0:
        num+=1
    if countl==0:
        num+=1
    if countu==0:
        num+=1
    if counts==0:
        num+=1

    while 6 - n > num:
        num += 1
        
    return num


n= int(input())
password = input()
answer = measure(n, password)

print(f'Need to add {answer} more characters')

