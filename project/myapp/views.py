from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

################## ADMIN ###############################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

from .models import bus_type_master
def admin_bus_type_master_add(request):
    if request.method == 'POST':
        bus_type = request.POST.get('bus_type')
        jm = bus_type_master(bus_type=bus_type)
        jm.save()
        context = {'msg': 'New Bus Record Added'}
        return render(request, './myapp/admin_bus_type_master_add.html', context)
    else:
        return render(request, './myapp/admin_bus_type_master_add.html')

def admin_bus_type_master_edit(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        bus_type = request.POST.get('bus_type')
        jm = bus_type_master.objects.get(id=int(s_id))

        jm.bus_type = bus_type
        jm.save()
        msg = 'Bus Record Updated'
        jm_l = bus_type_master.objects.all()
        context = {'bus_list': jm_l, 'msg': msg}
        return render(request, './myapp/admin_bus_type_master_view.html', context)
    else:
        id = request.GET.get('id')
        jm = bus_type_master.objects.get(id=int(id))
        context = {'bus_type': jm.bus_type, 's_id': jm.id}
        return render(request, './myapp/admin_bus_type_master_edit.html',context)


def admin_bus_type_master_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    jm = bus_type_master.objects.get(id=int(id))
    jm.delete()
    msg = 'Record Deleted'
    jm_l = bus_type_master.objects.all()
    context = {'bus_list': jm_l, 'msg':msg}
    return render(request, './myapp/admin_bus_type_master_view.html',context)


def admin_bus_type_master_view(request):
    jm_l = bus_type_master.objects.all()
    context = {'bus_list':jm_l}
    return render(request, './myapp/admin_bus_type_master_view.html',context)

from .models import rate_master
def admin_rate_master_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':

        bus_type_id = int(request.POST.get('bus_type_id'))
        stage = int(request.POST.get('stage'))
        fare = float(request.POST.get('fare'))
        month_fare = float(request.POST.get('month_fare'))


        pd = rate_master(bus_type_id=bus_type_id,stage=stage,fare=fare,
                         month_fare=month_fare)
        pd.save()
        hs_l = bus_type_master.objects.all()
        context = {'bus_list':hs_l,'msg': 'Record Added'}
        return render(request, './myapp/admin_rate_master_add.html', context)
    else:
        hs_l = bus_type_master.objects.all()
        context = {'bus_list': hs_l, 'msg': ''}
        return render(request, './myapp/admin_rate_master_add.html', context)


def admin_rate_master_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)

    pd = rate_master.objects.get(id=int(id))
    pd.delete()
    msg = 'Rate Record Deleted'

    pd_l = rate_master.objects.all()
    hs_l = bus_type_master.objects.all()
    context = {'rate_list': pd_l,'bus_list':hs_l,'msg':msg}
    return render(request, './myapp/admin_rate_master_view.html',context)

def admin_rate_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    pd_l = rate_master.objects.all()
    hs_l = bus_type_master.objects.all()
    context = {'rate_list': pd_l, 'bus_list': hs_l, 'msg': ''}
    return render(request, './myapp/admin_rate_master_view.html', context)


from .models import depot_master
def admin_depot_master_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':

        dpname = request.POST.get('dpname')
        dist = request.POST.get('dist')
        adr1 = request.POST.get('adr1')
        adr2 = request.POST.get('adr2')
        pin = request.POST.get('pin')
        ph = request.POST.get('ph')

        email = request.POST.get('email')
        lno = request.POST.get('lno')
        status = 'ok'
        uname = email
        password ='1234'

        ul = user_login(uname=uname, passwd=password, u_type='depot')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        pd = depot_master(user_id=user_id,dpname=dpname,dist=dist,
                          adr1=adr1,adr2=adr2,pin=pin,ph=ph,email=email,
                          lno=lno,status=status)
        pd.save()
        context = {'msg': 'Record Added'}
        return render(request, './myapp/admin_depot_master_add.html', context)
    else:

        context = { 'msg': ''}
        return render(request, './myapp/admin_depot_master_add.html', context)



