n = input()

total = 0;
numPossiveis = [];

for num in range(int(n), -1, -1):
  totalDigitos = sum(int(i) for i in str(num));
  if((num + totalDigitos) == int(n)):
    numPossiveis.append(num);

print(len(numPossiveis))
if(len(numPossiveis) > 0):
  sorted(numPossiveis);
  for key in numPossiveis:
    print(key)

  
