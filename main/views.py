from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import pyodbc
from django.http import FileResponse
from django.contrib import messages
from django.views import View
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
import xlwt
from .models import SettingsClass
from .forms import SettingsForm , SettingUpdateForm

one_yrs_ago = datetime.now() - relativedelta(years=1)
one_month_ago = datetime.now() - relativedelta(months=1)


complex_list = [
                ('5th On Brooklyn','5th On Brooklyn'),
                ('Ashkelon','Ashkelon'),
                ('Avonlea','Avonlea' ),
                ('Birchleigh View','Birchleigh View'),
                ('Birchpark','Birchpark'),
                ('Birds View','Birds View'),
                ('Blueberry Lane','Blueberry Lane'),
                ('BMT Community','BMT Community'),
                ('Bolder View','Bolder View'),
                ('Boschendal Manor','Boschendal Manor'),
                ('Bridgetown','Bridgetown'),
                ('Camperdown','Camperdown'),
                ('Caro Brooke','Caro Brooke'),
                ('Columbus Gardens','Columbus Gardens'),
                ('Constantia Place','Constantia Place'),
                ('CPH Court','CPH Court'),
                ('Daphne Heights','Daphne Heights'),
                ('Dennehof','Dennehof'),
                ('De Scheepen','De Scheepen'),
                ('Die Binnehuis','Die Binnehuis'),
                ('Drommedaris','Drommedaris'),
                ('Eden Gardens','Eden Gardens'),
                ('Falcon Haven','Falcon Haven'),
                ('Fielding Place','Fielding Place'),
                ('Founders View','Founders View'),
                ('Glen Eden Villas','Glen Eden Villas'),
                ('Graceland Estates','Graceland Estates'),
                ('Hadedahs','Hadedahs'),
                ('Hillside Estate','Hillside Estate'),
                ('Ingwe','Ingwe'),
                ('Kiaat','Kiaat'),
                ('Kleyngeluk','Kleyngeluk'),
                ('Kwikstertjie','Kwikstertjie'),
                ('Larenso Hof','Larenso Hof'),
                ('Loftus View','Loftus View'),
                ('Manhatten Heights','Manhatten Heights'),
                ('Monte Limar','Monte Limar'),
                ('Netosha Place','Netosha Place'),
                ('Nettleton Close','Nettleton Close'),
                ('Oak Tree Village','Oak Tree Village'),
                ('Poltin Court','Poltin Court'),
                ('Rapallo','Rapallo'),
                ('Rhino Industrial Park','Rhino Industrial Park'),
                ('River Close','River Close'),
                ('Robins Place','Robins Place'),
                ('Round About','Round About'),
                ('Ruddell Gardens','Ruddell Gardens'),
                ('Saligna','Saligna'),
                ('Sandpipers Nest','Sandpipers Nest'),
                ('San La Meer','San La Meer'),
                ('Stone Arch - Village 5','Stone Arch - Village 5'),
                ('Sunnyside Terrace','Sunnyside Terrace'),
                ('Sunridge','Sunridge'),
                ('Swallows Nest','Swallows Nest'),
                ('The Drommedaris','The Drommedaris'),
                ('Tulbagh Gardens','Tulbagh Gardens'),
                ('Victoria Court','Victoria Court'),
                ('Villa De Monte Negro','Villa De Monte Negro'),
                ('Villa Grove','Villa Grove'),
                ('Villa Izanie','Villa Izanie'),
                ('Villa Marina','Villa Marina'),
                ('Walthof','Walthof'),
                ('Windmills','Windmills'),
                ('Zeldre Place','Zeldre Place'),
                ]


driver= '{SQL Server Native Client 11.0}'

cnxn = pyodbc.connect('DRIVER={SQL Server};'
                    'SERVER=192.168.1.1;'
                    'PORT=1433;'
                    'DATABASE=Kyle;'
                    'UID=kyle_dev_ro;'
                    'PWD=fh$sa#8d#7F8Y3;')

def home(request):

    return render(request , 'main/home.html')

def KyletrbSettings(request):
    return render(request , 'main/kyletrbsettings.html')

