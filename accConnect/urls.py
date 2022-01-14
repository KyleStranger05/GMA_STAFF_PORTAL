from django.contrib import admin
from django.urls import path , include
from accounts import views as v
from main import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pov:yourmom', views.yourmom , name='yourmom'),

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
    path('accConnect/printReports/<int:reports_pk>' , views.printReports , name='printReports'),

    #Print Each Report
    path('accConnect/trialBalanceMonthly/<int:reports_pk>' , views.trialBalanceMonthly, name='trialBalanceMonthly'),
    path('accConnect/trialBalanceYearly/<int:reports_pk>' , views.trialBalanceYearly, name='trialBalanceYearly'),
    path('accConnect/incomeStatementMonthly/<int:reports_pk>', views.incomeStatementMonthly, name='incomeStatementMonthly'),
    path('accConnect/incomeStatementYearly/<int:reports_pk>', views.incomeStatementYearly, name='incomeStatementYearly'),

    #Credit Control
    path('accConnect/AgeAnalysisCSV/<int:reports_pk>', views.AgeAnalysisCSV, name='AgeAnalysisCSV'),
    path('accConnect/InterestChargeCSV/<int:reports_pk>', views.InterestChargeCSV, name='InterestChargeCSV'),
    path('creditControlHome1231217581' , views.creditControlHome , name='creditControlHome'),
    path('creditControl', views.creditControl, name='creditControl'),
    path('interestBatches', views.interestBatches, name='interestBatches'),

    #Customer Updates
    path('accConnect/printViewCustomers/<int:reports_pk>', views.printViewCustomers , name='printViewCustomers'),
    path('complexCustomerList' , views.complexCustomerList , name='complexCustomerList'),
    path('customerDetailsHome' , views.customerDetailsHome , name='customerDetailsHome'),
    path('cdcComplex' , views.customerDetails , name='customerDetails'),
    path('accConnect/DisplayCustomers/<int:reports_pk>' , views.DisplayCustomers , name='DisplayCustomers'),
    path('viewDetailsHome' , views.viewDetailsHome , name='viewDetailsHome'),
    path('viewSingleCustomer', views.viewSingleCustomer , name='viewSingleCustomer'),

    #Journal Entry
    path('journentry', views.journalEntry , name='journalEntry'),

]
