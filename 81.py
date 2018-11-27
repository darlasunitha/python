def do_stuff(input):
	m,n = [int(x) for x in input.split(" ")]
	print(n-m)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached
