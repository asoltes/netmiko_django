from django.shortcuts import render
from .forms import CmdForm
# Create your views here.

def index(request):
    if request.method == "POST":
        form = CmdForm(request.POST)
        if form.is_valid():
            from netmiko import ConnectHandler
            device = {}
            device['device_type'] = 'cisco_ios'
            device['ip'] = '172.16.0.251'
            device['username'] = 'asoltes'
            device['password'] = 'bsit113092'
            cmd = request.POST.get('command', '')
            conn = ConnectHandler(**device)
            output = conn.send_command(cmd)
            return render(request, 'netinfo/index.html', {'output': output})
    else:
        form = CmdForm()
        return render(request, 'netinfo/index.html', {'form' : form})
