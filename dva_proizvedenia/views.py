from django.shortcuts import render


def home(request):
	return render(request, "home.html")


def proizvedenie(request):
	val_1 = float(request.GET["num1"])
	val_2 = float(request.GET["num2"])

	# Если число А = 0, то сделать коэффициент К = 2
	k = 2 if val_1 == 0 else 1

	# Допустимые значения от -1000 до 1000 включительно
	if abs(val_1) > 1000 or abs(val_2) > 1000:
		return render(request, "404.html")
	else:
		# Невозможно ввести более 2 символов после запятой
		if len(str(val_1).split(".")[1]) > 2 or len(str(val_2).split(".")[1]) > 2:
			return render(request, "404.html")
		else:
			# Если одно из чисел = 999 сделать некорректный расчет:
			# вместо А*Б и (А-К)*(Б+К) сделать (А*Б)+1 и ((А-К)*(Б+К))+1
			if val_1 == 999 or val_2 == 999:
				proizv_1 = (val_1 * val_2) + 1
				proizv_2 = ((val_1 - k) * (val_2 + k)) + 1
			else:
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
	try:
		user_agent = request.META["HTTP_SEC_CH_UA"]
		# Когда пользователь выбирает неправильное произведение
		# Во всех браузерах кроме Google Chrome будет ошибка 404
		if "Google Chrome" in user_agent:
			return render(request, "neudacha_chrome.html")
		else:
			return render(request, "404.html")
	except KeyError:
		return render(request, "404.html")
