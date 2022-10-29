import math

# COUNTS
box_count = int(input("Box count: "))
wallpaper_count = int(input("Wallpaper count: "))
gloves_price = float(input("Gloves price: "))
brush_price = float(input("Brush price: "))

# PRICES
box_price = 21.50 * box_count
wallpaper_price = 5.20 * wallpaper_count
gloves_price = math.ceil(wallpaper_count * 0.35) * gloves_price
brush_price = math.floor(box_count * 0.48) * brush_price

total = (gloves_price + brush_price + box_price + wallpaper_price) / 15

print(f"This delivery will cost {total:.2f} lv.")