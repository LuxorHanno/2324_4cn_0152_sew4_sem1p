__author__ = "Hanno Postl"
__version__ = "1.0"
__status__ = "Finished"

from rekursiv import M
from time import time

t0 = time()
m_list = [M(n) for n in range(1, 201)]

t1 = time()

m_dict = {n: M(n) for n in range(1, 201)}
t2 = time()

print(m_list)
print(len(m_list))
print(m_dict)
print(len(m_dict))
print(f"Liste: {t1 - t0} Dict: {t2 - t1}")

#Es stellt sich heraus das Dictionaries länger Brauchen als Listen.
#In meinem Fall braucht die Liste 0.000997304916381836 Sekunden und das Dictionary 0.001994609832763672 Sekunden.