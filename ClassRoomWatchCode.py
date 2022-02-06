n = input()
x = max(0, int(n)-81);
numPossiveis = [];
while(x <= int(n)):
  totalDigitos = sum(int(i) for i in str(x));
  if(x + totalDigitos == int(n)):
    numPossiveis.append(x);
  x +=1;

print(len(numPossiveis))
if(len(numPossiveis) > 0):
  sorted(numPossiveis);
  for key in numPossiveis:
    print(key)

  
