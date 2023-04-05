from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Doctor, Report, Appointment ,new_user
from .forms import UserRegisterForm, UserLoginForm, ReportForm, AppointmentForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



def home(request):
    return render(request, 'home.html')

@login_required
def view_reports(request):
    reports = Report.objects.filter(user=request.user)
    return render(request, 'report_list.html', {'reports': reports})

@login_required
def upload_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, 'Your report has been uploaded successfully!')
            return redirect('view_reports')
    else:
        form = ReportForm()
    return render(request, 'upload_report.html', {'form': form})

@login_required
def delete_selected_reports(request):
    if request.method == 'POST':
        report_ids = request.POST.getlist('report_ids')
        Report.objects.filter(id__in=report_ids).delete()
    return redirect('view_reports')

@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'view_appointments.html', {'appointments': appointments})

@login_required
def book_appointment(request,pk):
    doctor = Doctor.objects.get(id=pk)
    return render(request,'book_appointment.html',{'Doctor':doctor})

@login_required
def book_appointment_save(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            doctor_id = request.POST.get('doctor')
            doctor = Doctor.objects.get(id=doctor_id)
            appointment.doctor = doctor
            appointment.user = request.user
            appointment.save()
            messages.success(request, f'Your appointment has been booked for {appointment.date} at {appointment.time}.')
            return redirect('view_appointments')
        else:
            messages.error(request, 'There was an error in the form. Please check the fields and try again.')
    else:
        form = AppointmentForm()
        doctors = Doctor.objects.all()
        context = {'form': form, 'doctors': doctors}
        return render(request, 'book_appointment.html', context)

@login_required
def delete_selected_appointments(request):
    if request.method == 'POST':
        appointment_ids = request.POST.getlist('appointment_ids')
        Appointment.objects.filter(id__in=appointment_ids).delete()
    return redirect('view_appointments')

@login_required
def view_doctors(request):
    specialty_search = request.GET.get('specialty')
    name_search = request.GET.get('name')
    city_search = request.GET.get('city')
    if name_search is not None or specialty_search is not None or city_search is not None:
        doctors = Doctor.objects.filter(name__icontains = name_search,specialty__icontains = specialty_search,address__icontains=city_search)
        return render(request, 'doctor_list.html', {'doctors': doctors})
    else:
        doctors = Doctor.objects.all()
        return render(request, 'doctor_list.html', {'doctors': doctors})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST.get('username')
        user_name = new_user.objects.filter(username=username)
        if user_name:
           return render(request,'error.html')
        else:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in.')
                return redirect('user_login')
        
    else:
        form = UserRegisterForm()
    return render(request, 'user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})



@login_required
def user_home(request):
    reports = Report.objects.filter(user=request.user)
    appointments = Appointment.objects.filter(user=request.user)

    
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('user_home')
    else:
        form = ReportForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('user_home')
    else:
        form = AppointmentForm()

    context = {
        'reports': reports,
        'appointments': appointments,
        'report_form': form,
        'appointment_form': form
    }
    return render(request, 'user_home.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your details has been updated ! please login again')
            return redirect('user_login')
    else:
        form =  UserRegisterForm(instance=request.user)
    return render(request, 'update.html', {'form': form})





def user_logout(request):
    logout(request)
    return redirect('user_login')



class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    template_name = 'reset_password.html'
    success_url = 'password_reset_done'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = 'password_reset_complete'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'





