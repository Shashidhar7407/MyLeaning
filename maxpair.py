
n = int(input())
a = [int(x) for x in input().split()]
product = 0
input_list = sorted(a)
product = max(input_list[0]*input_list[1], input_list[-1] * input_list[-2])
print(product)
