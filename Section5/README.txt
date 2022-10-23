Réalisé par Martin Gyselinck et Luca Hafhouf

Le fichier en se lançant appelle une seule fonction : tester().
Cette fonction reprend toutes les fonctions de tests, contenant chacune quelques assertions,
afin de vérifier le bon fonctionnement du code.

Le petit plus:
En temps normal, une AssertionError amène un arrêt de l'exécution du code.
Mais nous avions envie de montrer que notre code détectait bien les erreurs.
Donc nous avons, par un système de try et de except, créé une fonction verify(),
capable de renvoyer une erreur mise en forme (en couleurs etc), et ce sans arrêter le code.
Pour mettre cela en place, il a fallu un peu chipoter sur la forme d'une fonction: coordinate,
qui peut maintenant accepter une tuple contenant les deux communes.
