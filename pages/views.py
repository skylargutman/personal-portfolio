from django.shortcuts import render

def home(request):
    from portfolio.models import Project
    featured = Project.objects.filter(featured=True)
    return render(request, 'pages/home.html', {'featured': featured})

def about(request):
    skills = [
        'C', 'C++', 'Python', 'ROS2', 'ESP32', 'FreeRTOS',
        'FPGA', 'Linux', 'Git', 'SolidWorks', 'Raspberry Pi',
        'Jetson Nano', 'BLE', 'Nginx', 'Django', 'Docker'
    ]
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
