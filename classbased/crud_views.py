from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import UserInfoModelForm
from .models import UserInfo


class Create(CreateView):
    form_class = UserInfoModelForm
    template_name = 'classbased/create.html'
    # success_url = '/c/list/'   # classbased:list
    success_url = reverse_lazy('classbased:list')

    # def get_success_url(self):
    #     return reverse('classbased:list')


class List(ListView):
    template_name = 'classbased/list.html'
    context_object_name = 'data'
    model = UserInfo
    # queryset = UserInfo.objects.all()
    #
    # def get_queryset(self):
    #     if self.request.user.id==1:
    #         return UserInfo.objects.all()
    #     else:
    #         return UserInfo.objects.filter(is_active=True)


class Detail(DetailView):
    model = UserInfo
    template_name = 'classbased/detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'user_obj'


class Update(UpdateView):
    form_class = UserInfoModelForm
    pk_url_kwarg = 'id'
    success_url = '/c/list/'
    model = UserInfo
    template_name = 'classbased/update.html'

    def form_valid(self, form):
        print("form is valid")
        # my logic
        return super().form_valid(form)


class Delete(DeleteView):
    model = UserInfo
    success_url = '/c/list/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
