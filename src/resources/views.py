from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import smart_str
from .forms import resourceForm
from django.core.urlresolvers import reverse
# Create your views here.
from .models import resource
from django.http import HttpResponseRedirect
from datetime import datetime   

def resource_create(request):
	form = resourceForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = resource(upload=request.FILES['upload'], title=request.POST.get("title"), description=request.POST.get("description"))
		instance.save()
		messages.success(request, "Successfully Created")
		#return HttpResponseRedirect("http://127.0.0.1:8000/resources/detail/%s" %str(instance.id))
		return HttpResponseRedirect(reverse('detail', kwargs={'id': instance.id}))
	context = {
		"form": form,
	}
	return render(request, "resource_form.html", context)	

def resource_detail(request, id=None):
	instance = get_object_or_404(resource, id = id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "resource_detail.html", context)

def resource_list(request):
	queryset = resource.objects.all()
	context = {
		"object_list": queryset,
		"title": "Resources",
	}

	return render(request, "resource_list.html", context)

def resource_update(request, id = None):
	instance = get_object_or_404(resource, id = id)
	form = resourceForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = resource(upload=request.FILES['upload'], title=request.POST.get("title"), description=request.POST.get("description"), id=instance.id, timestamp = instance.timestamp, updated = datetime.now())
		instance.save()
		messages.success(request, "Saved")
		return HttpResponseRedirect(reverse('detail', kwargs={'id': instance.id}))
	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "resource_form.html", context)

def resource_delete(request, id = None):
	instance = get_object_or_404(resource, id = id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("list")

def download(request, id = None):
	# Create the HttpResponse object with the appropriate PDF headers.
    instance = get_object_or_404(resource, id = id)
    fd = open(str(instance.upload))
    response = HttpResponse(fd, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"'%((instance.title) + ".pdf")

    # Create the PDF object, using the response object as its "file."
    #p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    #p.showPage()
    #p.save()
    return response


