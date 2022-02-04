from django.shortcuts import render

# Create your views here.

from .models import Teacher, Information, Subject
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_teachers = Teacher.objects.all().count()

    num_teachers_available = Information.objects.filter(status__exact='a').count()

    num_subjects = Subject.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_teachers': num_teachers,
        'num_teachers_available': num_teachers_available,
        'num_subjects': num_subjects,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 10

class TeacherDetailView(generic.DetailView):
    model = Teacher

class SubjectListView(generic.ListView):
    model = Subject
    paginate_by = 10

class SubjectDetailView(generic.DetailView):
    model = Subject

class MeetingTeachersByUserListView(LoginRequiredMixin,generic.ListView):
    model = Information
    template_name ='catalog/meetings_of_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Information.objects.filter(student=self.request.user).filter(status__exact='r').order_by('to_date')
