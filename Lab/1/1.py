num_input = input("Enter a number: ")
num_var = num_input
float_num = float(num_var)
string_num = str(num_var)
complex_num = complex(float_num)
print(type(float_num))
print(type(string_num))
print(type(complex_num))
if (int(float_num) // 2) * 2 == int(float_num):
    print("YES Divisible by 2")
else:
    print("Not divisible by 2")