def my_func():
 print("Hello World")
 return my_func
 a = my_func()
 print(a)

my_func()

def add(a,b):
 c = a+b
 return c
result = add(5,4)
print(result)

def add_sub(a,b):
  c = a+b
  d = a-b

  return c,d

result1,result2 = add_sub(5,4)

print(result1,result2)