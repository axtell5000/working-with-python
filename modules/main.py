import random
import pyjokes

from utils import multiply, divide


if __name__ == '__main__':
  print(multiply(5, 2))
  print(divide(10, 2))
  print(random)


print(random.random())
print(random.randint(1,20))
print(random.choice(['a', 'b','c','d']))

joke = pyjokes.get_joke('en', 'neutral')
print(joke)
