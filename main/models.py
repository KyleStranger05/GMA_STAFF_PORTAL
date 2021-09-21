from django.db import models


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


# Create your models here.
class SettingsClass(models.Model):

    Complex = models.CharField(choices=complex_list , max_length =  22 ,default='1' , unique=True)

    #Trial Balance Year To Date
    Trial_balance_Year_to_date= models.BooleanField(default = False)
    tbytd_Include_opening_balances=models.BooleanField(default = False)
    tbytd_Only_use_main_accounts=models.BooleanField(default = False)
    tbytd_Print_null_values=models.BooleanField(default = False)
    tbytd_Print_description=models.BooleanField(default = True)
    tbytd_Print_account=models.BooleanField(default = True)
    tbytd_Sort_by_account_name=models.BooleanField(default = True)

    #Trial Balance Monthly
    Trial_balance_Monthly=models.BooleanField(default = False)
    tbm_Only_use_main_accounts=models.BooleanField(default = False)
    tbm_Print_null_values=models.BooleanField(default = False)
    tbm_Print_description=models.BooleanField(default = True)
    tbm_Print_account=models.BooleanField(default = True)
    tbm_Sort_by_account_name=models.BooleanField(default = True)

    #Income Statement Year To Date
    Income_Statement_Year_to_date=models.BooleanField(default = False)
    isytd_Only_use_main_accounts=models.BooleanField(default = False)
    isytd_Sort_by_account_name=models.BooleanField(default = True)
    isytd_Print_null_values=models.BooleanField(default = False)
    isytd_Print_description=models.BooleanField(default = True)
    isytd_Print_account=models.BooleanField(default = True)

    #Income Statement Monthly
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
