def do_stuff(input):
	a, op, b = [a for a in input.split(" ")]
	if op == '/':
		print(int(a) / int(b))
	else:
		print(int(a) % int(b))
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached
