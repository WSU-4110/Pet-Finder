from django.contrib.auth import logout
from django.shortcuts import render
from petManager.models import pets

# Create your views here.
def quiz(request, error=None, info=None, success=None, warning=None):
    context = {'title': 'Home'}
    if error:
        context['error'] = str(error)
    if info:
        context['info'] = str(info)
    if warning:
        context['warning'] = str(warning)
    if success:
        context['success'] = str(success)
    if request.method == 'POST':
        data = request.POST
        print(data)
        petResults = pets.objects.all()
        context = {'title': 'Pet Results'}
        return render(request, 'app/questionnaireManager/results_page.html', {'context': context, 'petresults': petResults})
    return render(request, 'app/questionnaireManager/questionnaire_page.html', {'context': context})

def results(request, error=None, info=None, success=None, warning=None):
    context = {'title': 'Home'}

    if error:
        context['error'] = str(error)
    if info:
        context['info'] = str(info)
    if warning:
        context['warning'] = str(warning)
    if success:
        context['success'] = str(success)
    return render(request, 'app/questionnaireManager/questionnaire_page.html', {'context': context})
