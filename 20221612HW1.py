class Item:
    def __init__(self, name, vendor, category, price, cost, weight):
        self.name = name
        self.vendor = vendor
        self.category = category
        self.price = price
        self.cost = cost
        self.weight = weight

    def increase_cost(self, rate):
        self.cost *= (1 + rate)

    def profit(self) :
        return self.price - self.cost



# 2

item1 = Item("포테이토칩","농심","과자류", 1800, 1300, 300)
item2 = Item("액츠파워젤", "피죤", "세탁세제류", 20770, 13500, 4.2)
item3 = Item("대천김 도시락김 5g(54봉)", "케이앤비컴퍼니", "식품류", 18300, 10000, 300)

items = [item1, item2, item3]

# 3
item3.increase_cost(0.15)

# 4
total_profit = 0
for item in items:
    total_profit += item.profit()

print("총 판매이익금: ", total_profit)


