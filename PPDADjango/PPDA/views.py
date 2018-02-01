from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.

from .models import dataUpload
from .forms import dataForm

def myFormView(request):
	# Handle file upload
	if request.method == 'POST':
		form = dataForm(request.POST, request.FILES)
		if form.is_valid():
			newDoc = dataUpload(docFile = request.FILES['docFile'])
			newDoc.epsilon = form.cleaned_data['epsilon']
			newDoc.sensitivity = form.cleaned_data['sensitivity']
			newDoc.save()
		# Redirect to the same page after POST
		return HttpResponseRedirect("")

	else:
		form = dataForm() # A empty, unbound form
		return render(request, 'myForm.html', {'form': form})
