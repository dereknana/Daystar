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
        # Retrieve form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        location = request.POST.get('location')
        person_bringing_baby = request.POST.get('person_bringing_baby')
        time_of_arrival = request.POST.get('time_of_arrival')
        parents_names = request.POST.get('parents_names')
        period_of_stay = request.POST.get('period_of_stay')
        baby_number = request.POST.get('baby_number') 
        sitter_assigned_to_id = request.POST.get('sitter')  # Use the sitter's ID

        # Automatically setting a fee based on the period_of_stay
        if period_of_stay == 'half-day':
            fee_in_ugx = 10000
        else:  # That's when period_of_stay == Full Day
            fee_in_ugx = 15000

        # Create a new Baby object
        new_baby = Baby.objects.create(
            name=name,
            gender=gender,
            age=age,
            location=location,
            person_bringing_baby=person_bringing_baby,
            time_of_arrival=time_of_arrival,
            parents_names=parents_names,
            fee_in_ugx=fee_in_ugx,  # Use the dynamically determined fee
            period_of_stay=period_of_stay,
            baby_number=baby_number,
            sitter_assigned_to=sitter_assigned_to_id  # Use the sitter's ID
        )

        # Fetch the sitter assigned to the baby
        sitter_assigned_to = Sitter.objects.get(id=sitter_assigned_to_id)

        # Update the sitter's account balance
        sitter_assigned_to.account_balance += fee_in_ugx
        sitter_assigned_to.save()

        # Create a new Payment object
        new_payment = Payment.objects.create(
            sitter=sitter_assigned_to,
            baby=new_baby,
            payment_type=period_of_stay,
            amount=fee_in_ugx,
            date=time_of_arrival
        )

        # Create a new Notification object
        new_notification = Notification.objects.create(
            type="True",
            message=f"{name} assigned to {sitter_assigned_to.name}"  # Use sitter's name
        )

        # Create a new Activity object
        new_activity = Activity.objects.create(
            sitter_name=sitter_assigned_to.name,  # Use sitter's name
            payment_amount=fee_in_ugx,
            baby_name=name,
            baby_parent=parents_names
        )

        # Display success message
        messages.success(request, f'Successfully Added a {name}!')

        # Sleep function is used here just for demonstration purposes
        # You might not need it in your actual code
        sleep(3)
        return redirect('view_babies')

    else:
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



def view_baby(request, baby_id):
    baby = get_object_or_404(Baby, pk=baby_id)
    sitter_assigned_to = Sitter.objects.get(id=baby.sitter_assigned_to)

    content = {
        'baby': baby,
        'sitter_assigned_to': sitter_assigned_to,
        'other_sitters':  Sitter.objects.all(),

    }
    return render(request, 'view_baby.html', content)





def edit_baby(request, baby_id):
    # Retrieve the existing Baby object from the database
    baby = Baby.objects.get(id=baby_id)
    sitter_assigned_to = Sitter.objects.get(id=baby.sitter_assigned_to)


    if request.method == 'POST':
        # Update the Baby object with the data submitted in the form
        baby.name = request.POST['name']
        baby.gender = request.POST['gender']
        baby.age = request.POST['age']
        baby.location = request.POST['location']
        baby.time_of_arrival = request.POST['time_of_arrival']
        baby.parents_names = request.POST['parents_names']
        # baby.fee_in_ugx = request.POST['fee_in_ugx']
        baby.period_of_stay = request.POST['period_of_stay']
        baby.sitter_assigned_to = request.POST['sitter']

        if request.POST['period_of_stay'] == 'half-day':
            baby.fee_in_ugx = 10000
        else:  # That's when period_of_stay == Full Day
            baby.fee_in_ugx = 15000


        # Save the updated Baby object to the database
        baby.save()

        # Redirect to a success page or view
        return redirect('view_babies')

    # Render the edit baby form template with the existing data
    return render(request, 'view_baby.html', {'baby': baby})







def view_sitters(request):
    all_sitters = Sitter.objects.all()
    content = {
        'sitters': all_sitters,
    }

    return render(request, 'sitters.html', content)





def procurement(request):
    return render(request, 'procurement.html')


