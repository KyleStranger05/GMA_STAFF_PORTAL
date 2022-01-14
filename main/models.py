from django.db import models

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
                ('Prudential House','Prudential House'),
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

# Create your models here.
class SettingsClass(models.Model):

    Complex = models.CharField(choices=complex_list , max_length =  50 ,default='1' , unique=True)

    #Trial Balance Year To Date  Completed
    Trial_balance_Year_to_date= models.BooleanField(default = False)
    tbytd_Include_opening_balances=models.BooleanField(default = False)
    tbytd_Only_use_main_accounts=models.BooleanField(default = False)
    tbytd_Print_null_values=models.BooleanField(default = False)
    tbytd_Print_description=models.BooleanField(default = True)
    tbytd_Print_account=models.BooleanField(default = True)
    tbytd_Sort_by_account_name=models.BooleanField(default = True)

    #Trial Balance Monthly Completed
    Trial_balance_Monthly=models.BooleanField(default = False)
    tbm_Only_use_main_accounts=models.BooleanField(default = False)
    tbm_Print_null_values=models.BooleanField(default = False)
    tbm_Print_description=models.BooleanField(default = True)
    tbm_Print_account=models.BooleanField(default = True)
    tbm_Sort_by_account_name=models.BooleanField(default = True)

    #Income Statement Year To Date Completed
    Income_Statement_Year_to_date=models.BooleanField(default = False)
    isytd_Only_use_main_accounts=models.BooleanField(default = False)
    isytd_Sort_by_account_name=models.BooleanField(default = True)
    isytd_Print_null_values=models.BooleanField(default = False)
    isytd_Print_description=models.BooleanField(default = True)
    isytd_Print_account=models.BooleanField(default = True)

    #Income Statement Monthly Completed
    Income_Statement_Monthly=models.BooleanField(default = False)
    ism_Only_use_main_accounts=models.BooleanField(default = False)
    ism_Sort_by_account_name=models.BooleanField(default = True)
    ism_Print_null_values=models.BooleanField(default = False)
    ism_Print_description=models.BooleanField(default = True)
    ism_Print_account=models.BooleanField(default = True)

    #Age Analysis
    Age_Analysis=models.BooleanField(default = False)
    aa_Include_all_customers=models.BooleanField(default = True)
    aa_Include_cash_customers=models.BooleanField(default = True)
    aa_include_on_hold_customers=models.BooleanField(default = True)
    aa_include_null_values=models.BooleanField(default = False)
    aa_allocate_unalocated_credits_to_oldest=models.BooleanField(default = True)

    #Balance Sheet
    Balance_Sheet=models.BooleanField(default = False)
    bs_Only_use_main_accounts=models.BooleanField(default = False)
    bs_Print_current_month=models.BooleanField(default = True)
    bs_Include_null_values=models.BooleanField(default = False)
    bs_Print_assets_first=models.BooleanField(default = True)
    bs_statement_of_financial_position=models.BooleanField(default = False)

    #Repair and Maintenance General Ledger
    Repair_and_Maintenance_General_Ledger=models.BooleanField(default = False)
    rmgl_Ignore_inactive_accounts=models.BooleanField(default = True)
    rmgl_Sort_by_transaction_date=models.BooleanField(default = True)
    rmgl_Group_by_account_type=models.BooleanField(default = True)
    rmgl_Print_description=models.BooleanField(default = True)
    rmgl_Print_account=models.BooleanField(default = True)
    rmgl_Print_year_to_date=models.BooleanField(default = True)
    rmgl_Print_monthly=models.BooleanField(default = False)

    #Major Capital Items General Ledger
    Major_capital_Items_General_Ledger=models.BooleanField(default = False)
    mcigl_Ignore_inactive_accounts=models.BooleanField(default = True)
    mcigl_Sort_by_transaction_date=models.BooleanField(default = True)
    mcigl_Group_by_account_type=models.BooleanField(default = True)
    mcigl_Print_description=models.BooleanField(default = True)
    mcigl_Print_account=models.BooleanField(default = True)
    mcigl_Print_year_to_date=models.BooleanField(default = True)
    mcigl_Print_monthly=models.BooleanField(default = False)

    def __str__(self):
        return (self.Complex + ' Settings')

class ComplexListClass(models.Model):
    ComplexName = models.CharField(choices=complex_list , max_length =  50 ,default='1' , unique=True)
    NumberOfUnits = models.IntegerField(max_length=2 , blank=False , default=1 )

    def __str__(self):
        return (self.ComplexName)


