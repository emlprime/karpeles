from django.template import RequestContext
from django.shortcuts import render_to_response

from karpeles.content.models import HomeText, PracticeArea, AboutText, Attorney, AttorneyText, PracticeText, ResourceText, ContactText, DisclaimerText

def index(request):
    """Submits the home page information to the URL
    """
    template = "index.html"
    homeText = HomeText.objects.latest()
    practice_areas = PracticeArea.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def site_map(request):
    """ Submits info including practice areas and practice area links to the URL
    """
    template = "site_map.html"
    practice_areas = PracticeArea.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))


def about(request):
    """Submits the about information to the URL
    """
    template = "about.html"
    aboutText = AboutText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def attorneys(request):
    """Submits the attorneys information to the URL
    """
    template = "attorneys.html"
    attorneyText = AttorneyText.objects.latest()
    attorneys = Attorney.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def practice_areas(request):
    """Submits practice area information to the URL
    """
    template = "practice_areas.html"
    practiceText = PracticeText.objects.latest()
    practiceAreas = PracticeArea.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def resources(request):
    """Submits the resource text to the URL
    """
    template = "resources.html"
    resourceText = ResourceText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def contact(request):
    """Submits the latest contact information to the URL
    """
    template = "contact.html"
    contactText = ContactText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def disclaimer(request):
    """ Submits latest disclaimer text to the URL
    """
    template = "disclaimer.html"
    disclaimerText=DisclaimerText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))