def admin_depot_master_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        dpname = request.POST.get('dpname')
        dist = request.POST.get('dist')
        adr1 = request.POST.get('adr1')
        adr2 = request.POST.get('adr2')
        pin = request.POST.get('pin')
        ph = request.POST.get('ph')

        email = request.POST.get('email')
        lno = request.POST.get('lno')

        pd = depot_master.objects.get(id=int(s_id))

        pd.dpname = dpname
        pd.dist = dist
        pd.adr1 = adr1
        pd.adr2 = adr2
        pd.pin =pin
        pd.ph = ph
        pd.email = email
        pd.lno =lno

        pd.save()
        msg = 'Depot Record Updated'
        pd_l = depot_master.objects.all()
        context = {'depot_list': pd_l, 'msg': msg}
        return render(request, './myapp/admin_depot_master_view.html', context)
    else:
        id = request.GET.get('id')

        od = depot_master.objects.get(id=int(id))
        context = {'od':od,'s_id':od.id}
        return render(request, './myapp/admin_depot_master_edit.html',context)

def admin_depot_master_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)

    pd = depot_master.objects.get(id=int(id))
    ul = user_login.objects.get(id=pd.user_id)
    ul.delete()
    pd.delete()
    msg = 'Record Deleted'
    pd_l = depot_master.objects.all()
    context = {'depot_list': pd_l,'msg':msg}
    return render(request, './myapp/admin_depot_master_view.html',context)

def admin_depot_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    pd_l = depot_master.objects.all()
    context = {'depot_list':pd_l}
    return render(request, './myapp/admin_depot_master_view.html',context)




######################################################################
################ DEPOT ##########################################
def depot_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='depot')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            context = {'uname' : uname }
            return render(request,'./myapp/depot_home.html',context)
        else:
            msg = ' Invalid Uname or Password !!!'
            context ={ 'msg':msg }
            return render(request, './myapp/depot_login.html',context)
    else:
        msg = ''
        context ={ 'msg':msg }
        return render(request, './myapp/depot_login.html',context)


def depot_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)
    else:
        context = {'uname': uname}
        return render(request,'./myapp/depot_home.html',context)


def depot_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return depot_login(request)
    else:
        return depot_login(request)

def depot_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname, passwd=opasswd, u_type='depot')
            if ul is not None:
                ul.passwd = npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/depot_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/depot_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/depot_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/depot_changepassword.html', context)

def depot_rate_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    bus_type_id = request.GET.get('bus_type_id')
    pd_l = rate_master.objects.filter(bus_type_id=int(bus_type_id))
    hs_l = bus_type_master.objects.all()
    context = {'rate_list': pd_l, 'bus_list': hs_l, 'msg': ''}
    return render(request, './myapp/depot_rate_master_view.html', context)

def depot_bus_type_master_view(request):
    jm_l = bus_type_master.objects.all()
    context = {'bus_list':jm_l}
    return render(request, './myapp/depot_bus_type_master_view.html',context)


from .models import stop_master
def depot_stop_master_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        dm = depot_master.objects.get(user_id=int(user_id))

        stop_name = request.POST.get('stop_name')
        jm = stop_master(depot_id= dm.id,stop_name=stop_name)
        jm.save()
        context = {'msg': 'New Stop Record Added'}
        return render(request, './myapp/depot_stop_master_add.html', context)
    else:
        return render(request, './myapp/depot_stop_master_add.html')

