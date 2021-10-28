from django.contrib import admin
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
    path('Kyletrb', views.Kyletrb , name = 'Kyletrb'),
    path('pdf' , views.printToPdf, name='printToPdf'),

    #Settings
    path('settings', views.settingsHome , name='settingsHome'),
    path('ns' , views.newSetting , name='newSetting'),
    path('accConnect/setting/<int:setting_pk>', views.viewSettings, name='viewSettings' ),

    #ReportsHome
    path('reportsHome' , views.reportsHome, name='reportsHome'),
    path('creditControl' , views.creditControl, name='creditControl'),
    path('accConnect/printReports/<int:reports_pk>' , views.printReports , name='printReports'),

    #Print Each Report
    path('accConnect/trialBalanceMonthly/<int:reports_pk>' , views.trialBalanceMonthly, name='trialBalanceMonthly'),
    path('accConnect/trialBalanceYearly/<int:reports_pk>' , views.trialBalanceYearly, name='trialBalanceYearly'),
    path('accConnect/incomeStatementMonthly/<int:reports_pk>', views.incomeStatementMonthly, name='incomeStatementMonthly'),
    path('accConnect/incomeStatementYearly/<int:reports_pk>', views.incomeStatementYearly, name='incomeStatementYearly'),
    path('accConnect/AgeAnalysisCSV/<int:reports_pk>', views.AgeAnalysisCSV, name='AgeAnalysisCSV'),

]
