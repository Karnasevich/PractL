class A:
 def s(self): raise NotImplementedError

class B(A):
 def s(self): return "Гав-гав"

class C(A):
 def s(self): return "Мяу-мяу"

class D(A):
 def s(self): return "Чирик-чирик"

def f(x): 
 for i in x: print(i.s())

z=[B(),C(),D(),B()]
f(z)
