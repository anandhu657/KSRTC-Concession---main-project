from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id},{self.uname}'


class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname


class depot_master(models.Model):
    user_id = models.IntegerField()
    dpname = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)
    adr1 = models.CharField(max_length=300)
    adr2= models.CharField(max_length=300)
    pin = models.CharField(max_length=10)
    ph = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    lno = models.CharField(max_length=100)
    status = models.CharField(max_length=10)


class feedback(models.Model):
    user_id = models.IntegerField()
    fdbck = models.CharField(max_length=1000)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

class institution_master(models.Model):
    name = models.CharField(max_length=50)
    adrs1 = models.CharField(max_length=200)
    adrs2 = models.CharField(max_length=200)
    pin = models.CharField(max_length=20)
    ph = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    affili = models.CharField(max_length=50)
    govtpvt = models.CharField(max_length=20)
    princi_name = models.CharField(max_length=50)
    princi_ph = models.CharField(max_length=20)
    i_type = models.CharField(max_length=20)
    user_id = models.IntegerField()
    status = models.CharField(max_length=20)

class student_details(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    addr1 = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    dist = models.CharField(max_length=200)
    pin = models.CharField(max_length=20)
    father_name = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    g_contact = models.CharField(max_length=20)
    p_contact = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    year = models.IntegerField()
    institution_id = models.IntegerField()
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    pic = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

class app_form(models.Model):
    ap_dte = models.CharField(max_length=20)
    student_id = models.IntegerField()
    institution_id = models.IntegerField()
    depot_id = models.IntegerField()
    route_id = models.IntegerField()
    src = models.CharField(max_length=50)
    dest = models.CharField(max_length=50)
    status = models.CharField(max_length=20)


class bus_type_master(models.Model):
    bus_type = models.CharField(max_length=100)


class rate_master(models.Model):
    bus_type_id = models.IntegerField()
    stage = models.IntegerField()
    fare = models.FloatField()
    month_fare = models.FloatField()


class route_master(models.Model):
    depot_id = models.IntegerField()
    route_name = models.CharField(max_length=100)
    bus_type_id = models.IntegerField()
    src = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    status = models.CharField(max_length=10)


class stop_master(models.Model):
    depot_id = models.IntegerField()
    stop_name = models.CharField(max_length=100)


class route_stop_details(models.Model):
    route_id = models.IntegerField()
    stop_id = models.IntegerField()
    stop_no = models.IntegerField()
    stop_stage = models.IntegerField()

class consession_details(models.Model):
    app_id = models.IntegerField()
    c_number = models.CharField(max_length=100)
    stage_rate = models.FloatField()
    dt = models.CharField(max_length=20)
    year = models.IntegerField()
    month = models.IntegerField()
    no_months = models.IntegerField()
    status = models.CharField(max_length=100)

class consession_details_history(models.Model):
    app_id = models.IntegerField()
    c_number = models.CharField(max_length=100)
    stage_rate = models.FloatField()
    dt = models.CharField(max_length=20)
    year = models.IntegerField()
    month = models.IntegerField()
    no_months = models.IntegerField()
    status = models.CharField(max_length=100)
