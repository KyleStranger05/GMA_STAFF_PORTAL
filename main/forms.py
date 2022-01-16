from django.forms import ModelForm
from .models import SettingsClass , ComplexListClass

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

class SettingsForm(ModelForm):
     class Meta:
         model = SettingsClass
         fields = ('Complex','Trial_balance_Year_to_date' , 'Trial_balance_Monthly' , 'Income_Statement_Year_to_date' , 'Income_Statement_Monthly' , 'Age_Analysis' , 'Balance_Sheet' , 'Repair_and_Maintenance_General_Ledger' , 'Major_capital_Items_General_Ledger')

class SettingUpdateForm(ModelForm):
    class Meta:
        model = SettingsClass
        exclude = ['Complex']

class ComplexListForm(ModelForm):
    class Meta:
        model = ComplexListClass
        fields = ('ComplexName' , 'NumberOfUnits')