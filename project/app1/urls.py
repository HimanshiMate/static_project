from django.urls import path
from .views import home
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',home,name='home'),
  # path('app2/',include('app2/.urls'))
]