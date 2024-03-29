from django.shortcuts import render, HttpResponse, redirect

from app import models
from django import forms

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from app.utils.pagination import Pagination


# Create your views here.
def depart_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["deptname__contains"] = search_data

    queryset = models.Dept.objects.filter(**data_dict).order_by("deptorder")

    page_object = Pagination(request, queryset, page_size=5)

    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, 'depart_list.html', context)


class DeptModelFormAdd(forms.ModelForm):
    class Meta:
        model = models.Dept
        fields = ["deptname", "deptorder", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_deptname(self):
        txt_deptname = self.cleaned_data["deptname"]

        exists = models.Dept.objects.filter(deptname=txt_deptname).exists()
        if exists:
            raise ValidationError("Dept Name Existing")
        return txt_deptname


class DeptModelFormEbit(forms.ModelForm):
    deptname = forms.CharField(disabled=True)

    class Meta:
        model = models.Dept
        fields = ["deptname", "deptorder", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_deptname(self):
        txtdeptname = self.cleaned_data["deptname"]
        exists = models.Dept.objects.filter(deptname=txtdeptname).exclude(self.instance.pk).exists()
        if exists:
            raise ValidationError("Deptname Existing")
        return txtdeptname


def depart_add(request):
    if request.method == "GET":
        form = DeptModelFormAdd()
        return render(request, "depart_add.html", {"form": form})

    form = DeptModelFormAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/depart/list/")
    return render(request, "depart_add.html", {"form": form})


def depart_delete(request):
    nid = request.GET.get('nid')
    models.Dept.objects.filter(id=nid).delete()

    return redirect('/depart/list/')


def depart_ebit(request, nid):
    nowdepart = models.Dept.objects.filter(id=nid).first()
    if request.method == "GET":
        form = DeptModelFormEbit(instance=nowdepart)
        return render(request, "depart_ebit.html", {"form": form})
    form = DeptModelFormEbit(data=request.POST, instance=nowdepart)
    if form.is_valid():
        form.save()
        return redirect("/depart/list/")
    return render(request, "depart_ebit.html", {"form": form})


def role_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["role_name__contains"] = search_data
    queryset = models.Role.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=5)

    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, 'role_list.html', context)


class RoleModelFormAdd(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = ["role_name", "data_scope", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_role_name(self):
        txt_role_name = self.cleaned_data["role_name"]

        exists = models.Role.objects.filter(role_name=txt_role_name).exists()
        if exists:
            raise ValidationError("Role Name Existing")
        return txt_role_name


class RoleModelFormEbit(forms.ModelForm):
    role_name = forms.CharField(disabled=True)

    class Meta:
        model = models.Role
        fields = ["role_name", "data_scope", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_role_name(self):
        txt_role_name = self.cleaned_data["role_name"]
        exists = models.Role.objects.filter(role_name=txt_role_name).exclude(self.instance.pk).exists()
        if exists:
            raise ValidationError("Role Name Existing")
        return txt_role_name


def role_add(request):
    if request.method == "GET":
        form = RoleModelFormAdd()
        return render(request, "role_add.html", {"form": form})

    form = RoleModelFormAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/role/list/")
    return render(request, "role_add.html", {"form": form})


def role_delete(request):
    nid = request.GET.get('nid')
    models.Role.objects.filter(id=nid).delete()

    return redirect('/role/list/')


def role_ebit(request, nid):
    nowrole = models.Role.objects.filter(id=nid).first()
    if request.method == "GET":
        form = RoleModelFormEbit(instance=nowrole)
        return render(request, "role_ebit.html", {"form": form})
    form = RoleModelFormEbit(data=request.POST, instance=nowrole)
    if form.is_valid():
        form.save()
        return redirect("/role/list/")
    return render(request, "role_ebit.html", {"form": form})


def user_list(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["role_name__contains"] = search_data
    queryset = models.UserInfo.objects.all()

    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'user_list.html', context)


class UserModelForm(forms.ModelForm):
    username = forms.CharField(min_length=3, max_length=100)
    password = forms.CharField(min_length=6, max_length=200)

    class Meta:
        model = models.UserInfo
        fields = ["username", "password", "nick_name", "gender","age", "usertype", "email", "phonenumber", "depart", "roles", "employment_time", "create_time", "accoun_status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add.html', {"form": form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_add.html', {"form": form})


def user_delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')

def user_ebit(request,nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {"form": form})

