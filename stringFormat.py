first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

print("My age is {} and my name is {} {}.".format(age, first_name, last_name))


hw = "Hello %s" % "World"
py = "I love Python %d" % 3
print(hw, py)

name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# print("My name is %s and I'm %d" % (age, name))		# or with variables
# output: My name is Zen and I'm 27

x = "hello world"
print(x.title())