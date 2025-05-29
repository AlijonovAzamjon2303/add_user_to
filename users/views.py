from django.shortcuts import redirect, render

from users.forms import UserForm


def view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)  # MUHIM!
        if form.is_valid():
            form.save()
            return redirect('add')
    else:
        form = UserForm()
    return render(request, 'users/form.html', {'form': form})

def home(request):
    return render(request, "users/form.html")