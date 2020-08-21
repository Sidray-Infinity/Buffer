
#!/usr/bin/python3

if __name__ == "__main__":
    n = int(input())

    base = 7
    res = []
    mapper = list("0123456")
    while True:
        res.append(mapper[n%base])
        n = n // base
        if n == 0:
            break
   #this is a test comment 
