from django.shortcuts import render,redirect,get_object_or_404
from .models import Rating,Dish,Reservation
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.db.models import Avg  
from django.urls import reverse

# Create your views here.
def food(request):
    dishs = Dish.objects.all()

    for dish in dishs:
         avg_rating=Rating.objects.filter(dish=dish).aggregate(avg=Avg('stars'))['avg']
         dish.avg_rating=round(avg_rating,1)if avg_rating else 0
    context={
        'dishs':dishs,
        'categories' : Dish.objects.values_list('category', flat=True).distinct()

    }
    return render(request,'food.html',context)

def chef(request):
     dishs = Dish.objects.all()

     for dish in dishs:
         avg_rating=Rating.objects.filter(dish=dish).aggregate(avg=Avg('stars'))['avg']
         dish.avg_rating=round(avg_rating,1)if avg_rating else 0
     context={
        'dishs':dishs,
        'categories' : Dish.objects.values_list('category', flat=True).distinct()

    }
     return render(request,'chef.html',context)

def about(request):
        return render(request,'about.html')

def home(request):
        return render(request,'home.html')

def log(request):
      if request.method == 'POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                  login(request,user)
                  return redirect('home')
            else:
                  messages.error(request,'Eror in your login')
                  return redirect('log')
      return render(request, 'log.html')

def rate(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish_id')
        if not dish_id:
            messages.error(request, "لم يتم إرسال معرف الطبق.")
            return redirect('food')  # أو أي صفحة مناسبة

        dish = get_object_or_404(Dish, id=dish_id)
        username = request.POST.get('username')
        comment = request.POST.get('comment')
        rating = request.POST.get('rate')

        Rating.objects.create(name=username, comment=comment, stars=rating, dish=dish)
        messages.success(request, 'شكرا على تقيمك لنا')
        return redirect(f'/allrating/?dish_id={dish_id}')

    # عند فتح الصفحة بـ GET
    dish_id = request.GET.get('dish_id')
    dish = Dish.objects.filter(id=dish_id).first()

    return render(request, 'rate.html', {
        'dishes': Dish.objects.all(),
        'selected_dish': dish
    })

def allrating(request):
  
  dish_id=request.GET.get('dish_id')

  if not dish_id:
        messages.error(request, 'لم يتم تحديد الطبق لعرض تقييماته.')
        return redirect('rate')  # أو أي صفحة مناسبة

  else:
        dish_id=request.GET.get('dish_id')
        context={
            'dish':get_object_or_404(Dish,id=dish_id),
            
            'rates':Rating.objects.filter(dish_id=dish_id)
      }
        return render(request,'allrating.html',context)
  



def reservation(request):
    if request.method == 'POST':
        dish_id = request.POST.get('dish_id')
        dish = get_object_or_404(Dish, id=dish_id)

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        guests = request.POST.get('guests')
        date = request.POST.get('date')
        time = request.POST.get('time')
        notes = request.POST.get('notes')

        Reservation.objects.create(
            name=name,
            phone=phone,
            guests=guests,
            date=date,
            time=time,
            notes=notes,
            dish=dish
        )
        messages.success(request, 'تم حجز الطاولة بنجاح!')

        if 'go_to_payment' in request.POST:
            return redirect(f"{reverse('stripe')}?dish_id={dish.id}")

        return redirect('reservation')
    
    dish_id = request.GET.get('dish_id')
    selected_dish = get_object_or_404(Dish, id=dish_id)

    return render(request, 'reservation.html', {'selected_dish': selected_dish})



def stripe(request):
    dish_id = request.GET.get('dish_id') or request.POST.get('dish_id')
    dish = get_object_or_404(Dish, id=dish_id) if dish_id else None
    if request.method == 'POST':
        # استقبل بيانات الدفع
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        card = request.POST.get('card')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')

        # ممكن هنا تعمل تحقق بسيط لو عاوز
        if card and cvv and len(card) == 19 and len(cvv) == 3:
            # معناه الدفع ناجح في النظام الوهمي
            messages.success('thanks sur')
        else:
            return render(request, 'stripe.html', {'error': 'Invalid card details','dish':dish})

    return render(request, 'stripe.html',{'dish':dish})