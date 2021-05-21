import random

# The function Patient Data Set serves as our main patient database from which we will work with
PATIENT_DATA_SET = {
    'ZAIN': [29, 'WEST', 'NOT CRITICAL', 1],
    'ABDULLAH': [87, 'NORTH', 'CRITICAL', 3],
    'HAMID': [32, 'WEST', 'NOT CRITICAL', 4],
    'SAMAD': [45, 'EAST', 'NOT CRITICAL', 5],
    'SANA': [28, 'SOUTH', 'NOT CRITICAL', 3],
    'ALI': [15, 'SOUTH', 'NOT CRITICAL', 2],
    'ALIA': [27, 'SOUTH', 'NOT CRITICAL', 1],
    'RASHID': [68, 'WEST', 'CRITICAL', 4],
    'HAIDER': [21, 'EAST', 'NOT CRITICAL', 3],
    'REHMAN': [33, 'WEST', 'NOT CRITICAL', 5],
    'FARHAN': [39, 'EAST', 'NOT CRITICAL', 4],
    'ASLAM': [72, 'SOUTH', 'CRITCAL', 3],
    'SHEHBAZ': [17, 'WEST', 'NOT CRITICAL', 4],
    'ZAINAB': [41, 'EAST', 'CRITICAL', 3],
    'ALAM': [24, 'NORTH', 'NOT CRITCAL', 3],
    'AFFAN': [30, 'SOUTH', 'CRITICAL', 5],
    'FAIZAN': [34, 'WEST', 'NOT CRITICAL', 1],
    'DANIA': [35, 'EAST', 'NOT CRITICAL', 1]}


# This function helps us to delegate different patients to various hospitals based on their respective medical conditions
def recommended_hospital(PATIENT_DATA_SET, patient):
    for key, value in PATIENT_DATA_SET.items():
        if key == patient:
            if "CRITICAL" in value and PATIENT_DATA_SET.get(key)[3] >= 3:
                if "SOUTH" in value:
                    print(
                        "Patient "+key+" is critical and must be rushed to South City Hospital!")
                if "WEST" in value:
                    print(
                        "Patient "+key+" is critical and must be rushed to Ziauddin Hospital Nazimabad!")
                if "NORTH" in value:
                    print(
                        "Patient "+key+" is critical and must be rushed to Dow Ojha Hospital!")
                if "EAST" in value:
                    print(
                        "Patient "+key+" is critical and must be rushed to Aga Khan Hospital!")
            elif "CRITICAL" in value and PATIENT_DATA_SET.get(key)[3] < 3:
                if "SOUTH" in value:
                    print(
                        "Patient "+key+" is critical and must recieve immediate professional help at South City Hospital!")
                if "WEST" in value:
                    print(
                        "Patient "+key+" is critical and must recieve immediate professional help at Ziauddin Hospital Nazimabad!")
                if "NORTH" in value:
                    print(
                        "Patient "+key+" is critical and must recieve immediate professional help at Dow Ojha Hospital!")
                if "EAST" in value:
                    print(
                        "Patient "+key+" is critical and must recieve immediate professional help at Aga Khan Hospital!")
            elif "NOT CRITICAL" in value and PATIENT_DATA_SET.get(key)[3] < 3:
                if 'SOUTH' in value:
                    print(
                        "Patient "+key+" is not critical and can self isolate. Patient be taken to South City Hospital in case of emergency.")
                if "WEST" in value:
                    print(
                        "Patient "+key+" is not critical and can self isolate. Patient be taken to Ziauddin Hospital Nazimabad in case of emergency.")
                if "EAST" in value:
                    print(
                        "Patient "+key+" is not critical and can self isolate. Patient be taken to Aga Khan Hospital in case of emergency.")
                if "NORTH" in value:
                    print(
                        "Patient "+key+" is not critical and can self isolate. Patient be taken to Dow Ojha Hospital in case of emergency.")
            elif "NOT CRITICAL" in value and PATIENT_DATA_SET.get(key)[3] > +3:
                if 'SOUTH' in value:
                    print(
                        "Patient "+key+" is not critical and should isolate in covid isolation ward at South City Hospital.")
                if "WEST" in value:
                    print(
                        "Patient "+key+" is not critical and should isolate in covid isolation ward at Ziauddin Hospital Nazimabad.")
                if "EAST" in value:
                    print(
                        "Patient "+key+" is not critical and should isolate in covid isolation ward at Aga Khan Hospital.")
                if "NORTH" in value:
                    print(
                        "Patient "+key+" is not critical and should isolate in covid isolation ward at Dow Ojha Hospital.")
# THIS FUNCTION HELPS THE OPERATOR ADD A NEW PATIENT TO THE DATA


def new_patient(PATIENT_DATA_SET):
    patients_data = []
    name = input('Please enter patients name: ').upper()
    age = patients_data.append(int(input('Please enter patients age: ')))
    districts = 'South, East, West, North'
    region_input = patients_data.append(
        input('Please choose your district from '+districts+' : ').upper())
    condition_level = patients_data.append(
        input('Is the patient CRITICAL or NOT CRITICAL: ').upper())
    patient_condition_scale = patients_data.append(
        int(input('Please rate the patients condition from 1 (Bad) to 5 (Worse) : ')))

    # assigns key (name) and value(date in a list)
    PATIENT_DATA_SET[name] = patients_data
    return recommended_hospital(PATIENT_DATA_SET, name)


