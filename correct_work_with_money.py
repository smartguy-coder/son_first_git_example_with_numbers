from decimal import Decimal

# print(Decimal(str(30.3)))

cottage_cheese_price = 140.32
cottage_cheese_price = Decimal(str(cottage_cheese_price)).quantize(Decimal('0.01'))
cottage_cheese_quantity = 2.641
cottage_cheese_quantity = Decimal(str(cottage_cheese_quantity)).quantize(Decimal('0.001'))
cottage_cheese_cost = cottage_cheese_quantity * cottage_cheese_price
cottage_cheese_cost = Decimal(str(cottage_cheese_cost)).quantize(Decimal('0.01'))

blackberry_price = 60
blackberry_price = Decimal(str(blackberry_price)).quantize(Decimal('0.01'))
blackberry_quantity = 0.743
blackberry_quantity = Decimal(str(blackberry_quantity)).quantize(Decimal('0.001'))
blackberry_cost = blackberry_quantity * blackberry_price
blackberry_cost = Decimal(str(blackberry_cost)).quantize(Decimal('0.01'))

total_cost = blackberry_cost + cottage_cheese_cost
print(total_cost)
