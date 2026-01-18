# https://usaco.org/index.php?page=viewproblem2&cpid=855

c = [0, 0, 0]
m = [0, 0, 0]
with open("mixmilk.in") as read:
	for i in range(3):
		c[i], m[i] = map(int, read.readline().split())            

for i in range(100):
    test = i%3
    test2 = test + 1
    if (test2 == 3):
        test2 = 0

    if (m[test] + m[test2] <= c[test2]):
        m[test2] += m[test]
        m[test] = 0
    else:
        m[test] = m[test] + m[test2] - c[test2]
        m[test2] = c[test2]

with open("mixmilk.out", "w") as out:
	for mm in m:
		print(mm, file=out)
