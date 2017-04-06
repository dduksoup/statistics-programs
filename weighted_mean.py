nsum = 0 #numerator, sum of values multiplied by respective weights
wsum = 0 #denominator, sum of weight values
ith = 0 #iterator

count = list(range(int(input())))
values = list(map(int,input().split()))
weights = list(map(int,input().split()))


for i in count:
  nsum += int(values[ith]) * int(weights[ith])
  wsum += int(weights[ith])
  ith += 1
print (round(1.0*nsum/wsum,1))
