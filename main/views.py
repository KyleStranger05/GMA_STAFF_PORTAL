import numpy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import pyodbc
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import SettingsClass , ComplexListClass
from .forms import SettingsForm , SettingUpdateForm , ComplexListForm
import csv
from io import BytesIO
import xlsxwriter

one_yrs_ago = datetime.now() - relativedelta(years=1)
one_month_ago = datetime.now() - relativedelta(months=1)
sixty_days_ago = datetime.now() - relativedelta(days=60)
ninety_days_ago = datetime.now() - relativedelta(days=90)
onehundredtwenty_days_ago = datetime.now() - relativedelta(days=120)
onehundredeighty_days_ago = datetime.now() - relativedelta(days=180)

complex_list = [
                ('Kyle','Kyle'),
                ('5th Brooklyn BC','5th Brooklyn BC'),
                ('Ashkelon BC','Ashkelon BC'),
                ('Avonlea BC','Avonlea BC' ),
                ('Birchleigh View BC','Birchleigh View BC'),
                ('Birchpark BC','Birchpark BC'),
                ('Birdsview HOA','Birdsview HOA'),
                ('Blueberry Lane BC','Blueberry Lane BC'),
                ('BMT Community','BMT Community'),
                ('Bolderview BC','Bolderview BC'),
                ('Boschendal Manor BC','Boschendal Manor BC'),
                ('Bridgetown BC','Bridgetown BC'),
                ('Camperdown BC','Camperdown BC'),
                ('Caro Brooke','Caro Brooke'),
                ('Columbus Gardens BC','Columbus Gardens BC'),
                ('Constantia Park','Constantia Park'),
                ('Constantia Place BC','Constantia Place BC'),
                ('CPH Court BC','CPH Court BC'),
                ('Daphne Heights BC','Daphne Heights BC'),
                ('Dennehof ','Dennehof'),
                ('De Shepen HOA','De Shepen HOA'),
                ('Drommedaris BC','Drommedaris BC'),
                ('Eden Gardens BC','Eden Gardens BC'),
                ('Falcon Haven BC','Falcon Haven BC'),
                ('Fielding Place BC','Fielding Place BC'),
                ('Founders View HOA','Founders View HOA'),
                ('Glen Eden Villas BC','Glen Eden Villas BC'),
                ('Graceland Estates BC','Graceland Estates BC'),
                ('Grantwood Close BC', 'Grantwood Close BC'),
                ('Hadedahs HOA','Hadedahs HOA'),
                ('Hillside Estate HOA','Hillside Estate HOA'),
                ('Ingwe BC','Ingwe BC'),
                ('Kleyngeluk BC','Kleyngeluk BC'),
                ('Kwikstertjie BC','Kwikstertjie BC'),
                ('Larenzo Hof BC','Larenzo Hof BC'),
                ('Loftus View BC','Loftus View BC'),
                ('Manhattan BC','Manhattan BC'),
                ('Montelimar BC','Montelimar BC'),
                ('Netosha Place BC','Netosha Place BC'),
                (' Nettleton Close BC',' Nettleton Close BC'),
                ('Oaktree Village BC','Oaktree Village BC'),
                ('Poltin Court BC','Poltin Court BC'),
                ('Rapallo','Rapallo'),
                ('Rhino Industrial Park BC','Rhino Industrial Park BC'),
                ('River Close BC','River Close BC'),
                ('Robin Place BC','Robin Place BC'),
                ('Round About BC','Round About BC'),
                ('Ruddel Garden BC','Ruddel Garden BC'),
                ('Saligna Mews BC','Saligna Mews BC'),
                ('Sandpipers Nest BC','Sandpipers Nest BC'),
                ('San Lameer','San Lameer'),
                ('Stone Arch Village BC','Stone Arch Village BC'),
                ('Sunnyside Terrace BC','Sunnyside Terrace BC'),
                ('Sunridge BC','Sunridge BC'),
                ('Swallows Nest BC','Swallows Nest BC'),
                ('The Dromedaris BC','The Dromedaris BC'),
                ('The Pearls of Fourways','The Pearls of Fourways'),
                ('Tulbagh Gardens','Tulbagh Gardens'),
                ('Victoria BC','Victoria BC'),
                ('Villa Di Monte Negro BC','Villa Di Monte Negro BC'),
                ('Villa Grove','Villa Grove'),
                ('Villa Izanie BC','Villa Izanie BC'),
                ('Villa Marina BC','Villa Marina BC'),
                ('Walthof BC','Walthof BC'),
                ('Windmills BC','Windmills BC'),
                ('Zeldre Place HOA','Zeldre Place HOA'),
                ]

driver= '{SQL Server Native Client 11.0}'

def home(request):
    model = SettingsClass.objects.all().order_by('Complex')

    content ={'model':model }
    return render(request, 'main/reportsHome.html' , content)

