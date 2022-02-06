t = int(input())
finalRes = [];
while(t):
  string = input();
  string += "#"
  chars = [];
  j = 0;
  while(j < len(string) - 1):
    if(string[j] == string[j+1]):
      j+=2;
    else:
      if(string[j] not in chars):
        chars.append(string[j])
      j+=1;

  res = '';
  chars.sort(); 
  for char in chars:
    res += char;
  
  finalRes.append(res);
  t -= 1;
    

for res in finalRes:
  print(res); 