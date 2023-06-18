from django.shortcuts import render

from music_school.models import Student


# Create your views here.

def show_index_page(request):
    context = {"Students": Student.objects.all()}
    return render(request, "index.html", context=context)


def show_student_page(request, student_id):
    context = {"profile": Student.objects.get(pk=student_id)}
    return render(request, "profile.html", context=context)


def show_register_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sure_name = request.POST.get("sure_name")
        age = request.POST.get("age")
        course = request.POST.get("course")
        musical_instrument = request.POST.get("musical_instrument")
        progress = request.POST.get("progress")
        payment = request.POST.get("payment")

        Student.objects.create(Name=name,
                               Sure_Name=sure_name,
                               Age=age,
                               Course=course,
                               Musical_Instrument=musical_instrument,
                               Progress=progress,
                               Payment=payment)

    return render(request, "register.html")


def show_student_edit_page(request, student_id):
    Profile = Student.objects.get(pk=student_id)
    context = {"profile": Profile}
    if request.method == "POST":
        name = request.POST.get("name")
        sure_name = request.POST.get("sure_name")
        age = request.POST.get("age")
        course = request.POST.get("course")
        musical_instrument = request.POST.get("musical_instrument")
        progress = request.POST.get("progress")
        payment = request.POST.get("payment")

        Profile.Name = name
        Profile.Sure_Name = sure_name
        Profile.Age = age
        Profile.Course = course
        Profile.Musical_Instrument = musical_instrument
        Profile.Progress = progress
        Profile.Payment = payment
        Profile.save()

    return render(request, "edit.html", context=context)
