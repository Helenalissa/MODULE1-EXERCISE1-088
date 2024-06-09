# Câu 1 
import math

def calc_f1_score(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score
assert round ( calc_f1_score ( tp =2 , fp =3 , fn =5) , 2) == 0.33
print ( round ( calc_f1_score ( tp =2 , fp =4 , fn =5) , 2) )
# Đáp án: C


# Câu 2
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
assert is_number (3) == 1.0
assert is_number ('-2a') == 0.0
print ( is_number (1) )
print ( is_number ('n') ) 
# Đáp án: B

# Câu 3: Đáp án C: ReLu

# Câu 4:

def calc_sig(x):
    return 1/ (1 + math.exp(-x))
assert round(calc_sig(3),2)==0.95
print(round(calc_sig(2),2))
# Đáp án: A: 0,88

#Câu 5

def calc_elu(x):
    alpha = 0.01
    if x <= 0.01:
        return alpha * (math.exp(x)-1)
    else:
        return x

assert round(calc_elu(1)) ==1
print(round(calc_elu(-1),2))
# Đáp án B: -0.01

# Câu 6:

def calc_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1/ (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0,x)
    elif act_name == 'elu':
        alpha = 0.01
        if x <= 0:
            return alpha * (math.exp(x)-1)
        else:
            return x
assert calc_activation_func ( x = 1 , act_name ='relu') == 1
print ( round ( calc_activation_func (x = 3 , act_name = 'sigmoid') , 2) )
# Đáp án: A 0.95

# Câu 7:

def calc_ae(y, y_hat):
    return abs(y - y_hat)
y = 1
y_hat = 6
assert calc_ae (y , y_hat ) == 5
y = 2
y_hat = 9
print( calc_ae (y , y_hat ) )
# Đáp án: A 7

#Câu 8

def calc_ae2(y, y_hat):
    return abs(y - y_hat) **2
y = 4
y_hat = 2
assert calc_ae2(y , y_hat ) == 4
print( calc_ae2(2 , 1) )
#Đáp án: A: 1

#Câu 9

def approx_cos(x, n):
    cos_x = 1.0
    for i in range(1, n+1):
        sign = (-1) ** i
        cos_x += sign * (x ** (2*i)) / math.factorial(2*i)
    return cos_x
assert round ( approx_cos ( x =1 , n =10) , 2) ==0.54
print( round ( approx_cos ( x =3.14 , n =10) , 2) )
# Đáp án: C -1.0

#Câu 10

def approx_sin(x, n):
    sin_x = 0
    for i in range(n+1):
        sign = (-1) ** i
        sin_x += sign * (x ** (2*i + 1)) / math.factorial(2*i + 1)
    return sin_x
assert round ( approx_sin ( x =1 , n =10) , 4) ==0.8415
print ( round ( approx_sin ( x =3.14 , n =10) , 4) )
#Đáp án: A: 0.0016

#Câu 11

def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n+1):
        sinh_x += (x ** (2*i + 1)) / math.factorial(2*i + 1)
    return sinh_x
assert round ( approx_sinh ( x =1 , n =10) , 2) ==1.18
print ( round ( approx_sinh ( x =3.14 , n =10) , 2) )
# Đáp án: 11.53

#Câu 12

def approx_cosh(x,n):
    cosh_x = 0
    for i in range(n+1):
        cosh_x += (x ** (2*i))/math.factorial(2*i)
    return cosh_x
assert round ( approx_cosh ( x =1 , n =10) , 2) ==1.54
print ( round ( approx_cosh ( x =3.14 , n =10) , 2) )
# Đáp án: 11.57

#Câu 13: C

