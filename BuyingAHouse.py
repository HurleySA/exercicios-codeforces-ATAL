n, m, k = [int(x) for x in input().split()]
housePrices = [int(x) for x in input().split()]

ladoEsq = 0;
for i in range((m - 1), 0, -1):
  if(housePrices[i-1] <= k and housePrices[i-1] != 0):
    ladoEsq = (m - i);
    break;
ladoDir = 0;
for i in range((m), n, 1):
  if(housePrices[i ] <= k and housePrices[i] != 0):
    ladoDir = (i - m + 1);
    break;
if(ladoEsq == 0 or ladoDir == 0):
  final = max(ladoEsq, ladoDir);
else:
  final = min(ladoEsq, ladoDir);

print(final*10)