x =int(input("Enter the number:\n"))
k=int(input("Enter the digit to remove:\n"))
m= int(str(x)[:-k])
print(m)
def smallest(lst):
     for i,x in enumerate(lst):
        if x != '0':
            tmp = lst.pop(i)
            break
     return str(tmp) + ''.join(lst)
if __name__ == '__main__':
     lst = list(str(m))
     lst.sort()
