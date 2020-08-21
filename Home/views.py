import random
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, View
from django.shortcuts import render, HttpResponse
from .forms import ModelDetailsForms
from .models import FormModel,Profile, CsvFile
from django.contrib.auth.decorators import login_required

# from Django.models.form

@login_required
def index(request):
    
    profile = Profile.objects.get(user= request.user )
    context ={
        "profile":profile
    }
    
    return render(request, "home.html", context)



class RecordAddView(View):
    def get(self, *args, **kwargs):

        form = ModelDetailsForms()
        profile = Profile.objects.get(user=self.request.user)
        if int(profile.amountB) > 0:
            
            context={
                "form":form,
            }

            return render(self.request, "form.html", context )
        else:
            return render(self.request, "upaid.html")

    def post(self, *args, **kwargs):
 
        form = ModelDetailsForms(self.request.POST or None)
        # print(self.request.POST)
        if form.is_valid():
            user = self.request.user
            first_name = form.cleaned_data.get("first_name")
            middle_name =form.cleaned_data.get("middle_name")
            last_name =form.cleaned_data.get("last_name")
            id_number =form.cleaned_data.get("Id_number")
            dob = form.cleaned_data.get("dob")
            gender = form.cleaned_data.get("gender")
            len_id= len(id_number)
            sub = 8 - int(len_id)  
            if  sub >0:
                id_number= "0"*sub + id_number

            # print(id_number , "this is formated id number")

            fixed= "IDKYA2441216280<<3981<<<<<3982"
            dobid_format= dob_id_format(dob, gender, id_number)
            name_section = name_format(first_name, middle_name, last_name)
            # print(fixed + "\n" +dobid_format + "\n" + name_section)
            record = FormModel.objects.create(
                user=user,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                Id_number=id_number,
                dob=dob,
                gender=gender,
                fixed=fixed,
                dob_id_section=dobid_format,
                name_section=name_section,
            )
            data = {
                "fixed":fixed,
                "dob_id_section":dobid_format,
                "name_section":name_section,
            }

            return JsonResponse(data)
        else:
            # form instance will have errors so we pass it into template
            data = {"errors": form.errors.as_json()}
            return JsonResponse(data)

            # return render(self.request, 'form.html', {'form': form})


def dob_id_format(dob,gender, id):
    year = dob.year
    month = str(dob.month)
    if len(str(month))==1:
        month = "0"+month
    print(month)
    day1 = dob.day
    day =""
    if int(day1)<10:
        day = "0"+str(day1)
    else:
        day= day1

    dob2= str(year)[-2:]
    dob= dob2 + str(month) + str(day)
    fixed ="1702150"
    id ="B00"+id
    rand= str(random.randint(0, 9))
    gender = gender
    part = dob+rand+gender+fixed + "<" + id +gender +"<<"
    return part

def name_format(first, middle,last):

    first = first.upper()
    middle = middle.upper()
    last = last.upper()
    part= first +"<"+ middle + "<" +last
    sub = 30 - len(part)
    if sub > 0:
        final = part + "<"*sub
    return final



def UploadMutiple(request):
    profile = Profile.objects.get(user=self.request.user)
    if int(profile.amountB) > 0:
            

        return render(request, "upload.html", {})
    else:
        return render(self.request, "upaid.html")


class UploadMutiple(View):
    def get(self, *args, **kwargs):

        profile = Profile.objects.get(user=self.request.user)
        if int(profile.amountB) > 0:
            
            return render(self.request, "upload.html", {} )

        else:
            
            return render(self.request, "upaid.html")

    def post(self, *args, **kwargs):
        user = self.request.user
        csv_file = self.request.FILES["file"]

        csv = CsvFile.objects.create(
            user = user,
            csv_file = csv_file
        )
        
        return render(self.request, "upload.html", {} )

         

class ListFiles(ListView):
    model = FormModel
    paginate_by = 20
    template_name = "listview.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-id')