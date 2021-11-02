# Password

## Casos de uso:
### Criar uma senha 
* Argumentos => (new), (nome), opcional(senha);
1. Checar a existência do arquivo;
1. Checar todas as senhas;
1. Verificar se a senha já existe. Se a senha não existir, criar;
1. Se a senha existir, avisar e jogar na área de transferência.
1. Checar a quantidade de argumentos;
1. Se argumentos = 3, cria senha com valor passado;
1. Se argumentos = 2, cria senha random.

### Deletar uma senha 
* Argumentos => (rm), (nome);
1. Checar a existência do arquivo;
1. Checar todas as senhas;
1. Verificar se a senha já existe. Se a senha não existir, avisar;
1. Se a senha existir, deletar.

### Mostrar as senhas salvas para cada app
* Argumentos => (show);
1. Checar a existência do arquivo;
1. Mostrar todas as senhas.

### Pegar uma senha específica
* Argumentos => (get), (nome);
1. Checar a existência do arquivo;
1. Checar todas as senhas;
1. Verificar se a senha já existe. Se a senha não existir, avisar.
1. Se a senha existir, levar para área de transferência.

### Atualizar senha
* Argumentos => (mod), (nome), (senha);
1. Checar a existência do arquivo;
1. Checar todas as senhas;
1. Verificar se a senha já existe. Se a senha não existir, avisar.
1. Se a senha existir, atualizar.