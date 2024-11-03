from django.db import models


from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nomi')
    model_year = models.IntegerField(verbose_name = 'Yili')
    mileage = models.IntegerField(verbose_name = 'Kilometiri')
    horsepower = models.IntegerField(verbose_name = 'Ot kuchi')
    
    AT = 'Avtomatk'
    MX = 'Mexanik'
    
    transmission_type = (
        ('AT', 'Avtomatik'),
        ('MX', 'Mexanik'),
    )
    
    transmission = models.CharField(max_length=20, choices=transmission_type, default="Mexanik", verbose_name='Transmissiyasi')
    
    UZ = "so'm"
    ENG = '$'

    the_price = (
        (UZ, "so'm"),
        (ENG, "$"),
    )
    price_type = models.CharField(max_length=10, choices=the_price, default="so'm")
    price = models.IntegerField(verbose_name='Narxi')
    body = models.TextField(verbose_name="Ma'lumoti")
    image = models.ImageField(upload_to='cars/images', verbose_name='Rasmi')

    def __str__(self):
        return f"{self.name} ({self.model_year})"
    
    
    class Meta:
        db_table = 'Mashina'
        managed = True
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'

class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categories'  # 'Categorys' ni 'Categories' bilan almashtiring
        managed = True
        verbose_name = 'Kategoriyalar'
        verbose_name_plural = 'Kategoriyalar'

        
class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ism')
    email = models.EmailField(max_length=254, verbose_name='Email')
    message = models.TextField(verbose_name='Xabar')

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'Contact'
        managed = True
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqalar'