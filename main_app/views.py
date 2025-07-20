from django.shortcuts import render

# # Create your views here.
# # Import HttpResponse to send text-based responses
# from django.http import HttpResponse - can remove because we're not using HttpResponse anymore

# Define the home view function
def home(request):
    # Send a simple HTML response
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1> About Groovasana </h1>')
    return render(request, 'about.html')

class Todo:
    def __init__(self, name, description, day, priority, tags, esttime):
        self.name = name
        self.description = description
        self.day = day
        self.priority = priority
        self.tags= tags
        self.esttime = esttime

todos= [
    Todo('Morning Routine', 'Brush teeth, take meds, make bed', 'today', 'urgent', 'self-care', '10min'),
    Todo('Final Project', 'Complete Groovasana', 'July 29th', 'urgent', 'bootcamp', '24 hours'),
    Todo('Job Upgrade', 'Update resume and apply to new jobs', 'today', 'low', 'professional', '1 hour')
]
def todos_index(request):
    #render the todos/index.html template with the todos data
    return render(request, 'todos/index.html', {'todos':todos})
