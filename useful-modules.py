from collections import Counter, defaultdict
from array import array
import datetime

li = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8]
print(Counter(li))

sentence = "I likes to keep it real"
print(Counter(sentence))

dictionary = defaultdict(lambda: 7, {"a": 1, "b": 10})
print(dictionary["c"])  # 7

print(datetime.time())
print(datetime.date.today())

arr = array(
    "i", [10, 20, 30]
)  # by giving it a type - i, we are helping with better memory allocation

print(arr[1])
