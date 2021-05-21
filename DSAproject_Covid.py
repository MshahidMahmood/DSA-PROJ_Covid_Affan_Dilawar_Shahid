
PATIENT_DATA_SET = {
'ZAIN': [29, 'WEST', 'NOT CRITICAL'],
'ABDULLAH': [87, 'NORTH', 'CRITICAL'],
'HAMID': [32, 'WEST', 'NOT CRITICAL'],
'SAMAD': [45, 'EAST', 'NOT CRITICAL'],
'SANA': [28, 'SOUTH', 'NOT CRITICAL'],
'ALI': [15, 'SOUTH', 'NOT CRITICAL'],
'ALIA': [27, 'SOUTH', 'NOT CRITICAL'],
'RASHID': [68, 'WEST', 'CRITICAL'],
'HAIDER': [21, 'EAST', 'NOT CRITICAL'],
'REHMAN': [33, 'WEST', 'NOT CRITICAL'],
'FARHAN': [39, 'EAST', 'NOT CRITICAL'],
'ASLAM': [72, 'SOUTH', 'CRITCAL'],
'SHEHBAZ': [17, 'WEST', 'NOT CRITICAL'],
'ZAINAB': [41, 'EAST', 'CRITICAL'],
'ALAM': [24, 'NORTH', 'NOT CRITCAL'],
'AFNAN': [30, 'SOUTH', 'CRITICAL'],
'FIAZAN': [34, 'WEST', 'NOT CRITICAL'],
'DANIA': [35, 'EAST', 'NOT CRITICAL'], 
}


def new_patient(PATIENT_DATA_SET):    # THIS FUNCTION HELPS THE OPERATOR ADD A NEW PATIENT TO THE DATA 
    patients_data = []
    name = input('Please enter patients name: ').upper()                                                        
    age = patients_data.append(int(input('Please enter patients age: ')))                                    
    districts = 'South, East, West, North'                                                                      
    region_input = patients_data.append(input('Please choose your district from '+districts+' :').upper())       
    condition_level = patients_data.append(input('Is the patient CRITICAL or NOT CRITICAL: ').upper())       
    
    if type(age)==int:       # checking for possible errors in the input
        pass
    else: 
        return("Please enter valid age")

    if region_input!= 'SOUTH' or 'EAST' or 'WEST' or 'SOUTH':
        return("Please enter valid region. Caution: check for extra spaces")

    if condition_level!='CRITICAL' or 'NOT CRITICAL':
        return("Please enter valid condition level. Caution: check for extra spaces")


    PATIENT_DATA_SET[name] = patients_data       #assigns key (name) and value(date in a list)


#new_patient(PATIENT_DATA_SET)


def display_data(PATIENT_DATA_SET):  # THIS FUNCTION DISPLAYS THE DATA SET
    return PATIENT_DATA_SET

#print(display_data(PATIENT_DATA_SET))

def recommended_hospital(PATIENT_DATA_SET, patient):
    for key, value in PATIENT_DATA_SET.items():
        if key==patient:
            if "CRITICAL" in value:
                if "SOUTH" in value:
                    print("Patient "+key+" is critical and must be rushed to South City Hospital!")
                if "WEST" in value:
                    print("Patient "+key+" is critical and must be rushed to Ziauddin Hospital Nazimabad!")
                if "NORTH" in value:
                    print("Patient "+key+" is critical and must be rushed to Dow Ojha Hospital!")
                if "EAST" in value:
                    print("Patient "+key+" is critical and must be rushed to Aga Khan Hospital!")
            elif "NOT CRITICAL" in value:
                if 'SOUTH' in value:
                    print("Patient "+key+" is not critical and can self isolate. Patient be taken to South City Hospital in case of emergency.")
                if "WEST" in value:
                    print("Patient "+key+" is not critical and can self isolate. Patient be taken to Ziauddin Hospital Nazimabad in case of emergency.")
                if "EAST" in value:
                    print("Patient "+key+" is not critical and can self isolate. Patient be taken to Aga Khan Hospital in case of emergency.")
                if "NORTH" in value:
                    print("Patient "+key+" is not critical and can self isolate. Patient be taken to Dow Ojha Hospital in case of emergency.")

