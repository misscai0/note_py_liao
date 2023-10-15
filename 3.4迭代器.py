#可迭代对象(Iterable)：可以直接作用于for循环的对象
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function
# 可以使用isinstance()判断一个对象是否是Iterable对象
from collections.abc import Iterable
isinstance([], Iterable)
isinstance('iii', Iterable)
isinstance(67.998, Iterable)

#迭代器(Iterator):可以被next()函数调用并不断返回下一个值的对象
# 可以使用isinstance()判断一个对象是否是Iterator对象
from collections.abc import Iterator
isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)
isinstance(iter('abc'), Iterator)