def KyletrbMonth(request):

        all =  'SELECT Master_Sub_Account , cAccountTypeDescription , Debit , Credit FROM [Kyle].[dbo].[PostGL] AS genLedger'\
                        ' Inner JOIN [Kyle].[dbo].[Accounts] '\
                        'on Accounts.AccountLink = genLedger.AccountLink '\
                        'Inner JOIN [Kyle].[dbo].[_etblGLAccountTypes] as AccountTypes '\
                        'on Accounts.iAccountType = AccountTypes.idGLAccountType'\
                        ' WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122)'\
                        ' AND genLedger.TxDate > ?'\
                        ' ORDER BY iAccountType'


        cursor = cnxn.cursor();
        cursor.execute(all, [one_month_ago]);
        xAll = cursor.fetchall()
        cursor.close()
        xAll_l = []
        for row in xAll:
            rdict = {}
            rdict["Description"] = row[0]
            rdict["Account"] = row[1]
            rdict["Debit"] = row[2]
            rdict["Credit"] = row[3]
            xAll_l.append(rdict)

        creditTotal = ' Select ROUND(SUM(Credit) , 2) FROM [Kyle].[dbo].[PostGL] '
        cursor = cnxn.cursor();
        cursor.execute(creditTotal);
        xCreditTotal = cursor.fetchone()

        debitTotal = ' Select ROUND(SUM(Debit) , 2) FROM [Kyle].[dbo].[PostGL] '
        cursor = cnxn.cursor();
        cursor.execute(debitTotal);
        xDebitTotal = cursor.fetchone()

        return render(request , 'main/KyletrbMonth.html' , {"xAlls":xAll_l , 'xCreditTotal':xCreditTotal , 'xDebitTotal':xDebitTotal})

def Kyletrb(request):
    all =  'SELECT Master_Sub_Account , cAccountTypeDescription , Debit , Credit FROM [Kyle].[dbo].[PostGL] AS genLedger'\
                    ' Inner JOIN [Kyle].[dbo].[Accounts] '\
                    'on Accounts.AccountLink = genLedger.AccountLink '\
                    'Inner JOIN [Kyle].[dbo].[_etblGLAccountTypes] as AccountTypes '\
                    'on Accounts.iAccountType = AccountTypes.idGLAccountType'\
                    ' WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122)'\
                    ' AND genLedger.TxDate > ?'\
                    ' ORDER BY iAccountType'


    cursor = cnxn.cursor();
    cursor.execute(all, [one_yrs_ago]);
    xAll = cursor.fetchall()
    cursor.close()
    xAll_l = []
    for row in xAll:
        rdict = {}
        rdict["Description"] = row[0]
        rdict["Account"] = row[1]
        rdict["Debit"] = row[2]
        rdict["Credit"] = row[3]
        xAll_l.append(rdict)

    creditTotal = ' Select ROUND(SUM(Credit) , 2) FROM [Kyle].[dbo].[PostGL] '
    cursor = cnxn.cursor();
    cursor.execute(creditTotal);
    xCreditTotal = cursor.fetchone()

    debitTotal = ' Select ROUND(SUM(Debit) , 2) FROM [Kyle].[dbo].[PostGL] '
    cursor = cnxn.cursor();
    cursor.execute(debitTotal);
    xDebitTotal = cursor.fetchone()

    return render(request , 'main/Kyletrb.html' , {"xAlls":xAll_l , 'xCreditTotal':xCreditTotal , 'xDebitTotal':xDebitTotal})

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
                    ' AND genLedger.TxDate > ?'\
                    ' ORDER BY iAccountType'

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

def printToXLS(request):
    response = HttpResponse(content_type= 'application/ms-excel')
    response['Content-Disposition']= 'attachment; filename=TrialBalance' + \
        str(datetime.now()) + '.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('TrialBalance')
    row_num = 0
    font_style = xlwt.XFStyle()

    columns = ('Account' , 'Description' , 'Debit' , 'Credit')


    all =  'SELECT Master_Sub_Account , cAccountTypeDescription , Debit , Credit FROM [Kyle].[dbo].[PostGL] AS genLedger'\
                ' Inner JOIN [Kyle].[dbo].[Accounts] '\
                'on Accounts.AccountLink = genLedger.AccountLink '\
                'Inner JOIN [Kyle].[dbo].[_etblGLAccountTypes] as AccountTypes '\
                'on Accounts.iAccountType = AccountTypes.idGLAccountType'\
                ' WHERE genLedger.AccountLink not in (161,162,163,164,165,166,167,168,122)'

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

    for col_num in range(len(xAll_l)):
        ws.write(row_num , col_num , columns[col_num] , font_style )

    font_style = xlwt.XFStyle()

    for row in xAll_l:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num , col_num , str(row[col_num]) , font_style)
    wb.save(response)

    return response

def settingsHome(request):

    allClass = SettingsClass.objects.all().order_by('Complex')
    return render(request, 'main/settingsHome.html' , {'allClass' : allClass})

def viewSettings(request,  settings_pk):
    setting = get_object_or_404(SettingsClass, pk=settings_pk)
    if request.method == 'GET':
        form = SettingUpdateForm(instance=setting)
        return render(request, 'main/viewSettings.html', {'setting': setting, 'form':form})
    else:
        form =  SettingUpdateForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('settingsHome')

    return render(request, 'main/viewSettings.html', {'setting': setting, 'form':form})

def newSetting(request):
    form = SettingsForm()

    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request , 'main/newSetting.html' , {'form':form})

def trb_Monthly(request , complexName):


    content = {}
    return render(request , 'main/trb_Monthly.html' , content)
