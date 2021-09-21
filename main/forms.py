from django.forms import ModelForm
from .models import SettingsClass

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

class SettingsForm(ModelForm):
     class Meta:
         model = SettingsClass
         fields = ('Complex','Trial_balance_Year_to_date' , 'Trial_balance_Monthly' , 'Income_Statement_Year_to_date' , 'Income_Statement_Monthly' , 'Age_Analysis' , 'Balance_Sheet' , 'Repair_and_Maintenance_General_Ledger' , 'Major_capital_Items_General_Ledger')

class SettingUpdateForm(ModelForm):
    class Meta:
        model = SettingsClass
        fields = '__all__'
