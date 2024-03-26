from django.shortcuts import render

def home(request):
    # Your home view logic here
    return render(request, 'calculator/home.html')

def calc_view(request):
    result = None  # Initialize result variable
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operator = request.POST.get('operator')

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Division by zero is not allowed'
        else:
            result = 'Invalid operator'

    # Render the template with result, if any
    return render(request, 'calculator/calculator.html', {'result': result})

def calculate_view(request):
    # Your calculate_view logic here
    return render(request, 'calculator/calculator.html')