def Kyletrb(request):
    cnxn = pyodbc.connect('DRIVER={SQL Server};'
                        'SERVER=192.168.1.1;'
                        'PORT=1433;'
                        'DATABASE=Kyle;'
                        'UID=kyle_dev_ro;'
                        'PWD=fh$sa#8d#7F8Y3;')

    #Trade Recievables
    tradeRecievables ="SELECT Master_Sub_Account , Accounts.Description , Debit , Credit FROM [dbo].[PostGL] as gl "\
         "Inner JOIN Accounts  "\
         "on Accounts.AccountLink = gl.AccountLink "\
         "Inner JOIN _etblGLAccountTypes as AccountTypes "\
         "on Accounts.iAccountType = AccountTypes.idGLAccountType "\
         "WHERE AccountTypes.idGLAccountType = '25' "

    cursor = cnxn.cursor();
    cursor.execute(tradeRecievables);
    xAllTR = cursor.fetchall()
    cursor.close()
    tradeRecievablesX = []
    for row in xAllTR:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Description"] = row[1]
        rdict["Debit"] = row[2]
        rdict["Credit"] = row[3]
        tradeRecievablesX.append(rdict)

    tradeRecievablesTotal = "SELECT ROUND(SUM(Credit) , 2) FROM PostGL AS gl "\
         "Inner JOIN Accounts  "\
         "on Accounts.AccountLink = gl.AccountLink "\
         "Inner JOIN _etblGLAccountTypes as AccountTypes "\
         "on Accounts.iAccountType = AccountTypes.idGLAccountType "\
         "WHERE AccountTypes.idGLAccountType = '25' "

    cursor = cnxn.cursor();
    cursor.execute(tradeRecievablesTotal);
    XtradeRecievablesTotal = cursor.fetchone()

    #Other Current Assets
    otherCurrentAssets ="SELECT Master_Sub_Account , Accounts.Description , Debit , Credit FROM [dbo].[PostGL] as gl "\
         "Inner JOIN Accounts  "\
         "on Accounts.AccountLink = gl.AccountLink "\
         "Inner JOIN _etblGLAccountTypes as AccountTypes "\
         "on Accounts.iAccountType = AccountTypes.idGLAccountType "\
         "WHERE AccountTypes.idGLAccountType = '3' "

    cursor = cnxn.cursor();
    cursor.execute(otherCurrentAssets);
    xAllOCR = cursor.fetchall()
    cursor.close()
    otherCurrentAssetsX = []
    for row in xAllOCR:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Description"] = row[1]
        rdict["Debit"] = row[2]
        rdict["Credit"] = row[3]
        otherCurrentAssetsX.append(rdict)

    otherCurrentAssetsTotal = "SELECT ROUND(SUM(Credit) , 2) FROM PostGL AS gl "\
         "Inner JOIN Accounts  "\
         "on Accounts.AccountLink = gl.AccountLink "\
         "Inner JOIN _etblGLAccountTypes as AccountTypes "\
         "on Accounts.iAccountType = AccountTypes.idGLAccountType "\
         "WHERE AccountTypes.idGLAccountType = '3' "

    cursor = cnxn.cursor();
    cursor.execute(otherCurrentAssetsTotal);
    XotherCurrentAssetsTotal = cursor.fetchone()

    #Cash and Cash Equivalents
    cashEquivalents ="SELECT Master_Sub_Account , Accounts.Description , Debit , Credit FROM [dbo].[PostGL] as gl "\
         "Inner JOIN Accounts  "\
         "on Accounts.AccountLink = gl.AccountLink "\
         "Inner JOIN _etblGLAccountTypes as AccountTypes "\
         "on Accounts.iAccountType = AccountTypes.idGLAccountType "\
         "WHERE AccountTypes.idGLAccountType = '1' "

    cursor = cnxn.cursor();
    cursor.execute(cashEquivalents);
    xAllCCE = cursor.fetchall()
    cursor.close()
    cashEquivalentsX = []
    for row in xAllCCE:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Description"] = row[1]
        rdict["Debit"] = row[2]
        rdict["Credit"] = row[3]
        cashEquivalentsX.append(rdict)

    cashEquivalentsTotal = "SELECT ROUND(SUM(Credit) , 2) FROM PostGL AS gl "\
         "Inner JOIN Accounts  "\
         "on Accounts.AccountLink = gl.AccountLink "\
         "Inner JOIN _etblGLAccountTypes as AccountTypes "\
         "on Accounts.iAccountType = AccountTypes.idGLAccountType "\
         "WHERE AccountTypes.idGLAccountType = '1' "

    cursor = cnxn.cursor();
    cursor.execute(cashEquivalentsTotal);
    XcashEquivalentsTotal = cursor.fetchone()

    #Total Current Asset + Asset
    #totalCurrentAsset = (XcashEquivalentsTotal + XotherCurrentAssetsTotal) - XtradeRecievablesTotal

    #totalAsset = totalCurrentAsset

    # Equity and Liabilities
    #
    #

    # Equity
    equity = "SELECT Master_Sub_Account , Accounts.Description , Debit , Credit FROM [dbo].[PostGL] as gl " \
                      "Inner JOIN Accounts  " \
                      "on Accounts.AccountLink = gl.AccountLink " \
                      "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                      "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                      "WHERE AccountTypes.idGLAccountType = '11' "

    cursor = cnxn.cursor();
    cursor.execute(equity);
    xAllE = cursor.fetchall()
    cursor.close()
    equityX = []
    for row in xAllE:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Description"] = row[1]
        rdict["Debit"] = row[2]
        rdict["Credit"] = row[3]
        equityX.append(rdict)

    equityTotal = "SELECT ROUND(SUM(Credit) , 2) FROM PostGL AS gl " \
                           "Inner JOIN Accounts  " \
                           "on Accounts.AccountLink = gl.AccountLink " \
                           "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                           "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                           "WHERE AccountTypes.idGLAccountType = '11' "

    cursor = cnxn.cursor();
    cursor.execute(equityTotal);
    XequityTotal = cursor.fetchone()

    # Current Liabilities
    otherCurrentLiabilities = "SELECT Master_Sub_Account , Accounts.Description , Debit , Credit FROM [dbo].[PostGL] as gl " \
             "Inner JOIN Accounts  " \
             "on Accounts.AccountLink = gl.AccountLink " \
             "Inner JOIN _etblGLAccountTypes as AccountTypes " \
             "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
             "WHERE AccountTypes.idGLAccountType = '5' "

    cursor = cnxn.cursor();
    cursor.execute(otherCurrentLiabilities);
    xAllOCL = cursor.fetchall()
    cursor.close()
    otherCurrentLiabilitiesX = []
    for row in xAllOCL:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Description"] = row[1]
        rdict["Debit"] = row[2]
        rdict["Credit"] = row[3]
        otherCurrentLiabilitiesX.append(rdict)

    otherCurrentLiabilitiesTotal = "SELECT ROUND(SUM(Credit) , 2) FROM PostGL AS gl " \
                  "Inner JOIN Accounts  " \
                  "on Accounts.AccountLink = gl.AccountLink " \
                  "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                  "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                  "WHERE AccountTypes.idGLAccountType = '5' "

    cursor = cnxn.cursor();
    cursor.execute(otherCurrentLiabilitiesTotal);
    XotherCurrentLiabilitiesTotal = cursor.fetchone()

    #Total Equity and Liabilities

    XequityAndLiabilitiesTotal = "SELECT ROUND(SUM(Credit) , 2) FROM PostGL AS gl " \
                  "Inner JOIN Accounts  " \
                  "on Accounts.AccountLink = gl.AccountLink " \
                  "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                  "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                  "WHERE AccountTypes.idGLAccountType = '5' AND AccountTypes.idGLAccountType = '11'"
    cursor = cnxn.cursor();
    cursor.execute(XequityAndLiabilitiesTotal);
    equityAndLiabilitiesTotal = cursor.fetchone()

    content = {'equityAndLiabilitiesTotal':equityAndLiabilitiesTotal,'XotherCurrentLiabilitiesTotal':XotherCurrentLiabilitiesTotal,'otherCurrentLiabilitiesX':otherCurrentLiabilitiesX,'XequityTotal':XequityTotal,'equityX':equityX,'cashEquivalentsX':cashEquivalentsX,'XcashEquivalentsTotal':XcashEquivalentsTotal,'tradeRecievablesX':tradeRecievablesX , 'XtradeRecievablesTotal':XtradeRecievablesTotal,'otherCurrentAssetsX':otherCurrentAssetsX,'XotherCurrentAssetsTotal':XotherCurrentAssetsTotal}
    return render(request , 'main/Kyletrb.html' , content)

