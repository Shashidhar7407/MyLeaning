# #import numpy as np
# # arr=np.array((1,2,3,4,5))
# # print(arr)
# # print(type(arr))
# import numpy as np
# #arr=np.array([1,2,3,4],[5,4,3,1])
# a = np.array(42)
# b = np.array([[[1, 2, 3, 4, 5],[1,2,3,4,5],[9,8,7,6,5]]])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
import numpy as np
arr=np.array([1,2,3,4],ndmin=6)
print(arr)