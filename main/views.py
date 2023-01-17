from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from authentication.views import login_request
from main.models import doctor, hospital, appointment
from authentication.models import additionalUserInfo, User


# Create your views here.


def homepage(request):
    return render(request, "main/home.html")


def unregis_view(request):
    return render(request, "main/unregis_view.html")


def update_pat(request, pk):
    if request.method == "POST":

        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        phone_no = request.POST["phone"]

        user = User.objects.get(id=pk)
        add = additionalUserInfo.objects.get(user_id=pk)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        add.phone_no = phone_no

        user.save()
        add.save()
    return redirect("main:patient",pk = pk)


def edit_info_patient(request, pk):
    user = User.objects.get(id=pk)
    add = additionalUserInfo.objects.get(user_id=pk)

    context = {"users": user, "addi": add}

    return render(request, "main/edit_info_patient.html", context)


def patient(request, pk):

    appoint_list = appointment.objects.all().filter(patient_id=pk)
    context = {"app": appoint_list}
    return render(request, "main/patient.html", context)


def appoint(request):
    query = doctor.objects.all()
    all_data = doctor.objects.all()
    query2 = hospital.objects.all()

    if request.method == "GET":
        data = request.GET.get("all")
        if data != None and data != "allItem":
            query = doctor.objects.filter(
                Q(name__icontains=data)
                | (Q(depart__icontains=data))
                | (Q(hos_name__hos_name__icontains=data))
            )
        elif data == "allItem":
            query = all_data

    dpt = [
        "Allergists",
        "Dermatologists",
        "Ophthalmologists",
        "gynecologists",
        "Cardiologists",
    ]

    if request.method == "POST":
        hos_name = request.POST.get("hos")
        department = request.POST.get("dept")
        doc_name = request.POST.get("doc")
        user = request.POST.get("user")
        date = request.POST.get("date")
        exist = appointment.objects.all().filter(date=date, doctor_id=doc_name).exists()
        if exist == False:
            app = appointment(
                doctor_id=doc_name, patient_id=user, date=date, time="NULL"
            )
            app.save()
            messages.success(request, "Your appointment is on request")
        else:
            messages.error(request, "You can take appointment of a doctor on same date")

    context = {
        "doctor": query,
        "hospital": query2,
        "department": dpt,
        "all_data": all_data,
    }

    return render(request, "main/appoint.html", context)


def hos_doc_list(request):
    query = doctor.objects.all()

    context = {"all_data": query}
    return render(request, "main/hos_doc_list.html", context)


# --------------------------doctor-----------------------------------#
def Hospital_admin_accp(request, pk):

    if request.method == "POST":
        time = request.POST["time"]
        saved = appointment.objects.get(id=pk)
        saved.time = time
        saved.status = "accepted"
        saved.save()
    return HttpResponseRedirect(reverse("main:Hospital_admin"))


def Hospital_admin(request, name):
    query2 = appointment.objects.all().filter(doctor_id__hos_name__hos_name= name)

    context = {"app": query2}

    return render(request, "main/Hospital_admin.html", context)


def register_doc(request):

    if request.method == "POST":
        name = request.POST.get("name")
        department = request.POST.get("department")
        hospital_name = request.POST.get("hospital")
        degree = request.POST.get("degree")
        date = request.POST.get("date")

        re_doc = doctor(
            name=name,
            depart=department,
            hos_name=hospital.objects.get(hos_name=hospital_name),
            date=date,
            degree=degree,
        )
        re_doc.save()

    queryset = hospital.objects.all().order_by("hos_name")
    dpt = [
        "Allergists",
        "Dermatologists",
        "Ophthalmologists",
        "gynecologists",
        "Cardiologists",
    ]
    return render(
        request, "main/regi_doc.html", context={"models": queryset, "department": dpt}
    )


def edit_doc(request):

    query = doctor.objects.all()

    context = {"all_data": query}
    return render(request, "main/edit_doc_info.html", context)


def deleteDoc(request, pk):
    doc = doctor.objects.get(id=pk)
    doc.delete()
    return HttpResponseRedirect(reverse("main:edit_doc_info"))


def updateDoc(request, pk):

    mymember = doctor.objects.get(id=pk)

    queryset = hospital.objects.all().order_by("hos_name")
    dpt = [
        "Allergists",
        "Dermatologists",
        "Ophthalmologists",
        "gynecologists",
        "Cardiologists",
    ]
    context = {"mymember": mymember, "models": queryset, "department": dpt}

    return render(request, "main/update.html", context)


def updaterecord(request, pk):
    if request.method == "POST":

        name = request.POST["name"]
        department = request.POST["department"]
        hospital_name = request.POST["hospital"]
        degree = request.POST["degree"]
        date = request.POST["date"]

        member = doctor.objects.get(id=pk)
        member.name = name
        member.depart = department
        member.degree = degree
        member.hos_name = hospital.objects.get(hos_name=hospital_name.id)
        member.date = date

        member.save()
    return HttpResponseRedirect(reverse("main:edit_doc_info"))
