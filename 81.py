def do_stuff(input):
	p,q = [int(y) for y in input.split(" ")]
	print(q-p)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached
