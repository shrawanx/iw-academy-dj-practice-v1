from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse("Hi, from Home")


# /profile/<username>/
def profile(request, username):
    data = {
        'ram': 'Ram Bahadur',
        'hari': 'Hari Bahadur',
        'shyam': 'Shyam Bahadur',
    }

    full_name = data.get(username)

    if not full_name:
        # return HttpResponseNotFound("The username doesnt exists")
        return HttpResponse("The username doesnt exists", status=404)

    string_data = f"Your full name is: {full_name}"

    return HttpResponse(string_data)


def profile_json(r, username):
    data = {
        'ram': 'Ram Bahadur',
        'hari': 'Hari Bahadur',
        'shyam': 'Shyam Bahadur',
    }

    full_name = data.get(username)

    if not full_name:
        # return HttpResponseNotFound("The username doesnt exists")
        return HttpResponse("The username doesnt exists", status=404)

    dict_data = {
        'full_name': full_name
    }

    return JsonResponse(dict_data)


def int_converter_view(r, int_data):
    print("int data is", int_data)
    print(type(int_data))
    try:
        _ = int(int_data)
    except ValueError:
        return HttpResponse("Something is wrong", status=404)

    return HttpResponse("OK OK OK")


def debug_request(request):
    print("Request method:", request.method)
    print("Scheme:", request.scheme)
    print("Headers:", request.headers)
    print("REQUEST GET:", request.GET)

    return HttpResponse("Ok from debug")


def test_args_kwargs(request, *args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
    data = kwargs['data']

    string_data = "Ok " * data
    return HttpResponse(string_data)
