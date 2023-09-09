# gerando-arquivos-aleatorios-Provas
Suponha que você seja um professor de geografia, tenha 35 alunos em sua classe e queira
aplicar uma prova surpresa sobre as capitais dos estados norte-americanos. Infelizmente,
sua classe tem alguns alunos desonestos, e não é possível confiar neles acreditando que
não vão colar. Você gostaria de deixar a ordem das perguntas aleatória para que cada
prova seja única, fazendo com que seja impossível para alguém copiar as respostas de
outra pessoa. É claro que fazer isso manualmente seria uma tarefa demorada e maçante.
Eis o que o programa faz:
• Cria 35 provas diferentes.
• Cria 50 perguntas de múltipla escolha para cada prova em ordem aleatória.
• Fornece a resposta correta e três respostas incorretas aleatórias para cada
pergunta em ordem aleatória.
• Grava as provas em 35 arquivos-texto.
• Grava os gabaritos contendo as respostas em 35 arquivos-texto.
Isso significa que o código deverá fazer o seguinte:
• Armazenar os estados e suas capitais em um dicionário.
• Chamar open(), write() e close() para os arquivos-texto contendo as provas e os
gabaritos com as respostas.
• Usar random.shuffle() para deixar a ordem das perguntas e as opções de
múltipla escolha aleatórias.
