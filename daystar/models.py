from django.db import models

class Baby(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    person_bringing_baby = models.CharField(max_length=100)
    time_of_arrival = models.DateTimeField()
    parents_names = models.CharField(max_length=200)
    fee_in_ugx = models.DecimalField(max_digits=10, decimal_places=2)
    period_of_stay = models.CharField(max_length=100)
    baby_number = models.CharField(max_length=20)
    sitter_assigned_to = models.CharField(max_length=100, default="Any")

    def __str__(self):
        return self.name


class Sitter(models.Model):
    
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    contacts = models.CharField(max_length=100, blank=True, null=True)
    on_duty = models.BooleanField(default=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Payment(models.Model):
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.sitter.name} - {self.date}"







class ProcurementItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class DollSale(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Doll sale for {self.baby.name}"



class Milk(DollSale):
    pass


class Fruits(models.Model):
    pass


class Diapers(models.Model):
    pass


# # ------------------------------------------------------------------
# class Procurement(models.Model):
#     ITEM_CHOICES = [
#         ('Diapers', 'Diapers'),
#         ('Fruits', 'Fruits'),
#         ('Milk', 'Milk'),
#         ('Dolls', 'Dolls'),
#     ]

#     item = models.CharField(max_length=50, choices=ITEM_CHOICES)
#     quantity = models.IntegerField()
#     price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()

#     def __str__(self):
#         return f"{self.quantity} of {self.item} procured"

# class DollSale(models.Model):
#     baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     sale_price = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()

#     def __str__(self):
#         return f"Doll sale for {self.baby.name}"

# x----------------------------------------

class Activity(models.Model):
    sitter_name = models.CharField(max_length=100)
    payment_amount = models.FloatField()
    baby_name = models.CharField(max_length=100)
    baby_parent = models.CharField(max_length=100)

    def __str__(self):
        return f"Activities for {self.sitter_name}"
    

class Notification(models.Model):
    type = models.BooleanField(default=True) # which would be a success status otherwise alert
    message = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.message