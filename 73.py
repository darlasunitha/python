p = int(raw_input())
l, g = [int(k) for k in raw_input().split(" ")]
print("yes" if (p > l and p < g) else "no")
