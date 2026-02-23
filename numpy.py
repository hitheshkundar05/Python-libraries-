import numpy as np
print("===test case1:3X3 array creation and reshaping===")
marks=np.array([
    [70,80,90],
    [85,78,90],
    [60,88,72],
])
print("original 3x3 matrix:\n",marks)
reshaped=marks.reshape(1,9)
print("\n reshaped to(1,9):\n",reshaped)
print("\n===Test case2:element-wise multiplication===")
arr1=np.array([2,4,6])
arr2=np.array([3,5,7])
result=arr1*arrr2
print("array 1:",arr1)
print("array 2:",arr2)
print("element-wise multipication:",result)
print("\n===application task:Teacher assessment processing===")
marks[:,1]*=2
print("after bonus(subject 2 doubled):\n",marks)
print("\nsingle row report format:\n",report_format)
print("\ntotal marks per sutudent:\n",total_marks)