from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
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
			# newDoc.save()
			newDoc.epsilon = form.cleaned_data['epsilon']
			newDoc.sensitivity = form.cleaned_data['sensitivity']
			newDoc.save()
			# data = form.save(commit = False)
			# data.epsilon = request.epsilon
			# data.sensitivity = request.sensitivity
			# data.save()
		# Redirect to the document list after POST
		# return HttpResponseRedirect(reverse('PPDA.views.myFormView'))
		return HttpResponse("Hello World")

	else:
		form = dataForm() # A empty, unbound form
		# Load documents for the list page
		# documents = dataUpload.objects.all()

		# Render list page with the documents and the form
		# return render(request, 'myForm.html', {'documents': documents, 'form': form})
		return render(request, 'myForm.html', {'form': form})