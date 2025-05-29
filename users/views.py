from django.shortcuts import redirect, render

from users.forms import UserForm
from users.models import User

from services.add import add_user

BASE_URL = "http://192.168.91.129"
USERNAME = "admin"
PASSWORD = "azamjon23032025"

def view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)  # MUHIM!
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            add_user(BASE_URL, USERNAME, PASSWORD, "5015", user.name, user.image.path)

            return redirect('add')
    else:
        form = UserForm()
    return render(request, 'users/form.html', {'form': form})

def home_view(request):
    users = User.objects.all()
    return render(request, 'users/home.html', {'users': users})