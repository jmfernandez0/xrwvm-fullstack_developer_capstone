# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    # Many-to-One relationship: one CarMake -> many CarModel
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Dealer ID referring to dealer in Cloudant (your external dealer DB)
    dealer_id = models.IntegerField()

    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
    ]

    # Field name per spec/sample: "type"
    type = models.CharField(max_length=12, choices=CAR_TYPES, default='SUV')

    # Year with min/max validators
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )

    # Optional extra field (harmless, useful)
    # description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
