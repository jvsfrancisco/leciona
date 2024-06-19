from leciona import *

# TODO converter pra unit tests

print(add_leciona(1, 2))
print(get_prof_by_turma(2))
print(get_prof_by_turma(-1))

add_leciona(1, 3)
add_leciona(2, 1)
print(get_turmas_by_prof(1))

print(add_leciona(1, 2))

set_leciona(2, 2)
print(get_prof_by_turma(2))

print(set_leciona(1, -1))
