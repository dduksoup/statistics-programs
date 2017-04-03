# Asks for two lines of input
count = int(input())
numbers = [int(n) for n in input().split()]

# Calculate mean
csum = 0
for i in numbers:
  csum += i
print (csum/count)

# Calculate median
if count % 2 == 0:
  print (((sorted(numbers)[int((count/2)-1)])+(sorted(numbers)[int(count/2)]))/2)
else:
  print (sorted(numbers)[int(round(count/2))])
  
# Calculate mode
md = {j:0 for j in numbers}
for l in numbers:
  md[l] += 1

k = list(md.keys())
v = list(md.values())
clist = []
for a in md:
  if md.get(a) == max(v): clist.append(a)
print (min(clist))

