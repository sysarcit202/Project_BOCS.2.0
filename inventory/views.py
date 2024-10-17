from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction, IntegrityError
from .models import InStock
from datetime import datetime  
from django.core.exceptions import ValidationError

def dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)

def update(request):
    context = {
        'title': 'Update'
    }
    return render(request, 'dashboard/update.html', context)

def inventory(request):
    context = {
        'title': 'Inventory'
    }
    return render(request, 'inventory/inventory.html')

def instock(request):
    context = {           
        'title': 'Instock'
    }
    return render(request, 'inventory/instock.html', context)

def insertuser(request):
    if request.method == 'POST':
        # Log received POST data
        print(f"Received POST data: {request.POST}")

        vCompID = request.POST.get('CompID')
        vDid = request.POST.get('Did')
        vComp = request.POST.get('Comp')
        vBtype = request.POST.get('Btype')
        vColl = request.POST.get('Coll')  # dd-mm-yyyy
        vExp = request.POST.get('Exp')    # dd-mm-yyyy

        # Print extracted values for debugging
        print(f"Extracted values - CompID: {vCompID}, Did: {vDid}, Comp: {vComp}, Btype: {vBtype}, Coll: {vColl}, Exp: {vExp}")

        # Ensure all fields are provided
        if not all([vCompID, vDid, vComp, vBtype, vColl, vExp]):
            messages.error(request, "All fields are required.")
            return redirect('instock')

        try:
            # Convert vColl and vExp from dd-mm-yyyy to date object
            vColl = datetime.strptime(vColl, '%d-%m-%Y').date()
            vExp = datetime.strptime(vExp, '%d-%m-%Y').date()

            with transaction.atomic():
                # Create InStock entry
                instock_entry = InStock.objects.create(
                    CompID=vCompID,
                    Did=vDid,
                    Comp=vComp,
                    Btype=vBtype,
                    Coll=vColl,
                    Exp=vExp
                )

                print(f"Inserted InStock Entry: {instock_entry}")

                # Check if the entry was saved successfully
                if instock_entry.pk:
                    messages.success(request, "Entry successfully inserted!")
                else:
                    messages.error(request, "Failed to insert entry. Please try again.")
                    return redirect('instock')

                return redirect('instock')  # Redirect to the instock page

        except ValueError:
            # Handle incorrect date format
            messages.error(request, "Incorrect date format. Please use DD-MM-YYYY.")
            return redirect('instock')

        except IntegrityError as e:
            # Handle database errors
            print(f"IntegrityError occurred: {e}")
            messages.error(request, f"Transaction failed: {e}. Please try again.")
            return redirect('instock')

        except Exception as e:
            # Catch all unexpected errors
            print(f"An unexpected error occurred: {e}")
            messages.error(request, f"An unexpected error occurred: {e}. Please try again.")
            return redirect('instock')

    return render(request, 'authentication/login.html')

def used(request):
    context = {
        'title': 'Used'
    }
    return render(request, 'inventory/used.html')

def donor(request):
    context = {
        'title': 'Donor'
    }
    return render(request, 'inventory/donor.html')