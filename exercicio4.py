
"""
Sequencia de chaves:30, 40, 24, 58, 48, 26, 11, 13:
30

30
  \
   40

   30
  /  \
24   40

   30
  /  \
24   40
         \
          58

   30
  /  \
24   40
         \
          58
         /
       48

     30
    /  \
  24   40
    \      \
    26     58
           /
         48

      30
     /  \
   24   40
  /   \      \
11    26     58
             /
           48

Resultado final:
        30
       /  \
     24    40
    /  \      \
  11   26     58
    \         /
    13       48
Usando regra da BST em todas as inserções
"""
