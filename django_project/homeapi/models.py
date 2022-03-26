from django.db import models

# Create your models here.

class RoomButton(models.Model):
    led_status = models.IntegerField()
    door_status = models.IntegerField()
    esaving_status = models.IntegerField()
    aircon_status = models.IntegerField()

    def __str__(self):
        return "Manager your room {}".format(self.pk)


class Todolist(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return "{} 今日のやるべき事：{}".format(self.pk, self.title)

class RoomStatus(models.Model):
    temperature = models.CharField(max_length=64)
    pressure = models.CharField(max_length=64)
    humidity = models.CharField(max_length=64)

    def __str__(self):
        return "temp:{} ~~ pres:{} ~~ humi:{}".format(self.temperature,
                                                      self.pressure,
                                                      self.humidity)

