from django.shortcuts import render, redirect, get_object_or_404
from formapp.models import StudentInquiry
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.conf import settings
from django.contrib.staticfiles import finders
import os

def index(request):
    if request.method == "POST":
        try:
            student = StudentInquiry(
                student_name=request.POST.get('student_name'),
                dob=request.POST.get('dob'),
                gender=request.POST.get('gender'),
                category=request.POST.get('category'),
                mobile=request.POST.get('mobile'),
                whatsapp=request.POST.get('whatsapp'),
                email=request.POST.get('email'),
                course=request.POST.get('course'),
                father_name=request.POST.get('father_name'),
                occupation=request.POST.get('occupation'),
                annual_income=request.POST.get('annual_income'),
                father_mobile=request.POST.get('father_mobile'),
                mother_name=request.POST.get('mother_name'),
                address=request.POST.get('address'),
                city=request.POST.get('city'),
                district=request.POST.get('district'),
                state=request.POST.get('state'),
                pincode=request.POST.get('pincode'),
                x_percent=request.POST.get('x_percent'),
                x_year=request.POST.get('x_year'),
                x_board=request.POST.get('x_board'),
                xii_stream_percent=request.POST.get('xii_stream_percent'),
                xii_year=request.POST.get('xii_year'),
                xii_board=request.POST.get('xii_board'),
                school_name=request.POST.get('school_name'),
                grad_stream_percent=request.POST.get('grad_stream_percent'),
                college_name=request.POST.get('college_name'),
                university_name=request.POST.get('university_name'),

                src_website=bool(request.POST.get('src_website')),
                src_newspaper=bool(request.POST.get('src_newspaper')),
                src_hoarding=bool(request.POST.get('src_hoarding')),
                src_calling=bool(request.POST.get('src_calling')),
                src_ads=bool(request.POST.get('src_ads')),
                src_other=bool(request.POST.get('src_other')),

                src_other_text=request.POST.get('src_other_text'),
                verified_by=request.POST.get('verified_by'),
                remark=request.POST.get('remark'),
            )
            student.save()
            return redirect('index')  # आपका मौजूदा behaviour बरकरार रखा
        except Exception as e:
            print("Error while saving inquiry:", e)

    obj = StudentInquiry.objects.all().order_by('-created_at')
    return render(request, "index.html", {'obj': obj})


# helper to allow xhtml2pdf to load static files (optional; उपयोगी यदि आप images use करेंगे)
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
    """
    # try staticfiles finders
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            return result
        return result[0]
    # otherwise, try direct filesystem (relative to STATIC_ROOT or MEDIA_ROOT)
    sUrl = settings.STATIC_URL  # Typically /static/
    sRoot = settings.STATIC_ROOT
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # not static/media

    if not os.path.isfile(path):
        return uri
    return path

def enquiry_list(request):
    obj = StudentInquiry.objects.all().order_by('-created_at')
    return render(request, "enquiry_list.html", {'obj': obj})


def enquiry_pdf(request, pk):
    enquiry = get_object_or_404(StudentInquiry, pk=pk)
    html = render_to_string('enquirypdf.html', {'enquiry': enquiry})
    response = HttpResponse(content_type='application/pdf')
    filename = f"enquiry_{enquiry.id}.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # create pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors while generating PDF <pre>' + html + '</pre>')
    return response

def delete_enquiry(request, pk):
    enquiry = get_object_or_404(StudentInquiry, pk=pk)
    enquiry.delete()
    return redirect('enquiry_list')

