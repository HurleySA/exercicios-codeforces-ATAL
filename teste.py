t = int(input());
while(t):
  inputStr = input();
  listChar = set();
  j = 0;
  if(len(inputStr) == 1):
    print(inputStr[0])
  else:
    for i in range(0, (len(inputStr) - 1), 1):
      if(i+j < len(inputStr) - 1):
        print(i,j,i+j,i+j+1, inputStr[i])
        print(i,j,i+j,i+j+1, inputStr[i+j])
        print(i,j,i+j,i+j+1, inputStr[i+j+1])
        if(inputStr[i+j]== inputStr[i+j+1]):
          listChar.add(inputStr[i+j]);
          print(listChar)
          j+=1;
    if(inputStr[i+1] != inputStr[i] and len(listChar) > 0):
      print(i, inputStr[i+1])
      listChar.remove(inputStr[i+1])
    print(i,j)
    print(listChar)



