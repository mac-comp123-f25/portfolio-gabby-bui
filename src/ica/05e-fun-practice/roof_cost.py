def rect_area(wid,len):
    area = float(wid)*float(len)
    return area

def roof_cost(area,sqf_cost):
    roof_cost = float(area)*float(sqf_cost)
    return roof_cost


def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

estimate_green_roof(10,10,10)