from django.db import models

# Create your models here.
class Subscribers(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.IntegerField(primary_key=True)
    # password = models.PasswordField()

    def __str__(self):
        return '%s %s %s' % (self.username, self.email, self.phone)

class Teams(models.Model):
    teamname = models.CharField(max_length=20)
    def __str__(self):
        return self.teamnane

class Fixtures(models.Model):
    date = models.DateTimeField()
    fieldvenue = models.CharField(max_length=20)
    team = models.ForeignKey(Teams, on_delete=models.PROTECT)

    def __str__(self):
        return '% % %' % (self.team, self.date, self.fieldvenue)

class Predictions(models.Model):
    teama_odds = models.DecimalField(decimal_places=2, max_digits=5)
    teamb_odds = models.DecimalField(decimal_places=2, max_digits=5)
    description_predictions = models.TextField(max_length=50)

    def __str__(self):
        return '% % %' % (self.teama_odds, self.teamb_odds, self.description_predictions)