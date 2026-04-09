import numpy as np

# 리스트로 생성 : np.array([1,2,3])
# 연속 값 생성 : np.arange(0, 10, 2)
# 특수 배열 :
#
#
#
# 난수 생성 :

import numpy as np

l1= [1, 2, 3]
array01 = np.array(l1)
print(l1)
print(array01)

array02 = np.arange(10,0,-2)
print(array02)

array03 = np.zeros((2,3))
print(array03)

array04 = np.ones((2,3))
print(array04)

array05 = np.full((2, 3), -1)
print(array05)

array06 = np.random.randn(2, 3)
print(array06)

array07 = np.linspace(0,10,3)
print(array07)