def depot_stop_master_edit(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        user_id = request.session['user_id']
        dm = depot_master.objects.get(user_id=int(user_id))
        stop_name = request.POST.get('stop_name')
        jm = stop_master.objects.get(id=int(s_id))

        jm.stop_name = stop_name
        jm.save()
        msg = 'Stop Record Updated'
        jm_l = stop_master.objects.filter(depot_id=dm.id)
        context = {'stop_list': jm_l, 'msg': msg}
        return render(request, './myapp/depot_stop_master_view.html', context)
    else:
        id = request.GET.get('id')
        jm = stop_master.objects.get(id=int(id))
        context = {'stop_name': jm.stop_name, 's_id': jm.id}
        return render(request, './myapp/depot_stop_master_edit.html',context)


def depot_stop_master_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    jm = bus_type_master.objects.get(id=int(id))
    jm.delete()
    msg = 'Record Deleted'

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    jm_l = stop_master.objects.filter(depot_id=dm.id)
    context = {'stop_list': jm_l, 'msg':msg}
    return render(request, './myapp/depot_stop_master_view.html',context)


def depot_stop_master_view(request):
    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    jm_l = stop_master.objects.filter(depot_id=dm.id)
    context = {'stop_list': jm_l, 'msg': ''}
    return render(request, './myapp/depot_stop_master_view.html', context)

from .models import route_master
def depot_route_master_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    if request.method == 'POST':
        user_id = request.session['user_id']
        dm = depot_master.objects.get(user_id=int(user_id))
        depot_id = dm.id
        bus_type_id = int(request.POST.get('bus_type_id'))
        route_name = request.POST.get('route_name')
        src = request.POST.get('src')
        dest = request.POST.get('dest')
        status = 'new'

        pd = route_master(bus_type_id=bus_type_id,depot_id=depot_id,route_name=route_name,
                          src=src, dest=dest,status=status)
        pd.save()
        hs_l = bus_type_master.objects.all()
        context = {'bus_list':hs_l,'msg': 'Record Added'}
        return render(request, './myapp/depot_route_master_add.html', context)
    else:
        hs_l = bus_type_master.objects.all()
        context = {'bus_list': hs_l, 'msg': ''}
        return render(request, './myapp/depot_route_master_add.html', context)


def depot_route_master_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    pd = route_master.objects.get(id=int(id))
    pd.delete()
    msg = 'Route Record Deleted'

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id
    pd_l = route_master.objects.filter(depot_id=depot_id)
    hs_l = bus_type_master.objects.all()
    context = {'route_list': pd_l,'bus_list':hs_l,'msg':msg}
    return render(request, './myapp/depot_route_master_view.html',context)

def depot_route_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    user_id = request.session['user_id']
    print(user_id)
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id
    pd_l = route_master.objects.filter(depot_id=depot_id)
    hs_l = bus_type_master.objects.all()
    context = {'route_list': pd_l, 'bus_list': hs_l, 'msg': ''}
    return render(request, './myapp/depot_route_master_view.html', context)


from .models import route_stop_details
def depot_route_stop_details_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    if request.method == 'POST':
        user_id = request.session['user_id']
        dm = depot_master.objects.get(user_id=int(user_id))
        depot_id = dm.id
        route_id = int(request.POST.get('route_id'))
        stop_id = int(request.POST.get('stop_id'))
        stop_no = int(request.POST.get('stop_no'))
        stop_stage = int(request.POST.get('stop_stage'))
        status = 'new'

        pd = route_stop_details(route_id=route_id,stop_id=stop_id,
                                stop_no=stop_no,stop_stage=stop_stage)
        pd.save()
        hs_l = stop_master.objects.filter(depot_id=depot_id)
        context = {'stop_list':hs_l,'msg': 'Record Added','route_id':route_id}
        return render(request, './myapp/depot_route_stop_details_add.html', context)
    else:
        user_id = request.session['user_id']
        dm = depot_master.objects.get(user_id=int(user_id))
        depot_id = dm.id
        route_id = int(request.GET.get('route_id'))
        hs_l = stop_master.objects.filter(depot_id=depot_id)
        context = {'stop_list': hs_l, 'msg': '','route_id':route_id}
        return render(request, './myapp/depot_route_stop_details_add.html', context)


def depot_route_stop_details_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    route_id = request.GET.get('route_id')
    print('id = '+id)
    pd = route_stop_details.objects.get(id=int(id))
    pd.delete()
    msg = 'Route Stop Record Deleted'

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id

    pd_l = route_stop_details.objects.filter(route_id=int(route_id))
    hs_l = stop_master.objects.filter(depot_id=depot_id)
    context = {'route_stop_list': pd_l,'stop_list':hs_l,'msg':msg,'route_id':route_id}
    return render(request, './myapp/depot_route_stop_details_view.html',context)

def depot_route_stop_details_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id
    route_id = int(request.GET.get('route_id'))

    pd_l = route_stop_details.objects.filter(route_id=route_id)
    hs_l = stop_master.objects.filter(depot_id=depot_id)
    context = {'route_stop_list': pd_l, 'stop_list': hs_l, 'msg': '', 'route_id': route_id}
    return render(request, './myapp/depot_route_stop_details_view.html', context)

def depot_app_form_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id

    app_form_list = app_form.objects.filter(depot_id=depot_id,status='pending')
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()
    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list':app_form_list,'consession_list':consession_list,'student_list':student_list,
               'depot_list':depot_list,'route_stop_list':route_stop_list,'stop_list':stop_list,
               'institution_list':institution_list,'route_list':route_list}
    return render(request, './myapp/depot_app_form_view.html', context)

