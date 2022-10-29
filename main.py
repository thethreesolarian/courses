import math

count_boxes = int(input())
roll_of_wallpaper = int(input())
price_of_gloves = float(input())
price_of_brush = float(input())

price_of_boxes = count_boxes * 21.50
price_of_wallpaper = roll_of_wallpaper * 5.20
price_of_gloves = math.ceil(roll_of_wallpaper * 0.35)
price_of_brush =  math.floor(count_boxes * 0.48)
total_sum = price_of_boxes + price_of_wallpaper + price_of_gloves + price_of_brush
value_of_supplies = total_sum / 15
print("This delivery will cost")
print(f"{value_of_supplies} lv.")