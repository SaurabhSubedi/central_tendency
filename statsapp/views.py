from django.shortcuts import render
from statistics import mean,median,mode
from .models import Datum
# Create your views here.
def calculator(request):
    if request.method == "POST":
        Mean = 0
        Median = 0
        Mode = 0
        data = request.POST.get("data")
        option = request.POST.get("option")
        string_to_list = list(data)
        string_to_list = set(string_to_list)
        string_to_list.remove(",")
        num_array = []
        for item in string_to_list:
            item = int(item)
            num_array.append(item)
        length = len(num_array)
        if option == "mean":
            Mean = mean(num_array)

        elif option == "median":
            Median = median(num_array)

        else:
            Mode = mode(num_array)

        context = {
            'length': length,
            'Mean': Mean,
            'Median': Median,
            'Mode': Mode,
        }
        object = Datum(num_of_items = length,mean = Mean, median = Median, mode = Mode)
        object.save()
        return render(request,'result.html',context)





    return render(request,'index.html')