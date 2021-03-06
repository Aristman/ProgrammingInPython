from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from .models import Feedback


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['text', 'grade', 'subject']
    success_url = '/feedback/add/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class FeedbackListView(LoginRequiredMixin, ListView):
    model = Feedback

    def get_queryset(self):
        if self.request.user.is_staff:
            return Feedback.objects.all()
        return Feedback.objects.filter(author=self.request.user)