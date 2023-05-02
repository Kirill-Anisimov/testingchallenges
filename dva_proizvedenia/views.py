from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, "home.html")

def proizvedenie(request):
	k = 1

	val_1 = int(request.GET["num1"])
	val_2 = int(request.GET["num2"])

	proizv_1 = val_1 * val_2
	proizv_2 = (val_1 - k) * (val_2 + k)

	result = {
		"results_list": [
			{"path": "uspeh", "value": proizv_1},
			{"path": "neudacha", "value": proizv_2}
		]
	}

	return render(request, "result.html", result)

def uspeh(request):
	return render(request, "uspeh.html")

def neudacha(request):
	return render(request, "neudacha.html")
