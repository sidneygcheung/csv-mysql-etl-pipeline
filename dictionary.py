rows = """Birmingham,Alabama,AL
Montgomery,Alabama,AL
Huntsville,Alabama,AL
Mobile,Alabama,AL
Kailua,Hawaii,HI
Waipahu,Hawaii,HI
Kanehoe,Hawaii,HI
Mililani Town,Hawaii,HI
Kahului,Hawaii,HI
Ewa Gentry,Hawaii,HI
Boise,Idaho,ID
Meridian,Idaho,ID
Nampa,Idaho,ID
Idaho Falls,Idaho,ID"""

my_dict = {}
city_rows = []

for each in rows.split("\n"):
    # print(each)
    (city, state, code) = each.split(',')
    # city_rows.append(each.split(','))
    state_id = my_dict.get(code, '')
    if state_id == '':
        # insert to state table

        print("city: ", city)
        print("state: ", state)
        print("code: ", code)
        print("insert in state table sql")
        # add to dictionary
        my_dict[code] = 101

    # insert to city table with the state_id
    print("city: ", city)
    print("insert into city table")


print("=====")
print(my_dict)
