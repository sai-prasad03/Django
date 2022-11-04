from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','Wolverine',30)
#         mv = cache.get('movie')        
#     return render(request, 'app/course.html', {'fm':mv})

#get_or_set method
# def home(request):
#     mv = cache.get_or_set('fees', 4000, 30)
#     return render(request,'app/course.html',{'fm':mv})

#set_many and get_many method
# def home(request):
#     data = {'name':'saiprasad', 'roll_no':4899}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)

#     return render(request,'app/course.html',{'stu':sv})

#delete cache

# def home(request):
#     cache.delete('roll_no')
#     return render(request,'app/course.html')


#clear method - it will delete your entire cache present in server

def home(request):
    cache.clear()
    return render(request,'app/course.html')