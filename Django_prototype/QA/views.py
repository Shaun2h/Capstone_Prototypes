from django.shortcuts import render
from django.http import HttpResponse
from .QuestionForm import QuestionForm, InsertForm
import inspect
import QA.models
# Create your views here.
all_in_model = dir(QA.models)  # get all in model.py
model_classes = {}
baseclass = None
for i in all_in_model:
    if inspect.isclass(getattr(QA.models, i)) and i != "BaseClass":  # check if it is a class
        model_classes[i] = getattr(QA.models, i)
    if i == "BaseClass":
        baseclass = getattr(QA.models, i)


def basic(request):
    error = "Make Req."
    if request.method == "POST":
        question = QuestionForm(request.POST)
        if question.is_valid():
            data = question.cleaned_data
            return asked(request, data["company"], data["region"], data["city"], data["product"],1)
        else:
            error = "ERROR"
    context = {"form": QuestionForm, "error_msg": error}
    return HttpResponse(render(request, "form.html", context=context))


def asked(request, company, region, city, product, num):
    try:
        target_class = model_classes[company]
        main_classes = baseclass.objects.filter(region=region, city_ID=city, product_ID=product)
        requested_instance = None
        for c in main_classes:
            temp = target_class.objects.filter(information=c)
            if temp:
                requested_instance = temp
                break
        if not main_classes:
            raise QA.models.models.ObjectDoesNotExist("Item does not exist")
        if not requested_instance:
            raise QA.models.models.ObjectDoesNotExist("Item does not exist")
        if len(requested_instance) > 1:
            raise QA.models.models.ObjectDoesNotExist("Multiple of same entry. Check Database")
            # there should only be one of this item. If there are multiple raised from the filter,
            # we request you check the database.
        requested_instance = requested_instance[0]  # it's essentially a list object here.
        context = {"company": requested_instance.getEQ(),
                   "region": requested_instance.information.region,
                   "city": requested_instance.information.city_ID,
                   "product": requested_instance.information.product_ID,
                   "target": requested_instance.information.target}
        if num == 1:
            return HttpResponse(render(request, "client_view.html", context=context))
        if num == 2:
            return HttpResponse(render(request, "Template1.html", context=context))
        if num == 3:
            return HttpResponse(render(request, "Template2.html", context=context))
        if num == 4:
            return HttpResponse(render(request, "Template3.html", context=context))
        if num == 5:
            return HttpResponse(render(request, "Template1.html", context=context))


    except (KeyError, QA.models.models.ObjectDoesNotExist) as ex:
        return HttpResponse(str(ex))


def insert_req(request):
    error = ""
    if request.method == "POST":
        insertreq = InsertForm(request.POST)
        if insertreq.is_valid():
            data = insertreq.cleaned_data
            return insert_succ(data["company"], data["region"], data["city"], data["product"],
                               data["urlline"])
        else:
            error = "ERROR"
            form = insertreq
    else:
        form = InsertForm
    context = {"form": form, "error_msg": error, "notice": "INSERTION"}
    return HttpResponse(render(request, "insertform.html", context=context))


def insert_succ(company, region, city, product, url):
    try:
        target_class = model_classes[company]
        url = "http://127.0.0.1:8000/models/"+str(company)+"/"+str(region)+"/"+str(city)+"/"+str(product)+"/"+url
        main_classes = baseclass.objects.filter(region=region, city_ID=city, product_ID=product)
        for main_class in main_classes:  # get the main classes that turned up.
            if(target_class.objects.filter(information=main_class)) > 0:
                # look through all companies.
                raise KeyError("An existing product takes up this slot. Please Remove it first.")

        attempt = baseclass(region=region, city_ID=city, product_ID=product,
                            target=url)  # generate the base class.

        attempt.save()  # save.
        subhead = target_class(information=attempt)
        subhead.save()
        return HttpResponse("Successfully added..." + subhead.information.target)
    except KeyError as ex:
        print(ex)
        return HttpResponse("Failure!<br>" + str(ex))


def del_req(request):
    error = ""
    if request.method == "POST":
        insertreq = QuestionForm(request.POST)
        if insertreq.is_valid() and len():
            data = insertreq.cleaned_data
            return del_succ(data["company"], data["region"], data["city"], data["product"])
        else:
            error = "ERROR"
            form = insertreq
    else:
        form = QuestionForm
    context = {"form": form, "error_msg": error, "notice": "DELETION"}
    return HttpResponse(render(request, "insertform.html", context=context))


def del_succ(company, region, city, product):
    try:
        target_class = model_classes[company]  # in case. you need to reference the actual class.
        attempt = baseclass.objects.filter(region=region, city_ID=city, product_ID=product)
        attempt.delete()  # save.
        return HttpResponse("Successfully REMOVED...")
    except (KeyError, QA.models.models.ObjectDoesNotExist) as ex:
        print(ex)
        return HttpResponse("Failure!<br>" + str(ex))


def test1(request):
    error = "Make Req."
    if request.method == "POST":
        question = QuestionForm(request.POST)
        if question.is_valid():
            data = question.cleaned_data
            return asked(request, data["company"], data["region"], data["city"], data["product"], 2)
        else:
            error = "ERROR"
    context = {"form": QuestionForm, "error_msg": error}
    return HttpResponse(render(request, "form.html", context=context))


def test2(request):
    error = "Make Req."
    if request.method == "POST":
        question = QuestionForm(request.POST)
        if question.is_valid():
            data = question.cleaned_data
            return asked(request, data["company"], data["region"], data["city"], data["product"], 3)
        else:
            error = "ERROR"
    context = {"form": QuestionForm, "error_msg": error}
    return HttpResponse(render(request, "form.html", context=context))

def test3(request):
    error = "Make Req."
    if request.method == "POST":
        question = QuestionForm(request.POST)
        if question.is_valid():
            data = question.cleaned_data
            return asked(request, data["company"], data["region"], data["city"], data["product"], 4)
        else:
            error = "ERROR"
    context = {"form": QuestionForm, "error_msg": error}
    return HttpResponse(render(request, "form.html", context=context))
