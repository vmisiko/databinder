import random
import os
import pandas as pd
import numpy as np
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import Profile, FormModel, CsvFile
from django.contrib.auth.models import User
import datetime


@receiver(user_signed_up)
def save_profile(sender, **kwargs):
    request = kwargs['request'] 
    user = kwargs['user']
    print(user, request)
    obj = User.objects.get(username= user)

    Profile.objects.create(
        user = user,
        email = obj.email,
        amountD = 0,
        amountS = 0,
        amountB = 0,
    )

    
@receiver(pre_save, sender=FormModel)
def account_update(sender, instance, *args, **kwargs):
    print("account update signal entered")
    instance_id = instance.id
    profile = Profile.objects.get(user=instance.user)
    profile.amountS += 1
    profile.amountB -= 1
    profile.save()

def dob_id_format(dob,gender, id_num):
#     part=f"{dob},{gender},{id_num}"
    dob= str(dob)
    print(dob, gender, id_num)
    dob1= dob.split("/")
    print(dob1)
    year = dob1[2][-2:]
    month = dob1[1]
    day1 = dob1[0]

    day =""
    if int(day1)<10:
        day = "0"+str(day1)
    else:
        day =str(day1)

    dob= year + month + day
    fixed ="1702150"
    id_num ="B00"+id_num
    rand= random.randint(0, 9)
    gender = gender
    part = dob+str(rand)+gender+fixed + "<" + id_num +gender +"<<"
    return str(part)

def name_format(first, middle,last):

    first = str(first).upper()
    middle = str(middle).upper()
    last = str(last).upper()
    part= first +"<"+ middle + "<" +last
    sub = 30 - len(part)
    final=""
    if sub > 0:
        final = part + "<"*sub
    else:
        final = part
    return final


def myrecode(x):
    len_id = len(str(x))
    sub = 8 - len_id
    id =""
    if sub>0:
        id= "0"*sub + str(x)
    else:
        id=str(x)
    return id

@receiver(post_save, sender=CsvFile)
def convert_csv(sender, instance, *args, **kwargs):
    print(instance.user)
    print(instance.csv_file.path)
    # print(instance.csv_file.url)

    path =instance.csv_file.path
    data =pd.read_csv(path)
    data = data.replace(np.nan, '', regex=True)

    data["id_number"] = data["id_number"].apply(myrecode)

    for index, row in data.iterrows():
        first_name =row[1]
        middle_name=row[2]
        last_name = row[3]
        id_num =row[4]
        dob = row[5]
        gender =row[6]
        fixed= "IDKYA2441216280<<3981<<<<<3982"
        dob_id= dob_id_format(dob, gender,id_num)
        name_section = name_format(first_name, middle_name,last_name)
        dobf = datetime.datetime.strptime( dob, "%d/%m/%Y")
        print(index, first_name,middle_name,last_name )
        FormModel.objects.create(
                user=instance.user,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                Id_number=id_num,
                dob=dobf,
                gender=gender,
                fixed=fixed,
                dob_id_section=dob_id,
                name_section=name_section,
            )

        

        
        





