from django.shortcuts import render
from .models import News


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Home'})


# Creating Function calc to calculate the tax according to the information provided by the user
def calc(request):
    # Requesting and taking the information from html to our local variable
    married = (request.POST['gender'])
    salary1 = int(request.POST['salary'])
    months = int(request.POST['month'])
    bon = int(request.POST['bonus'])
    expense = int(request.POST['expense'])
    total_salary = (salary1 * months) - bon

    # Calculating tax for Unmarried user
    if married == "married":
        if 45000 < total_salary <= 100000:
            total = ((salary1 * months) + bon)  # Formula to calculate total salary
            res = (1 / 100) * ((salary1 * months) - (bon + expense))  # Formula to calculate tax
            return render(request, 'home.html', {'result': res, 'total': total})

        elif 100000 < total_salary <= 200000:
            total = ((salary1 * months) + bon)
            res = (10 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'result': res, 'total': total})

        elif 200000 < total_salary <= 550000:
            total = ((salary1 * months) + bon)
            res = (20 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'result': res, 'total': total})

        elif 550000 < total_salary <= 2000000:
            total = ((salary1 * months) + bon)
            res = (30 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'total': total, 'result': res})

        elif total_salary > 2000000:
            total = ((salary1 * months) + bon)
            res = (36 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'total': total, 'result': res})

        else:
            return render(request, 'home.html', {'result': "You don't have to pay tax. If your salary is less than "
                                                           "NRS 40,000"})



    # Calculating tax for married user
    else:
        if 40000 < total_salary <= 100000:
            total = ((salary1 * months) + bon)
            res = (1 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'result': res, 'total': total})

        elif 100000 < total_salary <= 200000:
            total = ((salary1 * months) + bon)
            res = (10 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'result': res, 'total': total})

        elif 200000 < total_salary <= 600000:
            total = ((salary1 * months) + bon)
            res = (20 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'result': res, 'total': total})

        elif 600000 < total_salary <= 2000000:
            total = ((salary1 * months) + bon)
            res = (30 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'total': total, 'result': res})

        elif total_salary > 2000000:
            total = ((salary1 * months) + bon)
            res = (36 / 100) * ((salary1 * months) - (bon + expense))
            return render(request, 'home.html', {'total': total, 'result': res})

        else:
            return render(request, 'home.html', {'result': "You don't have to pay tax. If your salary is less than "
                                                           "NRS 40,000"})


# Function to connect the news in News.html
def news(request):
    data = News.objects.all()
    return render(request, 'News.html', {'data': data})
