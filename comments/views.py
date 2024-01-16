from django.shortcuts import render
from .forms import UserForm
from .models import Comments


# Create your views here.
def main(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['name']
            email = user_form.cleaned_data['email']
            comment = user_form.cleaned_data['comment']

            commentaries = Comments()
            commentaries.name = name
            commentaries.email = email
            commentaries.comment_text = comment
            commentaries.save()

            print(name)
        else:
            print('123')
    user_form = UserForm(request.POST)
    view_comments = Comments.objects.all()
    return render(request, 'main.html', {'form': user_form, 'comments': view_comments })