def printToPdf(request):

    response = HttpResponse(content_type= 'application/pdf')
    response['Content-Disposition']= 'attachment; filename=TrialBalance' + \
        str(datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'


    all =  'SELECT Master_Sub_Account , cAccountTypeDescription , Debit , Credit FROM [Kyle].[dbo].[PostGL] AS genLedger'\
                    ' Inner JOIN [Kyle].[dbo].[Accounts] '\
                    'on Accounts.AccountLink = genLedger.AccountLink '\
                    'Inner JOIN [Kyle].[dbo].[_etblGLAccountTypes] as AccountTypes '\
                    'on Accounts.iAccountType = AccountTypes.idGLAccountType'\
                    ' WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122)'\
                    ' AND genLedger.TxDate >  ? '\
                    ' ORDER BY iAccountType'

    cnxn = pyodbc.connect('DRIVER={SQL Server};'
                        'SERVER=192.168.1.1;'
                        'PORT=1433;'
                        'DATABASE=Kyle;'
                        'UID=kyle_dev_ro;'
                        'PWD=fh$sa#8d#7F8Y3;')

    cursor = cnxn.cursor();
    cursor.execute(all);
    xAll = cursor.fetchall()
    cursor.close()
    xAll_l = []
    for row in xAll:
        rdict = {}
        rdict["Description"] = row[0]
        rdict["Account"] = row[1]
        rdict["Credit"] = row[2]
        rdict["Debit"] = row[3]
        xAll_l.append(rdict)

    creditTotal = ' Select ROUND(SUM(Credit) , 2) FROM [Kyle].[dbo].[PostGL] '
    cursor = cnxn.cursor();
    cursor.execute(creditTotal);
    xCreditTotal = cursor.fetchone()

    debitTotal = ' Select ROUND(SUM(Debit) , 2) FROM [Kyle].[dbo].[PostGL] '
    cursor = cnxn.cursor();
    cursor.execute(debitTotal);
    xDebitTotal = cursor.fetchone()

    html_string=render_to_string('main/pdf-trialbalance.html' ,  {"xAlls":xAll_l , 'xCreditTotal':xCreditTotal , 'xDebitTotal':xDebitTotal})
    html=HTML(string=html_string)

    result=html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output.seek(0)
        response.write(output.read())

    return response

def settingsHome(request ):


    allClass = SettingsClass.objects.all().order_by('Complex')
    return render(request, 'main/settingsHome.html' , {'allClass' : allClass })

def viewSettings(request,  setting_pk):
    setting = get_object_or_404(SettingsClass, pk=setting_pk)
    if request.method == 'GET':
        form = SettingUpdateForm(instance=setting)
        return render(request, 'main/viewSettings.html', {'setting': setting, 'form':form})
    else:
        form =  SettingUpdateForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('settingsHome')
        else:
            print(form.errors)

    return render(request, 'main/viewSettings.html', {'setting': setting, 'form':form})

def newSetting(request):
    form = SettingsForm()

    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settingsHome')

    return render(request , 'main/newSetting.html' , {'form':form})

def reportsHome(request):
    model = SettingsClass.objects.all().order_by('Complex')



    content ={'model':model }
    return render(request, 'main/reportsHome.html' , content)

def creditControlHome(request):

    return render(request , 'main/creditControlHome.html')

def creditControl(request):
    model = SettingsClass.objects.all().order_by('Complex')

    content ={'model':model }
    return render(request, 'main/creditControl.html' , content)

def interestBatches(request):
    model = SettingsClass.objects.all().order_by('Complex')

    content ={'model':model }
    return render(request, 'main/interestBatches.html' , content)

def printReports(request , reports_pk):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                                                         'UID=kyle_dev_ro;'
                                                         'PWD=fh$sa#8d#7F8Y3;'
                             )



    #CHECKING AGE ANALYSIS SETTINGS
    if pkForm.Age_Analysis == True :
        printAge = True

        if pkForm.aa_Include_all_customers == True:
            includeAllCustomers= True
        else:
            includeAllCustomers = False

        if pkForm.aa_Include_cash_customers == True:
            IncludeCashCustomers = True
        else:
            IncludeCashCustomers = False

        if pkForm.aa_include_on_hold_customers == True:
            printOnHoldCustomers =True
        else:
            printOnHoldCustomers =False

        if pkForm.aa_include_null_values == True:
            IncludeNullValues = True
        else:
            IncludeNullValues = False

        if pkForm.aa_allocate_unalocated_credits_to_oldest == True:
            creditsToOldest = True
        else:
            creditsToOldest = False

        #SQL Statement
        all =  'SELECT Account , Name , DCBalance FROM [dbo].[Client] WHERE DCBalance IS NOT NULL '

        cursor = connect.cursor();
        cursor.execute(all );
        xAll = cursor.fetchall()
        cursor.close()
        xAll_l = []
        for row in xAll:
            rdict = {}
            rdict["Account"] = row[0]
            rdict["Name"] = row[1]
            rdict["Balance"] = row[2]
            xAll_l.append(rdict)

        ### Printing Trial Balance PDF
        response = HttpResponse(content_type= 'application/pdf')
        response['Content-Disposition']= 'attachment; filename=CustomerAgeAnalysis' + \
            str(datetime.now()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        content =  {'xAll_l':xAll_l}
        html_string=render_to_string('main/reports/CustomerAgeAnalysis.html' , content)
        html=HTML(string=html_string)

        result=html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()

            output.seek(0)
            response.write(output.read())
    else:
        printAge = False



    #CHECKING BALANCE SHEET SETTINGS
    if pkForm.Balance_Sheet == True :
        printBS = True

        if pkForm.ism_Only_use_main_accounts == True:
            useMainAccountsISMON= True
        else:
            useMainAccountsISMON = False

        if pkForm.ism_Sort_by_account_name == True:
            sortByAccountNameISMON = True
        else:
            sortByAccountNameISMON = False

        if pkForm.ism_Print_null_values == True:
            printNullISYTD  =True
        else:
            printNullISYTD =False

        if pkForm.ism_Print_description == True:
            printDescISMON = True
        else:
            printDescISMON = False

        if pkForm.ism_Print_account == True:
            printAccISMON = True
        else:
            printAccISMON = False

        #SQL Statement
        all =  'SELECT Account , Name , DCBalance FROM [dbo].[Client] WHERE DCBalance IS NOT NULL '

        cursor = connect.cursor();
        cursor.execute(all );
        xAll = cursor.fetchall()
        cursor.close()
        xAll_l = []
        for row in xAll:
            rdict = {}
            rdict["Account"] = row[0]
            rdict["Name"] = row[1]
            rdict["Balance"] = row[2]
            xAll_l.append(rdict)

        ### Printing Trial Balance PDF
        response = HttpResponse(content_type= 'application/pdf')
        response['Content-Disposition']= 'attachment; filename=IncomeStatementMON' + \
            str(datetime.now()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        content =  {'xAll_l':xAll_l}
        html_string=render_to_string('main/reports/IncomeStatementMON.html' , content)
        html=HTML(string=html_string)

        result=html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()

            output.seek(0)
            response.write(output.read())
    else:
        printBS = False

def trialBalanceYearly(self , reports_pk):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                             'UID=kyle_dev_ro;'
                             'PWD=fh$sa#8d#7F8Y3;'
                             )

    # CHECKING TRIAL BALANCE YTD SETTINGS
    if pkForm.Trial_balance_Year_to_date == True:  # Completed
        if pkForm.tbytd_Only_use_main_accounts == True:
            op2Y = 'AND  Len(Master_Sub_Account) < 4 '
        else:
            op2Y = ''

        if pkForm.tbytd_Print_null_values == True:
            printZeroY = True
        else:
            printZeroY = False

        if pkForm.tbytd_Print_description == True:
            printDescY = True
        else:
            printDescY = False

        if pkForm.tbytd_Print_account == True:
            printAccY = True
        else:
            printAccY = False

        if pkForm.tbytd_Sort_by_account_name == True:
            op6Y = ' '#ORDER BY Master_Sub_Account'
        else:
            op6Y = ''

        # SQL STATEMENT
        baseTRBYear = 'SELECT   Master_Sub_Account , cAccountTypeDescription ,Debit , Credit FROM PostGL AS genLedger ' \
                      'Inner JOIN Accounts ' \
                      'on Accounts.AccountLink = genLedger.AccountLink ' \
                      'Inner JOIN _etblGLAccountTypes as AccountTypes ' \
                      'on Accounts.iAccountType = AccountTypes.idGLAccountType ' \
                      'WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122) ' \
                      'AND genLedger.TxDate >  ? '
        xtrbY = baseTRBYear + op2Y + op6Y

        cursor = connect.cursor();
        cursor.execute(xtrbY, [one_yrs_ago]);
        xAllY = cursor.fetchall()
        cursor.close()
        xtrbYear = []
        for row in xAllY:
            rdict = {}
            rdict["Description"] = row[0]
            rdict["Account"] = row[1]
            rdict["Debit"] = row[2]
            rdict["Credit"] = row[3]
            xtrbYear.append(rdict)

        BaseCreditTotalY = 'Select ROUND(SUM(Credit) , 2) FROM PostGL AS genLedger ' \
                           'Inner JOIN Accounts ' \
                           'on Accounts.AccountLink = genLedger.AccountLink ' \
                           'Inner JOIN _etblGLAccountTypes as AccountTypes ' \
                           'on Accounts.iAccountType = AccountTypes.idGLAccountType ' \
                           'WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122) ' \
                           'AND genLedger.TxDate >  ? '

        creditTotalY = BaseCreditTotalY + op2Y + op6Y
        cursor = connect.cursor();
        cursor.execute(creditTotalY, [one_yrs_ago]);
        xCreditTotalY = cursor.fetchone()

        BaseDebitTotalY = 'Select ROUND(SUM(Debit) , 2) FROM PostGL AS genLedger ' \
                          'Inner JOIN Accounts ' \
                          'on Accounts.AccountLink = genLedger.AccountLink ' \
                          'Inner JOIN _etblGLAccountTypes as AccountTypes ' \
                          'on Accounts.iAccountType = AccountTypes.idGLAccountType ' \
                          'WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122) ' \
                          'AND genLedger.TxDate >  ? '

        debitTotalY = BaseDebitTotalY + op2Y + op6Y
        cursor = connect.cursor();
        cursor.execute(debitTotalY, [one_yrs_ago]);
        xDebitTotalY = cursor.fetchone()

        ### Printing Trial Balance PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=TrialBalanceYTD' + \
                                          str(datetime.now()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        content = {'printDescY': printDescY, 'printAccY': printAccY, "xtrbYear": xtrbYear,
                   'xCreditTotalY': xCreditTotalY, 'xDebitTotalY': xDebitTotalY, 'complexName': complexName,
                   'printZeroY': printZeroY}
        html_string = render_to_string('main/reports/trialBalanceYear.html', content)
        html = HTML(string=html_string)

        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()

            output.seek(0)
            response.write(output.read())
    else:
        response = redirect('reportsHome')

    return response

def trialBalanceMonthly(self ,  reports_pk):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                                                         'UID=kyle_dev_ro;'
                                                         'PWD=fh$sa#8d#7F8Y3;'
                             )

    # CHECKING TRIAL BALANCE MONTHLY SETTINGS
    if pkForm.Trial_balance_Monthly == True:  # Completed
        printTrialBalanceM = True
        if pkForm.tbm_Only_use_main_accounts == True:
            op2M = 'AND  Len(Master_Sub_Account) < 4 '
        else:
            op2M = ''

        if pkForm.tbm_Print_null_values == True:
            printZeroM = True
        else:
            printZeroM = False

        if pkForm.tbm_Print_description == True:
            printDescM = True
        else:
            printDescM = False

        if pkForm.tbm_Print_account == True:
            printAccM = True
        else:
            printAccM = False

        if pkForm.tbm_Sort_by_account_name == True:
            op6M = ' '#ORDER BY Master_Sub_Account ASC'
        else:
            op6M = ''

        # SQL STATEMENT
        baseTRBMonth = 'SELECT   Master_Sub_Account , cAccountTypeDescription ,Debit , Credit FROM PostGL AS genLedger ' \
                       'Inner JOIN Accounts ' \
                       'on Accounts.AccountLink = genLedger.AccountLink ' \
                       'Inner JOIN _etblGLAccountTypes as AccountTypes ' \
                       'on Accounts.iAccountType = AccountTypes.idGLAccountType ' \
                       'WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122) ' \
                       'AND genLedger.TxDate >  ? '
        xtrbMonth = baseTRBMonth + op2M + op6M

        cursor = connect.cursor();
        cursor.execute(xtrbMonth, [one_month_ago]);
        xAllM = cursor.fetchall()
        cursor.close()
        xtrbMonth = []
        for row in xAllM:
            rdict = {}
            rdict["Description"] = row[0]
            rdict["Account"] = row[1]
            rdict["Debit"] = row[2]
            rdict["Credit"] = row[3]
            xtrbMonth.append(rdict)

        BaseCreditTotalM = 'Select ROUND(SUM(Credit) , 2) FROM PostGL AS genLedger ' \
                           'Inner JOIN Accounts ' \
                           'on Accounts.AccountLink = genLedger.AccountLink ' \
                           'Inner JOIN _etblGLAccountTypes as AccountTypes ' \
                           'on Accounts.iAccountType = AccountTypes.idGLAccountType ' \
                           'WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122) ' \
                           'AND genLedger.TxDate >  ? '

        creditTotalM = BaseCreditTotalM + op2M + op6M
        cursor = connect.cursor();
        cursor.execute(creditTotalM, [one_month_ago]);
        xCreditTotalM = cursor.fetchone()

        BaseDebitTotalM = 'Select ROUND(SUM(Debit) , 2) FROM PostGL AS genLedger ' \
                          'Inner JOIN Accounts ' \
                          'on Accounts.AccountLink = genLedger.AccountLink ' \
                          'Inner JOIN _etblGLAccountTypes as AccountTypes ' \
                          'on Accounts.iAccountType = AccountTypes.idGLAccountType ' \
                          'WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122) ' \
                          'AND genLedger.TxDate >  ? '

        debitTotalM = BaseDebitTotalM + op2M + op6M
        cursor = connect.cursor();
        cursor.execute(debitTotalM, [one_month_ago]);
        xDebitTotalM = cursor.fetchone()

        ### Printing Trial Balance PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=TrialBalanceMonthly' + \
                                          str(datetime.now()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        content = {'printDescM': printDescM, 'printAccM': printAccM, "xtrbMonth": xtrbMonth,
                   'xCreditTotalM': xCreditTotalM, 'xDebitTotalM': xDebitTotalM, 'complexName': complexName,
                   'printZeroM': printZeroM}
        html_string = render_to_string('main/reports/trialBalanceMonthly.html', content)
        html = HTML(string=html_string)

        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()

            output.seek(0)
            response.write(output.read())
    else:
        response = redirect('reportsHome')

    return response

def incomeStatementMonthly(self , reports_pk):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                             'UID=kyle_dev_ro;'
                             'PWD=fh$sa#8d#7F8Y3;'
                             )

    # CHECKING INCOME STATEMENT MONTHLY SETTINGS
    if pkForm.Income_Statement_Monthly == True:
        printIncomeStatementMON = True

        if pkForm.ism_Only_use_main_accounts == True:
            useMainAccountsISMON = 'AND len(Master_Sub_Account) < 5'
        else:
            useMainAccountsISMON = ''

        if pkForm.ism_Sort_by_account_name == True:
            sortByAccountNameISMON = ''#ORDER BY Master_Sub_Account'
        else:
            sortByAccountNameISMON = ''

        if pkForm.ism_Print_null_values == True:
            printNullISMON = True
        else:
            printNullISMON = False

        if pkForm.ism_Print_description == True:
            printDescISMON = True
        else:
            printDescISMON = False

        if pkForm.ism_Print_account == True:
            printAccISMON = True
        else:
            printAccISMON = False

        # SQL Statement
        otherExpenseBaseM = "SELECT Master_Sub_Account, Debit , Credit FROM [dbo].[PostGL] as gl " \
                            "Inner JOIN Accounts  " \
                            "on Accounts.AccountLink = gl.AccountLink " \
                            "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                            "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                            "WHERE cAccountTypeDescription = 'Other Expense' " \
                            "AND gl.TxDate >  ? "

        otherExpenseM = otherExpenseBaseM + useMainAccountsISMON + sortByAccountNameISMON
        cursor = connect.cursor();
        cursor.execute(otherExpenseM, [one_month_ago]);
        xAllOtherExpenseM = cursor.fetchall()
        cursor.close()
        otherExpenseXM = []
        for row in xAllOtherExpenseM:
            rdict = {}
            rdict["Account"] = row[0]
            rdict["Debit"] = row[1]
            rdict["Credit"] = row[2]
            otherExpenseXM.append(rdict)

        otherIncomeBaseM = "SELECT Master_Sub_Account, Debit , Credit FROM [dbo].[PostGL] as gl " \
                           "Inner JOIN Accounts  " \
                           "on Accounts.AccountLink = gl.AccountLink " \
                           "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                           "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                           "WHERE cAccountTypeDescription = 'Other Income' " \
                           "AND gl.TxDate >  ? "

        otherIncomeM = otherIncomeBaseM + useMainAccountsISMON + sortByAccountNameISMON
        cursor = connect.cursor();
        cursor.execute(otherIncomeM, [one_month_ago]);
        xAllOtherIncomeM = cursor.fetchall()
        cursor.close()
        otherIncomeXM = []
        for row in xAllOtherIncomeM:
            rdict = {}
            rdict["Account"] = row[0]
            rdict["Debit"] = row[1]
            rdict["Credit"] = row[2]
            otherIncomeXM.append(rdict)

        otherExpenseTotalBaseM = "Select ROUND(SUM(Debit) , 2) FROM [dbo].[PostGL] AS gl " \
                                 "Inner JOIN Accounts  " \
                                 "on Accounts.AccountLink = gl.AccountLink " \
                                 "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                                 "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                                 "WHERE cAccountTypeDescription = 'Other Expense' " \
                                 "AND gl.TxDate >  ? "

        otherExpenseTotalM =  otherExpenseTotalBaseM + useMainAccountsISMON
        cursor = connect.cursor();
        cursor.execute(otherExpenseTotalM, [one_month_ago]);
        xotherExpenseTotalM = cursor.fetchone()

        otherIncomeTotalBaseM = "Select ROUND(SUM(Credit) , 2) FROM [dbo].[PostGL] AS gl " \
                                "Inner JOIN Accounts  " \
                                "on Accounts.AccountLink = gl.AccountLink " \
                                "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                                "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                                "WHERE cAccountTypeDescription = 'Other Income' " \
                                "AND gl.TxDate >  ? "

        otherIncomeTotalM = otherIncomeTotalBaseM + useMainAccountsISMON
        cursor = connect.cursor();
        cursor.execute(otherIncomeTotalM, [one_month_ago]);
        xotherIncomeTotalM = cursor.fetchone()

        content = {'complexName': complexName, 'printDescISMON': printDescISMON, 'printAccISMON': printAccISMON,
                   'otherIncomeXM': otherIncomeXM, 'otherExpenseXM': otherExpenseXM,
                   'xotherIncomeTotalM': xotherIncomeTotalM, 'xotherExpenseTotalM': xotherExpenseTotalM,
                   'printNullISMON': printNullISMON}

        ### Printing Trial Balance PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=IncomeStatementMonthly' + \
                                          str(datetime.now()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        html_string = render_to_string('main/reports/IncomeStatementMON.html', content)
        html = HTML(string=html_string)

        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()

            output.seek(0)
            response.write(output.read())
    else:
        response = redirect('reportsHome')

    return response

def incomeStatementYearly(self , reports_pk):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                                                         'UID=kyle_dev_ro;'
                                                         'PWD=fh$sa#8d#7F8Y3;'
                             )

    # CHECKING INCOME STATEMENT YTD SETTINGS
    if pkForm.Income_Statement_Year_to_date == True:  # Completed
        printIncomeStatementYTD = True

        if pkForm.isytd_Only_use_main_accounts == True:
            useMainAccountsISYTD = 'AND len(Master_Sub_Account) < 5'
        else:
            useMainAccountsISYTD = ''

        if pkForm.isytd_Sort_by_account_name == True:
            sortByAccountNameISYTD = ''#ORDER BY Master_Sub_Account'
        else:
            sortByAccountNameISYTD = ''

        if pkForm.isytd_Print_null_values == True:
            printNullISYTD = True
        else:
            printNullISYTD = False

        if pkForm.isytd_Print_description == True:
            printDescISYTD = True
        else:
            printDescISYTD = False

        if pkForm.isytd_Print_account == True:
            printAccISYTD = True
        else:
            printAccISYTD = False

        # SQL Statement
        otherExpenseBase = "SELECT Master_Sub_Account, Debit , Credit FROM [dbo].[PostGL] as gl " \
                           "Inner JOIN Accounts  " \
                           "on Accounts.AccountLink = gl.AccountLink " \
                           "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                           "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                           "WHERE cAccountTypeDescription = 'Other Expense' " \
                           "AND gl.TxDate >  ? "

        otherExpense = otherExpenseBase + useMainAccountsISYTD + sortByAccountNameISYTD
        cursor = connect.cursor();
        cursor.execute(otherExpense, [one_yrs_ago]);
        xAllOtherExpense = cursor.fetchall()
        cursor.close()
        otherExpenseX = []
        for row in xAllOtherExpense:
            rdict = {}
            rdict["Account"] = row[0]
            rdict["Debit"] = row[1]
            rdict["Credit"] = row[2]
            otherExpenseX.append(rdict)

        otherIncomeBase = "SELECT Master_Sub_Account, Debit , Credit FROM [dbo].[PostGL] as gl " \
                          "Inner JOIN Accounts  " \
                          "on Accounts.AccountLink = gl.AccountLink " \
                          "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                          "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                          "WHERE cAccountTypeDescription = 'Other Income' " \
                          "AND gl.TxDate >  ? "

        otherIncome = otherIncomeBase + useMainAccountsISYTD + sortByAccountNameISYTD
        cursor = connect.cursor();
        cursor.execute(otherIncome, [one_yrs_ago]);
        xAllOtherIncome = cursor.fetchall()
        cursor.close()
        otherIncomeX = []
        for row in xAllOtherIncome:
            rdict = {}
            rdict["Account"] = row[0]
            rdict["Debit"] = row[1]
            rdict["Credit"] = row[2]
            otherIncomeX.append(rdict)

        otherExpenseTotalBase = "Select ROUND(SUM(Debit) , 2) FROM [dbo].[PostGL] AS gl " \
                                "Inner JOIN Accounts  " \
                                "on Accounts.AccountLink = gl.AccountLink " \
                                "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                                "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                                "WHERE cAccountTypeDescription = 'Other Expense' " \
                                "AND gl.TxDate >  ? "

        otherExpenseTotal =  otherExpenseTotalBase + useMainAccountsISYTD
        cursor = connect.cursor();
        cursor.execute(otherExpenseTotal, [one_yrs_ago]);
        xotherExpenseTotal = cursor.fetchone()

        otherIncomeTotalBase = "Select ROUND(SUM(Credit) , 2) FROM [dbo].[PostGL] AS gl " \
                               "Inner JOIN Accounts  " \
                               "on Accounts.AccountLink = gl.AccountLink " \
                               "Inner JOIN _etblGLAccountTypes as AccountTypes " \
                               "on Accounts.iAccountType = AccountTypes.idGLAccountType " \
                               "WHERE cAccountTypeDescription = 'Other Income' " \
                               "AND gl.TxDate >  ? "

        otherIncomeTotal = otherIncomeTotalBase + useMainAccountsISYTD
        cursor = connect.cursor();
        cursor.execute(otherIncomeTotal, [one_yrs_ago]);
        xotherIncomeTotal = cursor.fetchone()

        content = {'complexName': complexName, 'printDescISYTD': printDescISYTD, 'printAccISYTD': printAccISYTD,
                   'otherIncomeX': otherIncomeX, 'otherExpenseX': otherExpenseX, 'xotherIncomeTotal': xotherIncomeTotal,
                   'xotherExpenseTotal': xotherExpenseTotal, 'printNullISYTD': printNullISYTD}

        ### Printing Trial Balance PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=IncomeStatementYTD' + \
                                          str(datetime.now()) + '.pdf'
        response['Content-Transfer-Encoding'] = 'binary'

        html_string = render_to_string('main/reports/IncomeStatementYTD.html', content)
        html = HTML(string=html_string)

        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()

            output.seek(0)
            response.write(output.read())
    else:
        response = redirect('reportsHome')

    return response

def AgeAnalysisCSV(self , reports_pk):

    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                             'UID=sa;'
                             'PWD=Z1p73r;'
                             )

    ownersAccounts = "Select Count(*) from dbo.Client Where iClassID = '1'"
    cursor = connect.cursor();
    cursor.execute(ownersAccounts);
    xOwnersAccounts = cursor.fetchone()                                         #Gets the amount of Owners Units

    ageSelect = "Select EMail , [Name], DrCrAccount , Account "\
	",Round(Sum(Credit) - Sum(Debit),2) as Balance "\
    " FROM PostGL "\
    " Inner JOIN Client as Client on Client.DCLink = DrCrAccount "\
    " WHERE AccountLink <> '104' and TxDate < '2022/01/31' and id <> 'CB' "\
    " GROUP BY DrCrAccount, Account , EMail , [Name]"\
    " ORDER BY DrCrAccount "

    cursor = connect.cursor();
    cursor.execute(ageSelect);
    xAgeSelect = cursor.fetchall()
    cursor.close()
    ageSelect = []

    for row in xAgeSelect:
        rdict = {}
        rdict["E-mail"] = row[0]
        rdict["Name"] = row[1]
        rdict["DrCrAccount"] = row[2]
        rdict["Account"] = row[3]
        rdict["Balance"] = row[4]
        ageSelect.append(rdict)

    totalCurent = "Select  Round(Sum(DCBalance),2) From dbo.Client Where iClassID ='1' "
    cursor = connect.cursor();
    cursor.execute(totalCurent);
    XtotalCurent = cursor.fetchone()

    # Starting CSV
    #
    #
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    data1 = ('Prepared By : Atout(PTY) ltd', '')
    data2 = ('Customer Age Analysis for Monthly Customers as at 15/01/22', '')
    data3 = (
        'Account', ' ', ' ', '120+ Days', '90 Days', '60 Days', '30 days', 'Current', 'Total', '', 'Name', 'E-mail')

    worksheet.write_row('A1', data1)
    worksheet.write_row('A2', data2)
    worksheet.write_row('A3', data3)

    count = 4
    for x  in ageSelect:
        if x["Balance"] > 0:
            data4 = (
                x["Account"], '*', ' ','','','','','',x["Balance"],'',x["Name"],x["E-mail"]
            )

            worksheet.write_row('A'+str(count) , data4 )
            count= count +1

    for x in XtotalCurent:
        counter = count
        data5 =('Totals :', ' ', ' ', '0', '0', '0', '0', x, x)
        data6 =('PERCENTAGE :', ' ', ' ', '0%', '0%', '0%', '0%', '100%', '100%')
        data7 =('GRAND TOTAL :', ' ', ' ', '', '', '', '', '', x)

        worksheet.write_row('A'+str(counter), data5)
        counter = counter +1
        worksheet.write_row('A'+str(counter), data6)
        counter = counter +1
        worksheet.write_row('A'+str(counter), data7)

    workbook.close()

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="' + complexName + '"Age Analysis.xlsx"'
    response.write(output.getvalue())

    return response

