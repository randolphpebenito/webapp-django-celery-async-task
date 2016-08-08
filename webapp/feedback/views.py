from django.views.generic.edit import FormView
from .forms import FeedbackForm


class FeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(FeedbackView, self).form_valid(form)
