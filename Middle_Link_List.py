head = [5, 2, 3, 4, 6, 9, 10]
size = len(head)
ans = []
if size % 2 == 0:
   size = (size / 2) + 1
   size = int(size)
   for i in range(len(head)//2):
         ans.append(head[size+i-1])
   print(ans)
else:
   size = size / 2
   size = int(size)
   for i in range(len(head)//2+1):
      ans.append(head[size+i])
   print(ans)