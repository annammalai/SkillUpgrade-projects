from django.shortcuts import render
import random

def home(request):
    return render(request, 'guessing_game/home.html')

def play_game(request):
    if request.method == 'POST':
        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)
        try:
            # Get the user's guess from the form
            guess = int(request.POST['guess'])
            if guess == random_number:
                result = "Congratulations! You guessed the correct number."
            elif guess < random_number:
                result = "Your guess is too low. Try again!"
            else:
                result = "Your guess is too high. Try again!"
        except ValueError:
            result = "Please enter a valid number."
        return render(request, 'guessing_game/result.html', {'result': result})
    else:
        return render(request, 'guessing_game/home.html')
