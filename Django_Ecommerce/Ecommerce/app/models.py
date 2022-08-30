from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
DISTRICT_CHOICE = (
    ('Barisal', 'Barisal'), ('Barguna', 'Barguna'), ('Bhola', 'Bhola'), ('Jhalokathi', 'Jhalokathi'),
    ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Chittagong', 'Chittagong'), ('Bandarban', 'Bandarban'),
    ('Brahmanbaria', 'Brahmanbaria'), ('Chadpur', 'Chadpur'),
    ('Comilla', 'Comilla'), ("Cox's Bazar", "Cox's Bazar"), ('Feni', 'Feni'), ('Khagrachhari', 'Khagrachhari'),
    ('Lakshmipur', 'Lakshmipur'),
    ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'),
    ('Gazipur', 'Gazipur'), ('Gopalgang', 'Gopalgang'),
    ('Kishpreganj', 'Kishpreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'),
    ('Munshiganj', 'Munshiganj'), ('Narayanganj', 'Narayanganj'),
    ('Narshingdi', 'Narshingdi'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Tangail', 'Tangail'),
    ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jessore', 'Jessore'), ('Jhenaidah', 'Jhenaidah'),
    ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'),
    ('Satkhira', 'Satkhira'), ('Mymanshing', 'Mymanshing'), ('Jamalpur', 'Jamalpur'), ('Netrokona', 'Netrokona'),
    ('Sherpur', 'Sherpur'),
    ('Rajshahi', 'Rajshahi'), ('Bogura', 'Bogura'), ('Joypurhat', 'Joypurhat'), ('Naogaon', 'Naogaon'),
    ('Natore', 'Natore'), ('Chapai', 'Chapai'), ('Nawabgonj', 'Nawabgonj'), ('Pabna', 'Pabna'),
    ('Sirajganj', 'Sirajganj'),
    ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'),
    ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'),
    ('Sylhet', 'Sylhet'), ('Habiganj', 'Habiganj'), ('Moulvibazar', 'Moulvibazar'), ('Sunamganj', 'Sunamganj')
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    division = models.CharField(max_length=50)
    district = models.CharField(choices=DISTRICT_CHOICE, max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICE = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear')
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __Str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_amount(self):
        return self.quantity * self.product.discount_price


STATUS_CHOICE = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')

)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Pending')

    @property
    def total_amount(self):
        return self.quantity * self.product.discount_price