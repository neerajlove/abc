if __name__ == '__main__':
       names = [ ]
       scores = [ ]
for _ in range(int(input())):
  name = input()
  names.append(name)
  score = float(input())
  scores.append(score)
print(names)
print(scores)
test = [ ]
for c in scores:
  test.append(c)
test.sort()
second = test[2] 
index = 0
print(second)
for i in scores:
  if second == scores[index]:
     a = index
     milgaye = (names[a])
  
     index += 1
print(milgaye)
  

# print(names[a])
 #print(scores[a])

  

   



  