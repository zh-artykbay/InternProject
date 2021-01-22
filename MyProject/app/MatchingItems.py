from fuzzywuzzy import process

from app.models import SulpakSmartphones
from app.models import TechnodomSmartphones
from app.models import ShopKzSmartphones
from app.models import Smartphone

from app.models import Camera, SulpakCamera, ShopKzCamera, TechnodomCamera
from app.models import Headphone, SulpakHeadphone, ShopKzHeadphone, TechnodomHeadphone
from app.models import Monitor, SulpakMonitor, ShopKzMonitor, TechnodomMonitor
from app.models import Powerbank, SulpakPowerbank, ShopKzPowerbank, TechnodomPowerbank
from app.models import Printer, SulpakPrinter, ShopKzPrinter, TechnodomPrinter
from app.models import Watch, SulpakWatch, ShopKzWatch, TechnodomWatch
from app.models import Tablet, SulpakTablet, ShopKzTablet, TechnodomTablet
from app.models import TV, SulpakTV, ShopKzTV, TechnodomTV
from app.models import VRglass, SulpakVRglass, ShopKzVRglass, TechnodomVRglass


def match_items(Sulpak_Item_table, Technodom_Item_table, Shopkz_Item_table, Item_table):


    sulpak_all_items = Sulpak_Item_table.objects.all()
    technodom_all_items = Technodom_Item_table.objects.all()
    shopkz_all_items = Shopkz_Item_table.objects.all()

    choices_sulpak = [i.name for i in sulpak_all_items]
    choices_technodom = [i.name for i in technodom_all_items]
    choices_shopkz = [i.name for i in shopkz_all_items]



    for technodom_item in technodom_all_items:
        if not Item_table.objects.filter(technodom_id=technodom_item.id).exists():
            shopkz_result = process.extractOne(technodom_item.name, choices_shopkz)
            sulpak_result = process.extractOne(technodom_item.name, choices_sulpak)

            if shopkz_result[1] >= 95:
                shopkz_new_item = Shopkz_Item_table.objects.get(name=shopkz_result[0])
            else:
                shopkz_new_item = None

            if sulpak_result[1] >= 95:
                sulpak_new_item = Sulpak_Item_table.objects.get(name=sulpak_result[0])
            else:
                sulpak_new_item = None

            new_item = Item_table(name=technodom_item.name, sulpak_id=sulpak_new_item, shopkz_id=shopkz_new_item,
                                  technodom_id=technodom_item,
                                  technodom_name=technodom_item.name, technodom_price=technodom_item.current_price,
                                  )
            new_item.save()

            if shopkz_new_item:
                new_item.shopkz_name = shopkz_new_item.name
                new_item.shopkz_price = shopkz_new_item.current_price
                new_item.save()
            if sulpak_new_item:
                new_item.sulpak_name = sulpak_new_item.name
                new_item.sulpak_price = sulpak_new_item.current_price
                new_item.save()



    for sulpak_item in sulpak_all_items:
        if not Item_table.objects.filter(sulpak_id=sulpak_item.id).exists():
            technodom_result = process.extractOne(sulpak_item.name, choices_technodom)
            shopkz_result = process.extractOne(sulpak_item.name, choices_shopkz)

            if technodom_result[1] >= 95:
                technodom_new_item = Technodom_Item_table.objects.get(name=technodom_result[0])
            else:
                technodom_new_item = None

            if shopkz_result[1] >= 95:
                shopkz_new_item = Shopkz_Item_table.objects.get(name=shopkz_result[0])
            else:
                shopkz_new_item = None


            new_item = Item_table(name=sulpak_item.name, sulpak_id=sulpak_item, shopkz_id=shopkz_new_item,
                                  technodom_id=technodom_new_item,
                                  sulpak_name=sulpak_item.name, sulpak_price=sulpak_item.current_price
                                  )
            new_item.save()

            if shopkz_new_item:
                new_item.shopkz_name = shopkz_new_item.name
                new_item.shopkz_price = shopkz_new_item.current_price
                new_item.save()
            if technodom_new_item:
                new_item.technodom_name = technodom_new_item.name
                new_item.technodom_price = technodom_new_item.current_price
                new_item.save()


    for shopkz_item in shopkz_all_items:
        if not Item_table.objects.filter(shopkz_id=shopkz_item.id).exists():
            technodom_result = process.extractOne(shopkz_item.name, choices_technodom)
            sulpak_result = process.extractOne(shopkz_item.name, choices_sulpak)

            if technodom_result[1] >= 95:
                technodom_new_item = Technodom_Item_table.objects.get(name=technodom_result[0])
            else:
                technodom_new_item = None

            if sulpak_result[1] >= 95:
                sulpak_new_item = Sulpak_Item_table.objects.get(name=sulpak_result[0])
            else:
                sulpak_new_item = None

            new_item = Item_table(name=shopkz_item.name, sulpak_id=sulpak_new_item, shopkz_id=shopkz_item,
                                  technodom_id=technodom_new_item,
                                  shopkz_name=shopkz_item.name, shopkz_price=shopkz_item.current_price)
            new_item.save()

            if technodom_new_item:
                new_item.technodom_name = technodom_new_item.name
                new_item.technodom_price = technodom_new_item.current_price
                new_item.save()
            if sulpak_new_item:
                new_item.sulpak_name = sulpak_new_item.name
                new_item.sulpak_price = sulpak_new_item.current_price
                new_item.save()



match_items(Sulpak_Item_table=SulpakSmartphones, Shopkz_Item_table=ShopKzSmartphones, Technodom_Item_table=TechnodomSmartphones, Item_table=Smartphone)
match_items(Sulpak_Item_table=SulpakMonitor, Shopkz_Item_table=ShopKzMonitor, Technodom_Item_table=TechnodomMonitor, Item_table=Monitor)
match_items(Sulpak_Item_table=SulpakPowerbank, Shopkz_Item_table=ShopKzPowerbank, Technodom_Item_table=TechnodomPowerbank, Item_table=Powerbank)
match_items(Sulpak_Item_table=SulpakPrinter, Shopkz_Item_table=ShopKzPrinter, Technodom_Item_table=TechnodomPrinter, Item_table=Printer)
match_items(Sulpak_Item_table=SulpakWatch, Shopkz_Item_table=ShopKzWatch, Technodom_Item_table=TechnodomWatch, Item_table=Watch)
match_items(Sulpak_Item_table=SulpakTablet, Shopkz_Item_table=ShopKzTablet, Technodom_Item_table=TechnodomTablet, Item_table=Tablet)
match_items(Sulpak_Item_table=SulpakTV, Shopkz_Item_table=ShopKzTV, Technodom_Item_table=TechnodomTV, Item_table=TV)
match_items(Sulpak_Item_table=SulpakVRglass, Shopkz_Item_table=ShopKzVRglass, Technodom_Item_table=TechnodomVRglass, Item_table=VRglass)

match_items(Sulpak_Item_table=SulpakCamera, Shopkz_Item_table=ShopKzCamera, Technodom_Item_table=TechnodomCamera, Item_table=Camera)
match_items(Sulpak_Item_table=SulpakHeadphone, Shopkz_Item_table=ShopKzHeadphone, Technodom_Item_table=TechnodomHeadphone, Item_table=Headphone)
