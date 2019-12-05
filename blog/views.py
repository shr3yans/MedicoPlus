from django.shortcuts import render
import mysql.connector

mydb = mysql.connector.Connect(host="127.0.0.1", user="root", password="Ab5524%@%", database="medico_plus",
                               auth_plugin='mysql_native_password', buffered=True)
mydbc = mydb.cursor()


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def fd(request):
    mydbc.execute(
        'select d_id,d_name, dpt_name, start_time, end_time from doctor, department, doctor_availability where '
        'd_dpt_id = dpt_id and doctor_id = d_id;')
    z = mydbc.fetchall()
    return render(request, 'find_doctor.html', {'doct': z})

def ba(request):
    val = request.POST.get('d_id3')
    mydbc.execute(
        'select username, email, d_name, start_time from auth_user, doctor, doctor_availability where is_active=1 '
        'and d_id=%s and  doctor_id = d_id;',
        (val,))
    z = mydbc.fetchall()
    return render(request, 'my_bookings.html', {'doct': z})


def mb(request):
    mydbc.execute(
        'select username, email, d_name, start_time from auth_user, doctor, doctor_availability where  d_id=%s and '
        'd_id = doctor_id;',
        (val,))
    z = mydbc.fetchall()
    return render(request, 'my_bookings.html', {'doct': z})


def mp(request):
    return render(request, 'blog/post_list.html', {})

def alll(request):
    mydbc.execute('select username, email, d_name, dpt_name, start_time from auth_user, doctor, department, doctor_availability, u_input where u_name=username and doctor_id = d_id and docid=d_id;')
    z = mydbc.fetchall()
    return render(request, 'blog/templates/blog/appointments.html', {'doct': z})