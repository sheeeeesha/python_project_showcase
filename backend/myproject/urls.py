from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.user_login, name='login'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_project/', views.create_project, name='create_project'),
    #path('join_project/', views.join_project, name='join_project'),
    path('available_projects/<str:project_id>/join/', views.send_join_request, name='send_join_request'),
    path('available_projects/', views.available_projects, name='available_projects'),
    path('created_projects/', views.user_projects, name='user_projects'),
    path('join_requests/', views.user_join_requests, name='user_join_requests'),
    path('join_request/<int:join_request_id>/accept/', views.accept_join_request, name='accept_join_request'),
    path('join_request/<int:join_request_id>/reject/', views.reject_join_request, name='reject_join_request'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),

    # Add more URL patterns as needed
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
def create_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("--------is valid", form.is_valid())
        print(form.error_messages)
        print(form.data["username"])
        if form.is_valid():
            user = form.save()
            username = form.data["username"]
            cust = Customer.objects.create(
                user=user,
                name=username
                
            )
            cust.save()
            messages.success(request, "Successfully Registered")
            return redirect('login')
    context = {'form': form}
    return render(request, 'store/Registration.html', context)
    """