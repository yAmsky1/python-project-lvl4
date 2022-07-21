from django.shortcuts import render
from django.utils.translation import gettext as _


# PROJECT_NAME = _('Task-manager')
# WELCOME_TEXT = _("welcome to the task-manager app!")


def index(request):

    return render(request, 'index.html')
