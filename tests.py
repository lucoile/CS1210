#### Calculates pay based on hours and rate
##def computePay(h, r):
##    try:
##        h = int(h)
##        r = int(r)
##        
##        if h <= 40:
##            pay = h * r
##            print(pay)
##        elif h > 40:
##            pay = (40 * r) + ((h - 40) * (r * 1.5))
##            print(pay)
##    except:
##        print('Please enter a numeric value')
##
##hours = input('Enter hours: ')
##rate = input('Enter rate: ')
##
##computePay(hours,rate)

## random
##import random
##
##for i in range(10):
##    x = random.randint(0,10)
##    print(x)

#### Find how many times each letter occurs in a word
##word = 'brontosaurus'
##d = dict()
##for c in word:
##    if c not in d:
##        d[c] = 1
##    else:
##        d[c] = d[c] + 1
##print(d)

##word = 'brontosaurus'
##d = dict()
##for c in word:
##    d[c] = d.get(c, 0) + 1
##print(d)

#### print dictionary alphabetically
##counts = {'chuck' : 1 , 'annie' : 42, 'jan': 100}
##lst = list(counts.keys())
##print(lst)
##lst.sort()
##for key in lst:
##    print(key, counts[key])


#### Sort a dictionary by values
##d = {'a':10, 'b':1, 'c':22}
##l = list()
##
##for key, val, in d.items():
##    l.append((val, key))
##    
##l.sort(reverse = True)
##print(l)

#### Print characters of a string backwards
##fruit = 'banana'
##index = len(fruit) - 1
##while 0 <= index < len(fruit):
##    print(fruit[index])
##    index = index - 1