def customerDetails(request):
    model = SettingsClass.objects.all().order_by('Complex')
    form = ComplexListForm
    message = ''
    if request.method=="POST":
        complex = request.POST.get("Complex")
        unitNo =  request.POST.get("Unit")
        phoneNo = request.POST.get("PhoneNumber")
        email = request.POST.get("E-mailAddress")

        unitNumber = int(unitNo) + 1

        customerCXNX = pyodbc.connect('DRIVER={SQL Server};'
                                           'SERVER=192.168.1.1;'
                                            'PORT=1433;'
                                            'DATABASE=' + complex + ';'
                                            'UID=sa;'
                                            'PWD=Z1p73r;'
                                            )

        print('The following changes have been successfully made ' + complex + ' - Unit ' + unitNo + '    Phone Number :' + phoneNo + ' E-mail :' + email)
        updateCustomer = "Update dbo.Client Set Telephone = ? , EMail = ? where DCLink = ?"
        cursor = customerCXNX.cursor();
        cursor.execute(updateCustomer , phoneNo , email , unitNumber);
        customerCXNX.commit()

        message = 'The following changes have been successfully made to ' + complex + ' - Unit ' + unitNo + '    Phone Number :' + phoneNo + ' E-mail :' + email


    content = {'model': model , 'form':form , 'message':message}
    return render(request, 'main/customerDetails.html', content)