def depot_app_form_view1(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id

    stscode = 0

    app_form_list = app_form.objects.filter(depot_id=depot_id,status='approved')
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()
    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list':app_form_list,'consession_list':consession_list,'student_list':student_list,
               'depot_list':depot_list,'route_stop_list':route_stop_list,'stop_list':stop_list,
               'institution_list':institution_list,'route_list':route_list,'sc':stscode}
    return render(request, './myapp/depot_app_form_view.html', context)

def depot_app_form_view2(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id

    stscode = 1

    app_form_list = app_form.objects.filter(depot_id=depot_id,status='rejected')
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()
    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list':app_form_list,'consession_list':consession_list,'student_list':student_list,
               'depot_list':depot_list,'route_stop_list':route_stop_list,'stop_list':stop_list,
               'institution_list':institution_list,'route_list':route_list}
    return render(request, './myapp/depot_app_form_view.html', context)

def depot_app_form_update(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    id = request.GET.get('id')
    status = request.GET.get('status')
    ap = app_form.objects.get(id=int(id))
    cc = consession_details.objects.get(app_id=int(id))
    cc.status=status
    dtt = datetime.now()

    cc.c_number = str(dtt.microsecond)
    cc.save()
    ap.status=status
    ap.save()
    cc2 = consession_details_history(app_id=cc.app_id,c_number=cc.c_number,
                                     stage_rate=cc.stage_rate,dt=cc.dt,year=cc.year,
                                     month=cc.month,no_months=cc.no_months,status=cc.status)
    cc2.save()

    user_id = request.session['user_id']
    dm = depot_master.objects.get(user_id=int(user_id))
    depot_id = dm.id

    app_form_list = app_form.objects.filter(depot_id=depot_id, status='pending')
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()
    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list': app_form_list, 'consession_list': consession_list, 'student_list': student_list,
               'depot_list': depot_list, 'route_stop_list': route_stop_list, 'stop_list': stop_list,
               'institution_list': institution_list, 'route_list': route_list,'msg':status}
    return render(request, './myapp/depot_app_form_view.html', context)


def depot_depot_master_view(request):
    dp_l = depot_master.objects.all()
    context = {'depot_list':dp_l}
    return render(request, './myapp/depot_depot_master_view.html', context)


###################################################################
############### Institution ########################
from .models import institution_master
def institution_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='institution')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            ins = institution_master.objects.get(user_id=ul[0].id)
            context = {'uname':ins.name }
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/institution_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/institution_login.html',context)
    else:
        return render(request, 'myapp/institution_login.html')

def institution_home(request):
    ins = institution_master.objects.get(user_id=int(request.session['user_id']))
    context = {'uname': ins.name}
    # context = {'uname':request.session['user_name']}
    return render(request,'./myapp/institution_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def institution_details_add(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        adrs1 = request.POST.get('adrs1')

        adrs2 = request.POST.get('adrs2')
        ph = request.POST.get('ph')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        affili = request.POST.get('affili')
        govtpvt = request.POST.get('govtpvt')
        princi_name = request.POST.get('princi_name')
        princi_ph = request.POST.get('princi_ph')
        i_type = request.POST.get('i_type')

        password = request.POST.get('pwd')
        uname=email
        status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='institution')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        im = institution_master(name=name,adrs1=adrs1,adrs2=adrs2,pin=pin,
                                ph=ph,email=email,affili=affili,govtpvt=govtpvt,
                                princi_name=princi_name,princi_ph=princi_ph,
                                i_type=i_type,user_id=user_id,status=status)
        im.save()

        print(user_id)
        context = {'msg': 'Institution Registered'}
        return render(request, 'myapp/institution_login.html',context)

    else:
        return render(request, 'myapp/institution_details_add.html')