#recommended_hospital(PATIENT_DATA_SET, "ABDULLAH")

def is_critical(PATIENT_DATA_SET):
    critical={}
    for key,values in PATIENT_DATA_SET.items():
        if values[2]=='CRITICAL':
            critical[key]=values        
    number_of_critical_patients = str(len(critical))
    
    print(critical)
    print("Number of critical patients is: "+number_of_critical_patients)
#is_critical(PATIENT_DATA_SET)


def is_not_critical(PATIENT_DATA_SET):
    not_critical={}
    for key,values in PATIENT_DATA_SET.items():
        if values[2]=='NOT CRITICAL':
            not_critical[key]=values        
    number_of_patients = str(len(not_critical))
    
    print(not_critical)
    print("Number of non-critical patients is: "+number_of_patients)

#is_not_critical(PATIENT_DATA_SET)


def most_infected_region(PATIENT_DATA_SET):
    region_frequency={}
    for key,value in PATIENT_DATA_SET.items():
        if value[1]=='SOUTH':
            if 'SOUTH' in region_frequency.keys():
                region_frequency["SOUTH"]+=1
            else:
                region_frequency["SOUTH"]=1

        if value[1]=='NORTH':
            if 'NORTH' in region_frequency.keys():
                region_frequency["NORTH"]+=1
            else:
                region_frequency["NORTH"]=1

        if value[1]=='WEST':
            if 'WEST' in region_frequency.keys():
                region_frequency["WEST"]+=1
            else:
                region_frequency["WEST"]=1

        
        if value[1]=='EAST':
            if 'EAST' in region_frequency.keys():
                region_frequency["EAST"]+=1
            else:
                region_frequency["EAST"]=1
    value_region_frequency=sorted(region_frequency.values())
    temp = []
    for key,value in region_frequency.items():
        if value==max(value_region_frequency):
            temp.append((key,value))
    print(region_frequency)       
    if len(temp)==1:
        print("The most infected region is "+temp[0][0]+" with "+str(temp[0][1])+" cases")
    if len(temp)==2:
        print("The most infected regions are "+temp[0][0]+" and "+temp[1][0]+" with "+str(temp[0][1])+" cases each")
    if len(temp)==3:
        print("The most infected regions are "+temp[0][0]+", "+temp[1][0]+" and "+temp[2][0]+" with "+str(temp[0][1])+" cases each")
    if len(temp)==4:
        print("All regions have "+str(temp[0][1])+" cases")

#most_infected_region(PATIENT_DATA_SET)


#For covid research
def agee(PATIENT_DATA_SET):
    agelist=[]
    for i in  PATIENT_DATA_SET:
        
        v=PATIENT_DATA_SET.get(i)[0]
        if v not in agelist:
            agelist.append(v)
    return agelist
#print(agee(PATIENT_DATA_SET))
bst = {}
keys=agee(PATIENT_DATA_SET)

def insert(bst, key):
    if bst == {}:
        bst['value'], bst['left'], bst['right'] = key, {}, {}
    elif bst != {}:
        if key < bst['value']:
            insert(bst['left'], key)
        elif key > bst['value']:
            insert(bst['right'], key)

def insert_keys(bst, keys):
    for key in keys:
        insert(bst, key)
    return bst

#insert_keys(bst, keys)
#print(insert_keys(bst, keys))

def exist(bst, key):
    if 'value' not in bst:
        return False
    elif bst['value'] == key:
        return True
    elif key < bst['value']:
        return exist(bst['left'], key)
    elif key > bst['value']:
        return exist(bst['right'], key)


bst = insert_keys(bst, keys)
key = 68




#print(exist(bst, key))
def vaccination_age(bst,lsy):
    list_of_age_in_cat=[]

    for i in keys:
        if i >=lsy:
            f=exist(bst, i)
            if f==True:
                list_of_age_in_cat.append(i)
            else:
                pass
    return sorted(list_of_age_in_cat)


age_category=int(input("please input the age actegory you are looking for:"))
print(vaccination_age(bst,age_category))