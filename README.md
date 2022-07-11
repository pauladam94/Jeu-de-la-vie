# Jeu-de-la-vie
Programmation du jeu de la vie de Conway en python

Ce projet consiste en la programmation du fameux automate cellulaire du "jeu de la vie" inventé
par Conway.Ce projet a ensuite inspiré la modélisation 2D choisit pour mon TIPE sur les feux de
forets.

Différents problèmes de programmation sont ici intéressants :

- tout d'abord une réflexion sur comment créer un espace pseudo infini ou l'automate peut se 
développer, une solution est de considérer un tore en bouclant les cotés les uns sur les autres.

- une réflexion sur la complexité de même est très importante pour pouvoir calculer en temps réel
les itérations ou générations de l'automate. Il ne faut pas en effet actualiser toutes les cases 
mais uniquement celle en activité ce qui réduit grandement le nombre de calcul.
