import numpy as np 
np.random.seed(0)
# mat = np.random.randint(10,100,(5,5))
# print(mat)

# mean_Col = np.mean(mat,axis=0)
# mean_row = np.mean(mat, axis=1)

# mat_5 = mat > 50
# mat50 = mat[mat_5]
# print("\n", mat_5)
# print("\n" ,mat50)

# x =np.random.choice([5, 2, 7], p=[0.4, 0.6, 0.0], size=(100))
# print(x)

student =np.array(["Hi", "Hello", "Morning", "Night", "Bad"])
Sub = np.array(["Math" , "Eng", "Soc" , "Lang"])
Mark = np.random.randint(40,100,(5,4))

StudC = student.reshape(5,1)

Stud_Mark = np.concatenate((StudC , Mark), axis = 1)

mean_mark = np.mean(Mark, axis= 1)
print(mean_mark)

Top = np.argmax(mean_mark)

top_student = Stud_Mark[Top]

fail = np.any(Mark < 70, axis = 1)
failed = Mark[fail]