def institution_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password,u_type='institution')

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/institution_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/institution_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/institution_changepassword.html', context)
    else:
        return render(request, './myapp/institution_changepassword.html')



def institution_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return institution_login_check(request)
    else:
        return institution_login_check(request)

def institution_depot_master_search(request):

    if request.method == 'POST':
        query = request.POST.get('query')
        pd_l = depot_master.objects.filter(dpname__contains=query)

        context = {'depot_list': pd_l}
        return render(request, './myapp/institution_depot_master_view.html', context)
    else:
        return render(request, 'myapp/institution_depot_master_search.html')

def institution_depot_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    pd_l = depot_master.objects.all()
    context = {'depot_list':pd_l}
    return render(request, './myapp/institution_depot_master_view.html',context)

def institution_route_master_search(request):

    if request.method == 'POST':
        query = request.POST.get('query')
        pd_l = route_master.objects.filter(route_name__contains=query)
        hs_l = bus_type_master.objects.all()
        dm_l = depot_master.objects.all()

        context = {'route_list': pd_l, 'depot_list': dm_l, 'bus_list': hs_l, 'msg': ''}
        return render(request, './myapp/institution_route_master_view.html', context)
    else:
        return render(request, 'myapp/institution_route_master_search.html')

def institution_route_master_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return institution_login_check(request)

    user_id = request.session['user_id']

    depot_id = request.GET.get('depot_id')
    pd_l = route_master.objects.filter(depot_id=depot_id)
    hs_l = bus_type_master.objects.all()
    dm_l = depot_master.objects.all()

    context = {'route_list': pd_l,'depot_list': dm_l, 'bus_list': hs_l, 'msg': ''}
    return render(request, './myapp/institution_route_master_view.html', context)

def institution_route_stop_details_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return institution_login_check(request)


    depot_id = request.GET.get('depot_id')
    route_id = int(request.GET.get('route_id'))

    pd_l = route_stop_details.objects.filter(route_id=route_id)
    hs_l = stop_master.objects.filter(depot_id=depot_id)
    context = {'depot_id':depot_id,'route_stop_list': pd_l, 'stop_list': hs_l, 'msg': '', 'route_id': route_id}
    return render(request, './myapp/institution_route_stop_details_view.html', context)


from .models import student_details
from datetime import datetime

def institution_student_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        addr1 = request.POST.get('addr1')
        street = request.POST.get('street')
        place = request.POST.get('place')
        dist = request.POST.get('dist')

        pin = request.POST.get('pin')
        father_name = request.POST.get('father_name')
        mothername = request.POST.get('mothername')
        g_contact = request.POST.get('g_contact')
        p_contact = request.POST.get('p_contact')
        course = request.POST.get('course')
        year = request.POST.get('year')
        pic='none'
        status = "new"
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        user_id = int(request.session['user_id'])
        im = institution_master.objects.get(user_id=user_id)
        ud = student_details(fname=fname,lname=lname,dob=dob,gender=gender,addr1=addr1,street=street,
                             place=place,dist=dist,pin=pin,father_name=father_name,mothername=mothername,
                             g_contact=g_contact,p_contact=p_contact,course=course,year=year,pic=pic,
                             status=status,dt=dt,tm=tm,institution_id=im.id)
        ud.save()

        #print(user_id)
        context = {'msg': 'Student Registered'}
        return render(request, 'myapp/institution_student_details_add.html',context)

    else:
        return render(request, 'myapp/institution_student_details_add.html')


