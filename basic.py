x = [2, 4, 5]


def get_pay(work_hour):
    pay_gross = work_hour * 13
    pay_net = pay_gross * (1 - .12)
    return pay_net

john = get_pay(20)
james = get_pay(56)
mary = get_pay(130)

print(f"John salary ${john} by the end of the month.")

print('++'*30)

# def get_expected_cost(beds, baths):
#     value = 80000 + 30000 * beds + 10000 *baths
#     return value

# house1 = get_expected_cost(2, 3)
# house2 = get_expected_cost(3, 2)
# house3 = get_expected_cost(3, 3)
# house4 = get_expected_cost(3, 4)
# print(house1)
# print(house2)
# print(house3)

def get_expected_cost(beds, baths, has_basement):
    value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
    return value

new1 = get_expected_cost(2, 1, True)
print(new1)

print('++'*30)

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total = sqft_walls + sqft_ceiling
    needed = total / sqft_per_gallon
    round_needed = round(needed)
    cost = round_needed * cost_per_gallon
    return cost

print(get_cost(594, 288, 400, 95))

print('++'*30)

def cost_gold_shop(engraving, solid_gold):
    # cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    # return cost
    if solid_gold:
        return 100 + 10 * len(engraving)
    else:
        return 50 + 7 * len(engraving)

gold = cost_gold_shop('08/10/2000', False)
print(gold)


def tax_calculation(id_number):
    if id_number < 1800:
        tax = .13 * id_number
    elif id_number < 2500:
        tax = .22 * id_number
    else:
        tax = .45 * id_number
    return tax

john = tax_calculation(1560)
print(f'john ${john} salary')
mary = tax_calculation(2200)
print(f'mary *{mary} salary')
paul = tax_calculation(8000)
print(f'paul *{paul} salary')
isaac = tax_calculation(1860)
print(f'Isaac *{isaac} salary')

print('++'*30)

def get_score_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

score1 = get_score_grade(60)
print(score1)


def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = num_gallons / 1000 * 5
    elif num_gallons <= 22000:
        bill = num_gallons / 1000 * 6
    elif num_gallons <= 30000:
        bill = num_gallons / 1000 * 7
    else:
        bill = num_gallons / 1000 * 10
    return bill

gallons1 = get_water_bill(83300)
print(gallons1)