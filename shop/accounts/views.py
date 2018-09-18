from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shopping.models import Order
# Create your views here.

@login_required
def profile(request):
    order_list = request.user.order_set.all()
    # order_list = Order.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{
        'order_list':order_list,
    })