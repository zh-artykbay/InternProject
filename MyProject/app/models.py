from django.db import models


class SulpakSmartphones(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakSmartphonesHistory(models.Model):
    phone_id = models.ForeignKey(SulpakSmartphones, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class SulpakTV(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakTVHistory(models.Model):
    phone_id = models.ForeignKey(SulpakTV, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class SulpakWatch(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakWatchHistory(models.Model):
    phone_id = models.ForeignKey(SulpakWatch, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakTablet(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakTabletHistory(models.Model):
    phone_id = models.ForeignKey(SulpakTablet, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class SulpakHeadphone(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakHeadphoneHistory(models.Model):
    phone_id = models.ForeignKey(SulpakHeadphone, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class SulpakPrinter(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakPrinterHistory(models.Model):
    phone_id = models.ForeignKey(SulpakPrinter, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class SulpakMonitor(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakMonitorHistory(models.Model):
    phone_id = models.ForeignKey(SulpakMonitor, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)


class SulpakVRglass(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakVRglassHistory(models.Model):
    phone_id = models.ForeignKey(SulpakVRglass, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class SulpakCamera(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


class SulpakCameraHistory(models.Model):
    phone_id = models.ForeignKey(SulpakCamera, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)

class SulpakPowerbank(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()
    image_url = models.URLField()


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

class TechnodomSmartphones(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.IntegerField()


class TechnodomSmartphonesHistory(models.Model):
    phone_id = models.ForeignKey(TechnodomSmartphones, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)
