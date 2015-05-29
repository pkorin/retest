from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext

# Create your views here.


def contact(request):
    c = {}
    c.update(csrf(request))
    errors=[]
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('enter a subject.')
        if not request.POST.get('message',''):
            errors.append('enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('enter a valid e-mail address.')
        if not errors:
            send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    request.POST.get('email','mymaster@qq.com'),
                    ['sendmailuser@163.com'],
                    )
            return HttpResponseRedirect('/polls/thanks/')
    return render_to_response('contact_form.html',{
        'errors':errors,
        'subject':request.POST.get('subject',''),
        'message':request.POST.get('message',''),
        'email':request.POST.get('emal',''),
        },context_instance = RequestContext(request))
 
def thanks(request):
    return render_to_response('thanks.html',{},context_instance =
            RequestContext(request))
