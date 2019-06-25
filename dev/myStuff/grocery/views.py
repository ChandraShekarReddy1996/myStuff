from django.http import HttpResponse
from grocery.models import user,products,bookings
from rest_framework.decorators import api_view
from django.core.validators import validate_email

import datetime


def index(request):
    return HttpResponse("Hello, User You're at the grocerry index.")

@api_view(['POST'])
def Registration(request):

    email1 = request.data.get('email')

    try:
            validate_email(email1)
            valid_email = True
    
    except :

        return HttpResponse("{message : 'Please Enter Valid Email'}")


    if((user.objects.filter(email = email1)).count() != 0):
        return HttpResponse("{message : 'User Already Registered'}")

    user1 = user(
        name = request.data.get('name'),
        last_name = request.data.get('last_name'),
        email = request.data.get('email'),
        mobile = request.data.get('mobile'),
        place = request.data.get('place'),
        user_type = request.data.get('user_type'),
        password = request.data.get('password')
    )

    user1.save()

    return HttpResponse(user1)


@api_view(['POST'])
def Login(request):

    is_user = user.objects.filter(
        email = request.data.get('email')).filter(password = request.data.get('password')).count()
    
    if is_user == 0 :
        return HttpResponse("{message : 'User Not Found !'}")

    elif is_user == 1:
        user1 = user.objects.filter(
        email = request.data.get('email')).filter(
        password = request.data.get('password')).get()

        return HttpResponse(f'Welcome {user1.name}')

    else:
        return HttpResponse("{message : 'Something Went Wrong'}")


@api_view(['POST'])
def add_items(request):
    is_eligible = user.objects.filter(
    email = request.data.get('email')).filter(
    user_type = 2).count()

    if(is_eligible == 0):

        return HttpResponse("{message : No privileges found for the user to add items}")

    item1 = products(
    product_name = request.data.get('name'),
    product_type = request.data.get('type'),
    product_owner = request.data.get('email')
    )

    item1.save()

    return HttpResponse(f"{request.data.get('name')} is added sucessfully")


@api_view(['POST'])
def order_items(request):

    is_item_found = products.order.filter(id = request.data.get('product_id')).count()

    if is_item_found != 1 :
        return HttpResponse("{Please Kidly re verify the product that you need}")
    
    item = products.order.filter(id = request.data.get('product_id')).get()

    booking = bookings(
        user = request.data.get('user'),
        booking_date = datetime.datetime.now(),
        booking_place = request.data.get('location'),
        booking_receiver =  item.product_owner,
        price = request.data.get('price')
    )

    booking.save()

    return HttpResponse('Booking Completed')
