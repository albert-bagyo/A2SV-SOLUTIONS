from collections import OrderedDict
N = int(input())
net_prices = OrderedDict()
for _ in range(N):
    inp = input().split()
    product = " ".join(inp[:-1])
    price = int(inp[-1])
    if not product in net_prices.keys():
        net_prices[product] = 0
    net_prices[product] += price
    
for prod, pri in net_prices.items():
    print(prod, pri)
