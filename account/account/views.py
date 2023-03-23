from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from .forms import AccountForm


@csrf_exempt
def create_account(request):
	'''
	Create Account
	username: minimum length of 3 characters and maximum length of 32 characters
	password: 1. minimum length of 3 characters and maximum length of 32 characters
			  2. contains at least 1 uppercase letter, 1 lowercase letter, and 1 number
	'''
	result = {
		"success": True,
		"reason": ""
	}
	if request.method == "GET":
		result["success"] = False
		result["reason"] = "Method Not Allowed"
		return JsonResponse(result, status=405)
	else:
		account_form = AccountForm(request.POST)
		if account_form.is_valid():
			account = account_form.save(commit=False)
			encrypted_password = make_password(account.password)
			account.password = encrypted_password
			account.save()
			return JsonResponse(result, status=201)
		else:
			reason_list = []
			for e in account_form.errors.items():
				reason_list.extend(e[1])
			result["success"] = False
			result["reason"] = " ".join(reason_list)
		return JsonResponse(result, status=400)

@csrf_exempt
def verify_account(request):
	'''
	Verify Account
	If the password verification fails five times, 
	the user should wait one minute before attempting to verify the password again.
	'''
	result = {"success": False, "reason": ""}
	if request.method == "GET":
		result["success"] = False
		result["reason"] = "Method Not Allowed"
		return JsonResponse(result, status=405)
	else:
		input_username = request.POST.get("username")
		input_password = request.POST.get("password")
		failed_attempts = cache.get(input_username, 0)
		if failed_attempts >= 5:
			last_attempt_time = cache.get(f"{input_username}:last_attempt_time", None)
			if last_attempt_time is not None and (datetime.now() - last_attempt_time).seconds < 60:
				result["reason"] = "Too many attempts. Try again later."
				return JsonResponse(result, status=403)
			else:
				cache.set(input_username, 0, 60)
				cache.set(f"{input_username}:last_attempt_time", datetime.now(), 60)
		try:
			account = Account.objects.get(username=input_username)
		except Account.DoesNotExist:
			result["reason"] = f"User: {input_username} does not exist."
			return JsonResponse(result, status=404)

		if check_password(input_password, account.password):
			result["success"] = True
			result["reason"] = ""
			return JsonResponse(result, status=200)
		else:
			result["reason"] = "Password is incorrect."
			cache.set(input_username, failed_attempts + 1, 60)
			cache.set(f"{input_username}:last_attempt_time", datetime.now(), 60)
			return JsonResponse(result, status=403)