def display_data(PATIENT_DATA_SET):  # THIS FUNCTION DISPLAYS THE DATA SET
    return PATIENT_DATA_SET


# THIS FUNCTION GIVES US THE NUMBER OF CRITICAL PATIENTS
def number_of_critical(PATIENT_DATA_SET):
    critical = {}
    for key, values in PATIENT_DATA_SET.items():
        if values[2] == 'CRITICAL':
            critical[key] = values
    number_of_critical_patients = str(len(critical))

    print(critical)
    print("Number of critical patients is: "+number_of_critical_patients)


# THIS FUNCTION GIVES US THE NUMBER OF NOT CRITICAL PATIENTS
def number_of_not_critical(PATIENT_DATA_SET):
    not_critical = {}
    for key, values in PATIENT_DATA_SET.items():
        if values[2] == 'NOT CRITICAL':
            not_critical[key] = values
    number_of_patients = str(len(not_critical))

    print(not_critical)
    print("Number of non-critical patients is: "+number_of_patients)


# THIS FUNCTION GIVES US THE MOST INFECTED REGION
def most_infected_region(PATIENT_DATA_SET):
    region_frequency = {}
    for key, value in PATIENT_DATA_SET.items():
        if value[1] == 'SOUTH':
            if 'SOUTH' in region_frequency.keys():
                region_frequency["SOUTH"] += 1
            else:
                region_frequency["SOUTH"] = 1

        if value[1] == 'NORTH':
            if 'NORTH' in region_frequency.keys():
                region_frequency["NORTH"] += 1
            else:
                region_frequency["NORTH"] = 1

        if value[1] == 'WEST':
            if 'WEST' in region_frequency.keys():
                region_frequency["WEST"] += 1
            else:
                region_frequency["WEST"] = 1

        if value[1] == 'EAST':
            if 'EAST' in region_frequency.keys():
                region_frequency["EAST"] += 1
            else:
                region_frequency["EAST"] = 1
    value_region_frequency = sorted(region_frequency.values())
    temp = []
    for key, value in region_frequency.items():
        if value == max(value_region_frequency):
            temp.append((key, value))
    print(region_frequency)
    if len(temp) == 1:
        print("The most infected region is " +
              temp[0][0]+" with "+str(temp[0][1])+" cases")
    if len(temp) == 2:
        print("The most infected regions are " +
              temp[0][0]+" and "+temp[1][0]+" with "+str(temp[0][1])+" cases each")
    if len(temp) == 3:
        print("The most infected regions are " +
              temp[0][0]+", "+temp[1][0]+" and "+temp[2][0]+" with "+str(temp[0][1])+" cases each")
    if len(temp) == 4:
        print("All regions have "+str(temp[0][1])+" cases")


# We have a function age_of_patients where a Vaccination Center is accepting patients of certain ages
def age_of_patients(PATIENT_DATA_SET):
    agelist = []
    for i in PATIENT_DATA_SET:

        v = PATIENT_DATA_SET.get(i)[0]
        if v not in agelist:
            agelist.append(v)
    return agelist


bst = {}
keys = age_of_patients(PATIENT_DATA_SET)


def insert_age(bst, key):  # THIS FUNCTION GENERATES A BINARY TREE WHERE WE HAVE AGES OF THE PATIENTS IN OUR DATABASE ARRANGED FOR OUR EASE
    if bst == {}:
        bst['value'], bst['left'], bst['right'] = key, {}, {}
    elif bst != {}:
        if key < bst['value']:
            insert_age(bst['left'], key)
        elif key > bst['value']:
            insert_age(bst['right'], key)


def insert_keys(bst, keys):  # THIS FUNCTION INSERTS THE AGES IN THE TREE
    for key in keys:
        insert_age(bst, key)
    return bst


def exist(bst, key):  # THIS FUNCTION CHECKS IF A CERTAIN AGE EXISTS OR NOT IN THE TREE
    if 'value' not in bst:
        return False
    elif bst['value'] == key:
        return True
    elif key < bst['value']:
        return exist(bst['left'], key)
    elif key > bst['value']:
        return exist(bst['right'], key)


# THIS FUNCTION HELPS US TO IDENTIFY WHICH AGES ARE ELIGIBLE FOR VACCINATION OR NOT
def vaccination_age(bst):
    age_category = int(
        input("Please input the age category you are looking for: "))
    list_of_age_in_cat = []

    for i in keys:
        if i >= age_category:
            f = exist(bst, i)
            if f == True:
                list_of_age_in_cat.append(i)
            else:
                pass
    return sorted(list_of_age_in_cat)


# (new_patient(PATIENT_DATA_SET))

# print(display_data(PATIENT_DATA_SET))

# number_of_critical(PATIENT_DATA_SET)
# number_of_not_critical(PATIENT_DATA_SET)
# most_infected_region(PATIENT_DATA_SET)
# print(age_of_patients(PATIENT_DATA_SET))

# print(insert_keys(bst, keys))
insert_keys(bst, keys)

print(vaccination_age(bst))
