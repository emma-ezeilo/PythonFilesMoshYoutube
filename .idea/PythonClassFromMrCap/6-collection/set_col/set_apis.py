set_py_lib = set()
set_py_lib.add('Nunpy')
set_py_lib.add('Panda')
set_py_lib.add('Seaborn')
set_py_lib.add('MathPlotLib')
set_py_lib.add('Keras')
set_py_lib.add('Django')

set_py_lib.add('Flask')
set_py_lib.add('Pillow')

set_py_lib.update(('Faker','PrettyTable'))
set_py_lib.remove('Pillow')  ##Remove shows error if element is not in the set
set_py_lib.discard('Keras') ## Discard does not show errors when element is not in the set

# set_py_lib.clear()
my_new_lib = set_py_lib.copy()
print(my_new_lib)

# print(set_py_lib)

# for py_lib in set_py_lib:     ###Looping in set
#     print(py_lib)