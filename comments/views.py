from django.shortcuts import render
from .forms import UserForm
from .models import Comments
import re


# Create your views here.
def main(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():

            name = user_form.cleaned_data['name']
            email = user_form.cleaned_data['email']
            comment = user_form.cleaned_data['comment']
            parent_comment_id = user_form.cleaned_data.get('parent_comment_id')

            if parent_comment_id:
                parent_comment = Comments.objects.get(id=parent_comment_id)
            else:
                parent_comment = None

            validated_data = data_validation(name, comment)

            if validated_data:
                commentaries = Comments()
                commentaries.name = name
                commentaries.email = email
                commentaries.comment_text = comment
                commentaries.parent_comment = parent_comment
                commentaries.save()

                if parent_comment:
                    commentaries.is_reply = True
                    commentaries.save()

                    parent_comment.have_replies = True
                    parent_comment.save()

    user_form = UserForm(request.POST)
    view_comments = Comments.objects.order_by('-id')
    print(view_comments)
    return render(request, 'main.html', {'form': user_form, 'comments': view_comments})


def data_validation(name, comment):
    regex_name = r'^[a-zA-Z0-9/-]+$'
    if len(name) > 100 and len(comment) > 3000:
        return False
    else:
        if not re.match(regex_name, name):
            return False
        return True

