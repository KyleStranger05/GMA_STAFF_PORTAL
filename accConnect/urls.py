from django.contrib import admin
from django.conf.urls import url
from django.urls import path , include
from accounts import views as v
from main import views as views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts
    path('login/home/' , views.home , name = 'home'),
    path('', v.register , name='register'),
    path('' , include('django.contrib.auth.urls') , name = 'login'),

    #Trial Balance
    path('KyletrbSettings' , views.KyletrbSettings , name = 'KyletrbSettings'),
    path('Kyletrb', views.Kyletrb , name = 'Kyletrb'),
    path('KyletrbMonth', views.KyletrbMonth , name = 'KyletrbMonth'),
    path('pdf' , views.printToPdf, name='printToPdf'),
    path('XLS' , views.printToXLS , name='printToXLS'),
    path('trb_Monthly' , views.trb_Monthly , name='trb_Monthly'),

    #Settings
    path('settings', views.settingsHome , name='settingsHome'),
    path('ns' , views.newSetting , name='newSetting'),
    path('accConnect/setting/<int:settings_pk>', views.viewSettings, name='viewSettings' ),

]