def viewSingleCustomer(request):
    model = SettingsClass.objects.all().order_by('Complex')
    form = ComplexListForm
    messageUnit = ''
    messageName = ''
    messageContactPerson = ''
    messageTelNumbers = ''
    messageEmail = ''

    if request.method=="POST":
        complex = request.POST.get("Complex")
        unitNo =  request.POST.get("Unit")

        unitNumber = int(unitNo) + 1

        customerCXNX = pyodbc.connect('DRIVER={SQL Server};'
                                           'SERVER=192.168.1.1;'
                                            'PORT=1433;'
                                            'DATABASE=' + complex + ';'
                                            'UID=sa;'
                                            'PWD=Z1p73r;'
                                            )

        selectCustomer = "Select Account , Name ,Telephone, Telephone2 , EMail , Contact_Person from dbo.Client where DCLink = ?"
        cursor = customerCXNX.cursor();
        cursor.execute(selectCustomer , unitNumber);
        detailsSelect = cursor.fetchall()
        detailsSelected = []

        for row in detailsSelect:
            rdict = {}
            rdict["Account"] = row[0]
            rdict["Name"] = row[1]
            rdict["Telephone"] = row[2]
            rdict["Telephone2"] = row[3]
            rdict["Email"] = row[4]
            rdict["Contact_Person"] = row[5]
            detailsSelected.append(rdict)

        messageUnit = 'Unit: ' + detailsSelected["Account"]
        messageName = 'Name: ' +detailsSelect["Name"]
        messageContactPerson = 'Contact Person: ' + detailsSelect["Contact_Person"]
        messageTelNumbers =  'Telephone Numbers: ' + detailsSelect["Telephone"] +'/'+  detailsSelect["Telephone2"]
        messageEmail = 'E-mail: ' + detailsSelect["Email"]

    content = {'model': model , 'form':form , 'messageUnit':messageUnit ,'messageName':messageName ,'messageContactPerson':messageContactPerson ,'messageTelNumbers':messageTelNumbers,'messageEmail':messageEmail}
    return render(request, 'main/viewSingleCustomer.html', content)

