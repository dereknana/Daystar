from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from time import sleep
from .models import Sitter, Baby, Payment, ProcurementItem, Notification, Activity




def delete_sitter(request, sitter_id):
    sitter = get_object_or_404(Sitter, pk=sitter_id)
    sitter.delete()
    return redirect('view_sitters')

# def add_babies():
#     pass


def redirect_to_dashboard(request):
    return redirect('home')


def add_baby(request):
    sitters = Sitter.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        location = request.POST.get('location')
        person_bringing_baby = request.POST.get('person_bringing_baby')
        time_of_arrival = request.POST.get('time_of_arrival')
        parents_names = request.POST.get('parents_names')
        period_of_stay = request.POST.get('period_of_stay')
        baby_number = request.POST.get('baby_number') 
        sitter_assigned_to = request.POST.get('sitter')

        # Automatically setting a fee based on the period_of_stay
        if period_of_stay == 'Half Day':
            fee_in_ugx = 10000
        else:# That's when period_of_stay == Full Day
            fee_in_ugx = 15000

            
        # Create a new Baby object
        new_baby = Baby(
            name=name,
            gender=gender,
            age=age,
            location=location,
            person_bringing_baby=person_bringing_baby,
            time_of_arrival=time_of_arrival,
            parents_names=parents_names,
            fee_in_ugx=fee_in_ugx,
            period_of_stay=period_of_stay,
            baby_number=baby_number,  # Assign 'baby_number' retrieved from the form
            sitter_assigned_to=sitter_assigned_to
        )
        new_baby.save()


        sitter_assigned_to = Sitter.objects.get(id=sitter_assigned_to)


        new_payment = Payment(
            sitter = sitter_assigned_to,
            baby = new_baby,
            payment_type = period_of_stay,
            amount = fee_in_ugx,
            date = time_of_arrival
        )

        new_payment.save()

        # Add account Balance
        sitter_assigned_to.account_balance += fee_in_ugx
        sitter_assigned_to.save()

        new_notification = Notification(
            type = "True",
            message = f"{name} assigned to {sitter_assigned_to}"

        )
        new_notification.save()



        new_activity = Activity(
            sitter_name = sitter_assigned_to,
            payment_amount = fee_in_ugx,
            baby_name = name,
            baby_parent = parents_names
        )

        new_activity.save()


        messages.success(request, f'Successfully Added a {name}!')
        # Sleep function is used here just for demonstration purposes
        # You might not need it in your actual code
        sleep(3)
        return redirect('view_babies')
    

    else:      
        # return render(request, 'add_baby.html')
        return render(request, 'add_baby.html', {'sitters': sitters})



def add_sitter(request):
    if request.method == 'POST':
        # Extract form data from the request
        name = request.POST.get('name')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        education_level = request.POST.get('education_level')
        contacts = request.POST.get('contacts')
        on_duty = bool(request.POST.get('on_duty'))  # Convert to boolean
        account_balance = float(request.POST.get('account_balance'))  # Convert to float

        # Create a new Sitter object
        new_sitter = Sitter(
            name=name,
            location=location,
            gender=gender,
            education_level=education_level,
            contacts=contacts,
            on_duty=on_duty,
            account_balance=account_balance
        )
        new_sitter.save()  # Save the new sitter object to the database
        return redirect('view_sitters')  # Redirect to a success page or URL
    else:
        return render(request, 'add_sitter.html')



def delete_baby(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    baby.delete()
    return redirect('view_babies')


# def auth(request):
#     if request.method == 'POST' and request.POST.get('username') == "suma" and request.POST.get('password') == "@password":
#         return redirect('home')
#     else:
#         messages.error(request, 'Wrong Credentials. Try again!')
#         sleep(3)
#         # return redirect('auth')
#     return render(request, home)



def home(request):

    baby_count = Baby.objects.count()
    sitter_count = Sitter.objects.count()
    all_babies = Baby.objects.all()
    all_sitters = Sitter.objects.all()
    notifications =  Notification.objects.all()
    activities = Activity.objects.all()
    payments = Payment.objects.all()

    content = {
        'baby_count': baby_count,
        'sitter_count': sitter_count,
        'babies_data': all_babies,
        'sitters_data': all_sitters,
        'notifications': notifications,
        'activities': activities,
        'payments': payments
    }
    # get data from db
    return render(request, 'home.html', content)


def view_babies(request):
    all_babies = Baby.objects.all()


    content = {
        'babies': all_babies
    }
    return render(request, 'babies.html', content)




def view_sitters(request):
    all_sitters = Sitter.objects.all()

    content = {
        'sitters': all_sitters
    }

    return render(request, 'sitters.html', content)