def institution_student_details_search(request):

    if request.method == 'POST':
        query = request.POST.get('query')
        user_id = int(request.session['user_id'])
        im = institution_master.objects.get(user_id=user_id)
        institution_id = im.id
        pd_l = student_details.objects.filter(institution_id=institution_id,fname__contains=query)
        hs_l = institution_master.objects.all()

        context = {'student_list': pd_l, 'institution_list': hs_l, 'msg': ''}
        return render(request, './myapp/institution_student_details_view.html', context)
    else:
        return render(request, 'myapp/institution_student_details_search.html')

def institution_student_details_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return institution_login_check(request)

    user_id = int(request.session['user_id'])
    im = institution_master.objects.get(user_id=user_id)
    institution_id = im.id

    pd_l = student_details.objects.filter(institution_id=institution_id)
    hs_l = institution_master.objects.all()

    context = {'student_list': pd_l, 'institution_list': hs_l, 'msg': ''}
    return render(request, './myapp/institution_student_details_view.html', context)


def institution_student_details_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return institution_login_check(request)
    id = request.GET.get('id')
    sd = student_details.objects.get(id=int(id))
    sd.delete()

    user_id = int(request.session['user_id'])
    im = institution_master.objects.get(user_id=user_id)
    institution_id = im.id

    pd_l = student_details.objects.filter(institution_id=institution_id)
    hs_l = institution_master.objects.all()

    context = {'student_list': pd_l, 'institution_list': hs_l, 'msg': 'Student Deleted'}
    return render(request, './myapp/institution_student_details_view.html', context)


from .models import app_form,consession_details,consession_details_history
from .models import route_stop_details
def institution_app_form_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return institution_login_check(request)

    if request.method == 'POST':
        user_id = int(request.session['user_id'])
        im = institution_master.objects.get(user_id=user_id)
        institution_id = im.id
        route_id = int(request.POST.get('route_id'))
        rm = route_master.objects.get(id=route_id)
        depot_id = rm.depot_id

        student_id = int(request.POST.get('student_id'))

        src = request.POST.get('src')
        dest = request.POST.get('dest')

        if src != dest:

            #tm = datetime.today().strftime('%H:%M:%S')
            ap_dte = datetime.today().strftime('%Y-%m-%d')

            dt = datetime.today().strftime('%Y-%m-%d')
            year = int(datetime.today().strftime('%Y'))
            month = int(datetime.today().strftime('%m'))


            no_months = int(request.POST.get('no_months'))
            c_number  = '0'

            rsd1 = route_stop_details.objects.get(id=int(src))
            stop_stage1 = rsd1.stop_stage
            stopm1 = stop_master.objects.get(id =rsd1.stop_id)
            src1 = stopm1.stop_name

            rsd2 = route_stop_details.objects.get(id=int(dest))
            stop_stage2 = rsd2.stop_stage
            stopm2 = stop_master.objects.get(id=rsd2.stop_id)
            dest1 = stopm2.stop_name

            stop_stage = abs(stop_stage1-stop_stage2)
            if stop_stage == 0:
                stop_stage =1
            ratem = rate_master.objects.get(bus_type_id=rm.bus_type_id,stage=stop_stage)
            stage_rate = ratem.month_fare
            status = 'pending'

            pd = app_form(ap_dte=ap_dte,student_id=student_id,institution_id=institution_id,
                        depot_id=depot_id,route_id=route_id,src=src1,dest=dest1,status=status)
            pd.save()
            app_id = app_form.objects.all().aggregate(Max('id'))['id__max']
            pd = consession_details(app_id=app_id,c_number=c_number,stage_rate=stage_rate,dt=dt,
                                    year=year,month=month,no_months=no_months,status=status)
            pd.save()

            pd_l = student_details.objects.filter(institution_id=institution_id)
            hs_l = stop_master.objects.filter(depot_id=depot_id)
            rs_l = route_stop_details.objects.filter(route_id=route_id)

            context = {'stop_list':hs_l,'route_stop_list':rs_l,'student_list':pd_l,'msg': 'Record Added','route_id':route_id}
            return render(request, './myapp/institution_app_form_add.html', context)
        else:
            return render(request, './myapp/institution_app_form_add.html')
    else:
        user_id = int(request.session['user_id'])
        im = institution_master.objects.get(user_id=user_id)
        institution_id = im.id
        route_id = int(request.GET.get('route_id'))
        rm = route_master.objects.get(id=route_id)
        depot_id = rm.depot_id
        pd_l = student_details.objects.filter(institution_id=institution_id)
        hs_l = stop_master.objects.filter(depot_id=depot_id)
        rs_l = route_stop_details.objects.filter(route_id=route_id)

        context = {'stop_list': hs_l, 'route_stop_list': rs_l, 'student_list': pd_l, 'msg': '',
                   'route_id': route_id}
        return render(request, './myapp/institution_app_form_add.html', context)



