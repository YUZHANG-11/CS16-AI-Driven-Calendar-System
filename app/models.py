from django.db import models


# Create your models here.
class Dept(models.Model):
    deptname = models.CharField(max_length=100)
    deptorder = models.IntegerField(verbose_name="order")
    status_choices = (
        (1, "normal"),
        (2, "Deactivate"),
    )
    status = models.SmallIntegerField(choices=status_choices)

    def __str__(self):
        return self.deptname


class Menu(models.Model):
    menuname = models.CharField(max_length=100)
    order_num = models.IntegerField
    path = models.CharField(max_length=100)
    status_choices = (
        (1, "normal"),
        (2, "Deactivate"),
    )
    status = models.SmallIntegerField(choices=status_choices)
    component = models.CharField(max_length=100)

    menu_type_choices = (
        (1, "Catalogue"),
        (2, "Menu"),
        (3, "Button"),
    )
    menu_type = models.SmallIntegerField(choices=menu_type_choices)


class Role(models.Model):
    role_name = models.CharField(max_length=50)

    data_scope_choices = (
        (1, "All"),
        (2, "NowDept"),
        (3, "Basic"),
    )

    data_scope = models.SmallIntegerField(choices=data_scope_choices)

    def __str__(self):
        return self.role_name

    status_choices = (
        (1, "normal"),
        (2, "Deactivate"),
    )
    status = models.SmallIntegerField(choices=status_choices)


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=50)
    age = models.IntegerField()

    user_type_choices = (
        (1, "system_user"),
        (2, "ordinary_user"),
    )
    usertype = models.SmallIntegerField(choices=user_type_choices)
    email = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    gender_choices = (
        (1, "male"),
        (2, "female"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    create_time = models.DateField()
    employment_time = models.DateField()
    accoun_status_choices = (
        (1, "normal"),
        (2, "Deactivate"),
    )
    accoun_status = models.SmallIntegerField(choices=accoun_status_choices)

    depart = models.ForeignKey(to="Dept", to_field="id", on_delete=models.CASCADE)
    roles = models.ForeignKey(to="Role", to_field="id", on_delete=models.CASCADE)
