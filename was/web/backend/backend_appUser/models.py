from tabnanny import verbose
from django.db import models

# 유저 정보
class User(models.Model):
    usernum = models.SmallAutoField(db_column='UserNum', primary_key=True)
    id = models.CharField(db_column='ID', unique=True, max_length=128, blank=True, null=True)
    pass_field = models.CharField(db_column='PASS', unique=False, max_length=128, blank=True, null=True)
    username = models.CharField(db_column='UserName', unique=False, max_length=32, blank=True, null=True)
    userphonenum = models.CharField(db_column='UserPhoneNUM', unique=True, max_length=32, blank=True, null=True)
    e_mail = models.CharField(db_column='E_Mail', unique=True, max_length=256, blank=True, null=True)
    userage = models.IntegerField(db_column='UserAge', unique=False, blank=True, null=True)
    commonusertype = models.IntegerField(db_column='CommonUserType', blank=True, null=True)
    adminusertype = models.IntegerField(db_column='AdminUserType', blank=True, null=True)

    # meta data
    class Meta:
        # managed = False
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'User'

    # naming data
    def __str__(self):
        return self.usernum

# 위치 추적 대상자 정보
class Target(models.Model):
    targetnum = models.SmallAutoField(db_column='TargetNum', primary_key=True)  # Field name made lowercase.
    usernum = models.ForeignKey('User', models.DO_NOTHING, db_column='UserNum')  # Field name made lowercase.
    targetname = models.CharField(db_column='TargetName', unique=False, max_length=32, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', unique=False, max_length=1, blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', unique=False, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', unique=False, blank=True, null=True)  # Field name made lowercase.
    targetage = models.IntegerField(db_column='TargetAge', unique=False, blank=True, null=True)  # Field name made lowercase.
    missingornot = models.IntegerField(db_column='MissingOrNot', unique=False, blank=True, null=True)  # Field name made lowercase.
    urgentnum = models.CharField(db_column='UrgentNum', unique=False, max_length=32, blank=True, null=True)  # Field name made lowercase.

    # meta data
    class Meta:
        # managed = False
        db_table = 'Target'
        unique_together = (('targetnum', 'usernum'),)
        verbose_name = 'Target'
        verbose_name_plural = 'Target'

    # naming data
    def __str__(self):
        return self.targetnum

# 위치 추적 장치 정보
class Device(models.Model):
    devicename = models.CharField(db_column='DeviceName', primary_key=True, max_length=64)  # Field name made lowercase.
    targetnum = models.ForeignKey('Target', models.DO_NOTHING, db_column='TargetNum')  # Field name made lowercase.
    usernum = models.ForeignKey('User', models.DO_NOTHING, db_column='UserNum')  # Field name made lowercase.

    # meta data
    class Meta:
        # managed = False
        db_table = 'Device'
        unique_together = (('devicename', 'targetnum', 'usernum'),)
        verbose_name = 'Device'
        verbose_name_plural = 'Device'

    # naming data
    def __str__(self):
        return self.devicename