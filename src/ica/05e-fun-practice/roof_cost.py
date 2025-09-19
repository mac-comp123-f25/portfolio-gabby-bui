def rect_area(wid,len):
    area = wid*len
    return area

def roof_cost(area,sqf_cost)
    
    return area*sqf_cost


def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

estimate_green_roof(10,10,10)