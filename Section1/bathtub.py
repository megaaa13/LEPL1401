import math
water_vol = 0
filled_time = 80/11
int_filled_time = math.ceil(filled_time)
for i in range(0, int_filled_time) :
    water_vol = water_vol + 12 - 1