def institution_app_form_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    user_id = int(request.session['user_id'])
    im = institution_master.objects.get(user_id=user_id)
    institution_id = im.id

    print("Inst ID: ",institution_id)

    app_form_list = app_form.objects.filter(institution_id=institution_id)
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()
    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list':app_form_list,'consession_list':consession_list,'student_list':student_list,
               'depot_list':depot_list,'route_stop_list':route_stop_list,'stop_list':stop_list,
               'institution_list':institution_list,'route_list':route_list}
    return render(request, './myapp/institution_app_form_view.html', context)

def institution_app_form_view2(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    user_id = int(request.session['user_id'])
    im = institution_master.objects.get(user_id=user_id)
    institution_id = im.id
    student_id = int(request.GET.get('student_id'))
    app_form_list = app_form.objects.filter(institution_id=institution_id,student_id=student_id)
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()
    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list':app_form_list,'consession_list':consession_list,'student_list':student_list,
               'depot_list':depot_list,'route_stop_list':route_stop_list,'stop_list':stop_list,
               'institution_list':institution_list,'route_list':route_list}
    return render(request, './myapp/institution_app_form_view.html', context)

def institution_app_form_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    id = request.GET.get('id')
    ap = app_form.objects.get(id=int(id))
    cc = consession_details.objects.get(app_id=int(id))
    cc.delete()
    ap.delete()

    user_id = int(request.session['user_id'])
    im = institution_master.objects.get(user_id=user_id)
    institution_id = im.id

    app_form_list = app_form.objects.filter(institution_id=institution_id)
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()

    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list':app_form_list,'consession_list':consession_list,'student_list':student_list,
               'depot_list':depot_list,'route_stop_list':route_stop_list,'stop_list':stop_list,
               'institution_list':institution_list,'route_list':route_list,'msg':'Request Deleted'}
    return render(request, './myapp/institution_app_form_view.html', context)


def institution_app_form_update(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return depot_login(request)

    id = request.GET.get('id')
    dt = datetime.today().strftime('%Y-%m-%d')
    year = int(datetime.today().strftime('%Y'))
    month = int(datetime.today().strftime('%m'))


    ap = app_form.objects.get(id=int(id))
    cc = consession_details.objects.get(app_id=int(id))
    cc.dt = dt
    cc.year =year
    cc.month = month
    cc.save()
    cc2 = consession_details_history(app_id=cc.app_id, c_number=cc.c_number,
                                     stage_rate=cc.stage_rate, dt=cc.dt, year=cc.year,
                                     month=cc.month, no_months=cc.no_months, status=cc.status)
    cc2.save()

    user_id = int(request.session['user_id'])
    im = institution_master.objects.get(user_id=user_id)
    institution_id = im.id

    app_form_list = app_form.objects.filter(institution_id=institution_id)
    institution_list = institution_master.objects.all()
    consession_list = consession_details.objects.all()
    student_list = student_details.objects.all()
    depot_list = depot_master.objects.all()
    route_stop_list = route_stop_details.objects.all()
    stop_list = stop_master.objects.all()
    route_list = route_master.objects.all()
    context = {'app_form_list': app_form_list, 'consession_list': consession_list, 'student_list': student_list,
               'depot_list': depot_list, 'route_stop_list': route_stop_list, 'stop_list': stop_list,
               'institution_list': institution_list, 'route_list': route_list, 'msg': 'Renewed'}
    return render(request, './myapp/institution_app_form_view.html', context)


##################################################################
################## USER ####################################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)



