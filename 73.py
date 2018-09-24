m = int(raw_input())
l, r = [int(x) for x in raw_input().split(" ")]
print("yes" if (m > l and m < r) else "no")