def journalEntry(request):
    cnxn = pyodbc.connect('DRIVER={SQL Server};'
                        'SERVER=192.168.1.1;'
                        'PORT=1433;'
                        'DATABASE=Kyle;'
                        'UID=kyle_dev_ro;'
                        'PWD=fh$sa#8d#7F8Y3;')

    accounts = ' Select Master_Sub_Account , Description , cAccountTypeDescription from [Kyle].[dbo].[Accounts] as Accounts Inner Join [Kyle].[dbo].[_etblGLAccountTypes] as AccountTypes ' \
               'on Accounts.iAccountType = AccountTypes.idGLAccountType '
    cursor = cnxn.cursor();
    cursor.execute(accounts);
    Xaccounts = cursor.fetchall()
    cursor.close()
    accountsAll = []
    for row in Xaccounts:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Description"] = row[1]
        rdict["AccountType"] = row[2]
        accountsAll.append(rdict)

    tax = ' Select Code , Description , TaxRate from [Kyle].[dbo].[TaxRate] '
    cursor = cnxn.cursor();
    cursor.execute(tax);
    Xtax = cursor.fetchall()
    cursor.close()
    taxAll = []
    for row in Xtax:
        rdict = {}
        rdict["Code"] = row[0]
        rdict["Description"] = row[1]
        rdict["TaxRate"] = row[2]
        taxAll.append(rdict)

    content = {'accountsAll':accountsAll , 'taxAll':taxAll}
    return render(request, 'main/journalEntry.html', content)

def InterestChargeCSV(request, reports_pk):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex


    # Getting list of DB Names
    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                             'UID=kyle_dev_ro;'
                             'PWD=fh$sa#8d#7F8Y3;'
                             )


    # Starting CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=" ' + complexName + ' Interest Batch.csv"'
    writer = csv.writer(response)

    selectBalances =    " SELECT   DrCrAccount , Account, Round(Sum(Credit) - Sum(Debit),2) as Balance, Round(Round(Sum(Credit) - Sum(Debit),2)*0.02,2) as Interest FROM [dbo].[PostGL] as PostGl" \
                        " Inner JOIN [dbo].[Client] as Client on Client.DCLink = DrCrAccount " \
                        " Where AccountLink <> '104' and TxDate < '2022/01/16' and id <> 'CB' Group By Account , DrCrAccount Order By DrCrAccount "
    cursor = connect.cursor();
    cursor.execute(selectBalances);
    XselectBalances = cursor.fetchall()
    cursor.close()
    Balances = []
    for row in XselectBalances:
        rdict = {}
        rdict["DrCrAccount"] = row[0]
        rdict["Account"] = row[1]
        rdict["Balance"] = row[2]
        rdict["2% Interest"] = row[3]
        Balances.append(rdict)

    for x in Balances:
        if x["Balance"] > 200:
            writer.writerow([
                    '2022/02/15',
                    x["Account"],
                    'AR',
                    'Interest',
                    '0',
                    '10-Jan',
                    'Interest',
                    ' ',
                    x["2% Interest"],
                    ' ',
                    ' ',
                    '0',
                    x["2% Interest"],
                    '1',
                    x["2% Interest"],
                    x["2% Interest"],
                    '0',
                    '0',
                    ' ',
                    '0',
                    '0',
                    '0',
                    ' ',
                    ' ',
                    '0',
                    '0',
                    ' ',
                    '0',
                    '0',
                    '0',
                    '2750>050',
                    '0',
                    '0'
                ])


    return response

def complexCustomerList(request):
    model = SettingsClass.objects.all().order_by('Complex')

    content ={'model':model }
    return render(request, 'main/complexCustomerList.html' , content)

def DisplayCustomers(request, reports_pk ):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                             'UID=kyle_dev_ro;'
                             'PWD=fh$sa#8d#7F8Y3;'
                             )

    viewCustomersSQL = ' Select Account , Name , Contact_Person , Telephone , Telephone2 , Fax1 , Fax2, EMail from dbo.Client Where DCLink <> 1 '

    cursor = connect.cursor();
    cursor.execute(viewCustomersSQL);
    viewCustomersData = cursor.fetchall()
    cursor.close()
    viewCustomers = []
    for row in viewCustomersData:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Name"] = row[1]
        rdict["Contact_Person"] = row[2]
        rdict["Telephone"] = row[3]
        rdict["Telephone2"] = row[4]
        rdict["Fax1"] = row[5]
        rdict["Fax2"] = row[6]
        rdict["Email"] = row[7]
        viewCustomers.append(rdict)

    content ={'viewCustomers':viewCustomers }
    return render(request, 'main/viewCustomers.html' , content)

def printViewCustomers(request , reports_pk):
    pkForm = get_object_or_404(SettingsClass, pk=reports_pk)

    complexName = pkForm.Complex

    connect = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=192.168.1.1;'
                             'PORT=1433;'
                             'DATABASE=' + complexName + ';'
                             'UID=kyle_dev_ro;'
                              'PWD=fh$sa#8d#7F8Y3;'
                             )

    viewCustomersSQL = ' Select Account , Name , Contact_Person , Telephone , Telephone2 , Fax1 , Fax2, EMail from dbo.Client Where DCLink <> 1 '

    cursor = connect.cursor();
    cursor.execute(viewCustomersSQL);
    viewCustomersData = cursor.fetchall()
    cursor.close()
    viewCustomers = []
    for row in viewCustomersData:
        rdict = {}
        rdict["Account"] = row[0]
        rdict["Name"] = row[1]
        rdict["Contact_Person"] = row[2]
        rdict["Telephone"] = row[3]
        rdict["Telephone2"] = row[4]
        rdict["Fax1"] = row[5]
        rdict["Fax2"] = row[6]
        rdict["Email"] = row[7]
        viewCustomers.append(rdict)

    # Starting CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=" ' + complexName + ' Customer Details.csv"'
    writer = csv.writer(response)

    writer.writerow([
        'Unit',
        'Name',
        'Contact Person',
        'Telephone 1',
        'Telephone 2',
        'E-mail'
    ])

    for x in viewCustomers:
        writer.writerow([
            x["Account"],
            x["Name"],
            x["Contact_Person"],
            x["Telephone"],
            x["Telephone2"],
            x["Email"]
        ])

    return response

def customerDetailsHome(request):

    return render(request, 'main/customerDetailsHome.html')

def viewDetailsHome(request):

    return render(request , 'main/viewDetailsHome.html')

def yourmom(request):
    return redirect('https://www.youtube.com/watch?v=HIcSWuKMwOw')
