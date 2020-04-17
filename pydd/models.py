from django.db import models

# Create your models here.

class Spell(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    levels = [
        ('cantrip', 'Cantrip'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    ]
    level = models.CharField(choices=levels, max_length=12, default=0)
    school_choices = [
        ('Abjuration', 'Abjuration'),
        ('Conjuration', 'Conjuration'),
        ('Divination', 'Divination'),
        ('Enchantment', 'Enchantment'),
        ('Evocation', 'Evocation'),
        ('Illusion', 'Illusion'),
        ('Necromancy', 'Necromancy'),
        ('Transmutation', 'Transmutation'),
    ]
    school = models.CharField(choices=school_choices, max_length=20)
    casting_time = models.CharField(max_length=30)
    range = models.CharField(max_length=30)
    components_choices = [
        ('vsm', 'V, S, M'),
        ('vs', 'V, S'),
        ('vm', 'V, M'),
        ('sm', 'S, M'),
        ('v', 'V'),
        ('s', 'S'),
        ('m', 'M'),
    ]
    components = models.CharField(choices=components_choices, max_length=10)
    materials = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=60)
    description = models.TextField()