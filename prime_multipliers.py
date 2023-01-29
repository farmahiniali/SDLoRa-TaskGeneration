# in this module we make a matrix of prime multipliers so that meet our constraints such as max period and
# max acceptable prime multipliers
# initial matrix can have below number and levels
# 1, 2,
# 1, 3
# 1, 5
# 1, 7
# 1, 11, 121
# 1, 13, 169
# 1, 17, 289
# 1, 19

import time
from operator import ne


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def primeFactors(n):
    multipliers = []
    powers = []
    if is_prime(n):
        multipliers.append(n)
        powers.append(1)
    else:
        rang = int(n / 2)
        tmp_n = n
        for i in range(rang + 1):
            if tmp_n == 1:
                break
            if not is_prime(i):
                continue
            else:
                counter = 0
                while tmp_n % i == 0 and tmp_n != 1:
                    counter += 1
                    tmp_n /= i
                if counter > 0:
                    multipliers.append(i)
                    powers.append(counter)
    return multipliers, powers




# N = input("enter a no: ")
# (mult, powr) = primeFactors(int(N))
# print("Number is : ")
# for i in range(len(mult)):
#     print(mult[i], "^", powr[i], " * ", end="")


# ---------- make prime matrix ----------------------------------------


def make_prime_matrix(matrix_bound):
    mat = []
    base_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for i in range(450001, matrix_bound + 1, 1):
        (mult, powr) = primeFactors(i)
        break_flag = False
        for j in mult:
            if j not in base_primes:
                break_flag = True
                break
        if break_flag == False:
            mat.append(i)
    return mat


# --------- choose nearest number -------------------------------


# def nearest_number(number, matrix):
#     sorted_matrix = matrix.copy()
#     i = 0
#     while number > sorted_matrix[i]:
#         i += 1
#     if (number - sorted_matrix[i - 1]) <= (sorted_matrix[i] - number):
#         return sorted_matrix[i - 1]
#     else:
#         return sorted_matrix[i]


def nearest_num (number, matrix):
    if (number > matrix[len(matrix)-1]):
        return matrix[len(matrix)-1]
    elif number < matrix[0]:
        return matrix[0]
    elif matrix[0] < number < matrix[1]:
        if abs(matrix[0] - number) < abs(matrix[1] - number):
            return matrix[0]
        else:
            return matrix[1]
    mid = len(matrix) // 2
    if number == matrix[mid]:
        return matrix[mid]
    if number < matrix[mid]:
        return nearest_num(number, matrix[:mid])
    elif number > matrix[mid]:
        return nearest_num(number, matrix[mid :])

# matrix = [5, 7, 9, 11, 15, 19, 23, 25, 35]   
# print(nearest_num(19,matrix))

if __name__ == "__main__":
    print(time.asctime())
    mat1 = make_prime_matrix(500000)
    #out for matrix 
    out = ""
    for x in mat1: 
        out += str(x) + ","
    out = out [:len(out)-1]
    of = open("prime_mat_500-000.txt", "w")
    of.writelines(out)
    of.close()
    of = open("prime_mat_500-000.txt", "r")
    mat = str(of.readlines()).strip("[").strip("]").strip("\'")
    mat = mat.split(",")
    mat2 = [int(x) for x in mat] 
    print (mat2)
    print(time.asctime())

