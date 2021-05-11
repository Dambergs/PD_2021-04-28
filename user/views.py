from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View, FormView, DetailView
from user.models import User
from user.forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class AddUserView(FormView):

    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response


class GetUserView(View):

    def get(self, request):
        return render(
            template_name='user.html',
            request=request,
            #context=context,
        )

    def post(self, request):
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)

        context = {
        'user': user,
        }


class DeleteUser(View):
    def get(self, request, user_id):

        return render(
            template_name='index.html',
            request=request
        )

    def post(self, request, user_id):
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        user.delete()

        return HttpResponse(f'Deleted {user.username}')


class EditUser(View):
    def get(self, request, user_id):
        return render(
            template_name='edit_user.html',
            request=request
        )

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        username = request.POST['name']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        context = {
            'user': user,
        }

        return render(
            template_name='index.html',
            request=request,
            context=context,
        )



