num = raw_input().rstrip()
digits = []
for k in num:
	if k.isdigit():
		digits.append(k)
print("".join(digits))
