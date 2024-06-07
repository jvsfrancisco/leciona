# Como utilizar

No diretório imediatamente acima do seu módulo, execute:

`git clone https://github.com/jvsfrancisco/leciona`

Depois você pode utilizar as funções de turma com o import:

```Python
from .. import leciona

turma.get_prof_by_turma(1)
```

**OBS:** Para utilizar imports relativos, seu módulo também precisa fazer parte de um package, ou seja, o diretório do módulo deve possuir um arquivo `__init__.py` assim como o nosso.

Alternativamente, se o diretório acima do seu módulo também for um repositório, como o principal, você pode adicionar turma como submódulo:

`git submodule add https://github.com/jvsfrancisco/leciona`

## Dependências

Python 3.9+
