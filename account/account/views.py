from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Account
from .forms import AccountForm

@csrf_exempt
def create_account(request):
	result = {
		"success": True,
		"reason": ""
	}
	username = request.POST.get("username")
	password = request.POST.get("password")
	account_form = AccountForm(request.POST)
	print(AccountForm(request.POST).is_valid())
	if account_form.is_valid():
		account_form.save()
		return JsonResponse(result, status=201)
	else:
		reason_list = []
		for e in account_form.errors.items():
			reason_list.extend(e[1])
		result["success"] = False
		result["reason"] = " ".join(reason_list)

	return JsonResponse(result, status=400)