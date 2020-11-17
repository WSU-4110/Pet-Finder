from django.contrib.auth import logout
from django.shortcuts import render


# Create your views here.
def questions(request, error=None, info=None, success=None, warning=None):
    context = {'title': 'Home'}
    logout(request)
    if error:
        context['error'] = str(error)
    if info:
        context['info'] = str(info)
    if warning:
        context['warning'] = str(warning)
    if success:
        context['success'] = str(success)
    return render(request, 'app/questionnaireManager/questionnaire.html', {'context': context})
