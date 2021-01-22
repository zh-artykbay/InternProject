from django.db import models


class SulpakSmartphones(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakSmartphonesHistory(models.Model):
    phone_id = models.ForeignKey(SulpakSmartphones, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakTV(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakTVHistory(models.Model):
    phone_id = models.ForeignKey(SulpakTV, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakWatch(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakWatchHistory(models.Model):
    phone_id = models.ForeignKey(SulpakWatch, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakTablet(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakTabletHistory(models.Model):
    phone_id = models.ForeignKey(SulpakTablet, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakHeadphone(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakHeadphoneHistory(models.Model):
    phone_id = models.ForeignKey(SulpakHeadphone, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakPrinter(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakPrinterHistory(models.Model):
    phone_id = models.ForeignKey(SulpakPrinter, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakMonitor(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakMonitorHistory(models.Model):
    phone_id = models.ForeignKey(SulpakMonitor, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakVRglass(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakVRglassHistory(models.Model):
    phone_id = models.ForeignKey(SulpakVRglass, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakCamera(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakCameraHistory(models.Model):
    phone_id = models.ForeignKey(SulpakCamera, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakPowerbank(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class SulpakPowerbankHistory(models.Model):
    phone_id = models.ForeignKey(SulpakPowerbank, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)




class MechtaSmartphones(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()


class MechtaSmartphonesHistory(models.Model):
    phone_id = models.ForeignKey(MechtaSmartphones, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)




class ShopKzSmartphones(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()


class ShopKzSmartphonesHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzSmartphones, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzTV(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzTVHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzTV, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzWatch(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzWatchHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzWatch, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzTablet(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzTabletHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzTablet, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzHeadphone(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzHeadphoneHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzHeadphone, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzPrinter(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzPrinterHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzPrinter, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzMonitor(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzMonitorHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzMonitor, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzVRglass(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzVRglassHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzVRglass, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzCamera(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzCameraHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzCamera, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class ShopKzPowerbank(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class ShopKzPowerbankHistory(models.Model):
    phone_id = models.ForeignKey(ShopKzPowerbank, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)




class TechnodomSmartphones(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()


class TechnodomSmartphonesHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomSmartphones, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class TechnodomTV(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomTVHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomTV, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomWatch(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomWatchHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomWatch, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomTablet(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomTabletHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomTablet, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomHeadphone(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomHeadphoneHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomHeadphone, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomPrinter(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomPrinterHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomPrinter, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomMonitor(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomMonitorHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomMonitor, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomVRglass(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomVRglassHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomVRglass, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomCamera(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomCameraHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomCamera, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class TechnodomPowerbank(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()

class TechnodomPowerbankHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomPowerbank, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)



class Monitor(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakMonitor, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzMonitor, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomMonitor, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)


class Camera(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakCamera, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzCamera, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomCamera, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)



class Headphone(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakHeadphone, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzHeadphone, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomHeadphone, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)



class Powerbank(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakPowerbank, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzPowerbank, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomPowerbank, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)


class Printer(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakPrinter, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzPrinter, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomPrinter, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)


class Smartphone(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakSmartphones, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzSmartphones, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomSmartphones, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)


class Watch(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakWatch, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzWatch, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomWatch, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)


class Tablet(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakTablet, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzTablet, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomTablet, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)


class TV(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakTV, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzTV, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomTV, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)


class VRglass(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    sulpak_id = models.ForeignKey(SulpakVRglass, on_delete=models.CASCADE, null=True, blank=True)
    shopkz_id = models.ForeignKey(ShopKzVRglass, on_delete=models.CASCADE, null=True, blank=True)
    technodom_id = models.ForeignKey(TechnodomVRglass, on_delete=models.CASCADE, null=True, blank=True)
    sulpak_name = models.CharField(max_length=500, blank=False, default='')
    sulpak_price = models.IntegerField(null=True, blank=True)
    technodom_name = models.CharField(max_length=500, blank=False, default='')
    technodom_price = models.IntegerField(null=True, blank=True)
    shopkz_name = models.CharField(max_length=500, blank=False, default='')
    shopkz_price = models.IntegerField(null=True, blank=True)

