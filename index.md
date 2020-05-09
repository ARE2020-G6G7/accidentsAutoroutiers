# Les accidents d'autoroute sur le territoire français

Les autoroutes, maillages de voies rapides reliant toutes les zones d’un territoire entre elles, constituent aujourd’hui un réel dynamisme pour la mobilité des personnes en accroissement constante.  Ces voies représentent de réelles avantages par son gain de temps pour les usagers et les bénéfices rapportés pour l’Etat.

Or ces voies rapides ne sont pas sans défauts. Outre les coûts élevés, la sécurité des conducteurs est aussi un objectif majeur pour les services du réseau autoroutier. En effet, les accidents y sont fréquents, et ce, dû principalement à l’état et au comportement de l’individu.

Nous avons donc choisi de nous concentrer sur ces accidents d’autoroutes. Nous avons étudié ce phénomène dans le but de déterminer le temps maximal qu’un individu peut tenir  dès la prise de l’autoroute, compté donc comme point départ. Partant d’une hypothèse suggérant que l’absence de fatigue était bénéfique pour la conduite, nous avons fait varier cela pour pimenter notre étude.

Cette étude a pu être simulé grâce à  plusieurs paramètres influents dont principalement le sommeil représentant la fatigue, mais aussi d’autres, secondaires, tel que l’alcoolémie ou le moment de la journée. Nous avons enfin testé ceci sur trois voies différenciables par leur vitesse,  pour modéliser les résultats dans un graphique.

Ainsi, contrairement à nos attentes, nous avons pu assister une augmentation presque démesurée des risques d’accidents allant même jusqu’au millier. Cette analyse est détaillé dans le paragraphe dédié à la présentation des choix. 

A présent, nous vous invitons à naviguer vers le bas pour découvrir en profondeur notre étude. Bonne aventure !



## Highway accident on French territory

Motorways, a mesh of expressways linking all areas of a territory together, constitute nowadays a real dynamism for the mobility of people, which is constantly increasing.  These roads represent real advantages in terms of time savings for users and benefits for the State.

However, these expressways are not without flaws. Besides the high costs, driver safety is also a major goal for the services of the motorway network. Accidents are frequent on motorways, mainly due to the condition and behaviour of the driver.

Therefore, we have  chosen to focus on these motorway accidents. We have studied this phenomenon in order to determine the longest time a person can maintain as soon as he takes the motorway, counted as a starting point. Based on a assumption that suggests the absence of tiredness is beneficial for driving, we have varied this to spice up our work.

This study could've been simulated thanks to several influential factors, mainly sleep, which represents fatigue, but also other, secondary indicators, like the blood alcohol level or the time of day. Finally, we tested this on three tracks, differentiable by their speed, to model the outcomes in a graph.

Therefore, unlike our expectations, we were able to witness an almost disproportionate increase in the risk of accidents, even reaching up to a thousand. This analysis is detailed in the paragraph dedicated to the presentation of the choices. 

At this point, we invite you to navigate down to discover our study in deeper detail. Good luck!



## Présentation de l'équipe

| ᕕ( ᐛ )ᕗ | ᕦ(ò_óˇ)ᕤ | ಠ_ಠ | ٩( 'ω' )و |
|-----|--|--|--|
| S. Ménalie| A. Manel | F. Éric  | F. Julien  |


## Description synthétique du projet

**Problématique : La variation du nombre d’heure d’éveil influe-t-elle sur les accidents d’autoroute ?** 

**Hypothèse principale : Un sommeil de 7h suivi d’un temps d’éveil inférieur à une demi-journée est suffisant pour  réduire amplement le risque d’accident.**

**Hypothèses secondaires :** 

**Objectifs : Déterminer le nombre d’heures d'éveil maximal d’un conducteur afin de minimiser les risques d’accidents, à  l’aide de plusieurs autres paramètres.**

**Critère(s) d'évaluation : Évaluer le taux d’accident sur autoroute en fonction du nombre d’heure d’éveil.**

## Présentation structurée des résultats

Nous avons choisi de modéliser nos résultats à l’aide d’un graphique. Ce graphique illustre l’allure de trois courbes, une pour chaque voie, et ce, à partir des données des valeurs obtenues dans le dictionnaire ressortie de notre code global. 
Nous avions pour objectif de créer aussi un tableau pour la représentation des données mais cela ayant compliqué notre travail informatique, nous avons directement poursuivi avec  le graphique qui était censé apparaître à l’aide du tableau.
 
Ainsi, pour l’élaboration de ce graphique qui a pour abscisse le temps en heure et en ordonnée les coefficients multiplicateurs de risque d’accident à chaque heure, nous avons réalisé un code intermédiaire (list_for_graph) permettant de retranscrire en listes les données utiles du dictionnaire (temps et coefficients). 

Pour en revenir au point départ de notre codage, soit aux multiples codes-outils que nous avons créer pour alimenter le code global, voici leur description.
Chacun de nos paramètres-codes contribuant au code global renvoie tous des coefficients multiplicateurs de risques d’accidents qui varie en fonction de l’évolution des paramètres entrés.
Les chiffres ressorties  de ces “sous-codes” sont appliqués à une donnée factuelle récupérée d’un tableau issue d’un site qui nous a été recueilli par un professeur, le tableau  indiquant le nombre d’accidents de route  pour telle année.
Et ces chiffres obtenus des “sous-codes” sont renouvelés à chaque heure selon l’évolution des paramètres et variables.    
Tout ce travail s’effectue dans le code global.

Evidemment,  un accident n’étant pas réellement  prévisible dû au comportement du conducteur, l’accident est simulé par une fonction aléatoire (random) , et cela permettant de clôturer la boucle. Il en sort alors un dictionnaire répertoriant dans cet ordre, pour chaque voie, le nombre d’heure d’éveil (base de l’avancée du code global), le temps de conduite, le temps de repos, la liste contenant les risque d’accident enregistré à chaque heure, ainsi qu’une affirmation de la réalisation de l’accident ou non. Cette énumération est classée dans un tuple. 
Ce dictionnaire, comme déclaré précédemment, nous a finalement servi de tableau lui-même, faute de compréhension du codage d’un tableau en python.

Par conséquent, par brève analyse, nous pouvons affirmer  d’une part que les courbes ressorties de notre étude sont très aléatoires mais cela est attribuable. Effectivement, cela est dû à la fonction aléatoire qui régit la fonction globale. 
Mais aussi, d’autre part, et cela reste bien la conclusion la plus flagrante, les coefficients apparaissant au cours de la boucle globale (qui n’est pas aléatoire) peut monter jusqu’à l’extrême comme par exemple  2413.95039375, deuxième et dernier risque ressortie lors d’un essai pour un conducteur de la voie 3 (110km/h) sobre et très fatigué, d’où la surprenante variation des courbes.  

Ainsi, pour une simple conclusion moraliste, priorisez votre état et votre santé au reste pendant la conduite ! Soyez conscient de vous-même car les risques de vous retrouver invalides peuvent être extraordinairement élevés !  


## Lien vers page de blog : <a href="blog.html"> C'est ici ! </a>

## Bibliographie :

**Carte mentale de vos mots-clés, en utilisant** <a href="https://cdn.discordapp.com/attachments/692014867380437042/698625264833265704/framindmap.png">Carte heuristique </a> 

Liste de l'ensemble des ressources bibliographiques utilisées pour vos travaux. **<= Indiquez le canal utilisé pour les trouver (Google Scholar, sources wikipedia, ressources en ligne SU, ...)**
1.	Damien Mascret, « Conduire fatigué revient à conduire en état d’ébriété », article,  Le Figaro santé publique, France, publié le 22/12/2016 à 19 :11, site d’accès : https://sante.lefigaro.fr/article/conduire-fatigue-revient-a-conduire-en-etat-d-ebriete/.

2.	« La conduite automobile et l'alcool sont incompatibles », article, MAIF, France, site d’accès : https://www.maif.fr/conseils-prevention/la-route/ma-securite/capacites-conducteur.html

3.	Sébastien Roux et Philippe Zamora « L'impact local des radars fixes sur les accidents de la route : un effet important après l'installation mais plus réduit à long terme », article, France, Economie et Statistique, Année 2013, 460-461, p. 37-68,
disponible sur : http://www.persee.fr/doc/estat_0336-1454_2013_num_460_1_10197 

4.	« Alcool au volant, optez pour le risque zéro », article, MACSF, France, publié le 19.12.2017, site d’accès : https://www.macsf.fr/Actualites/Auto-Moto/Alcool-au-volant-optez-pour-le-risque-zero

5.	Sandrine Masson « Les 4 types d’accidents les plus fréquents chez les jeunes conducteurs », article, Dispofi.fr, Mise à jour le 03/06/19 à 11:30, site d’accès : https://assurance-auto.dispofi.fr/jeune-conducteur-accident-voiture

6.	Jihane, « Conduite de nuit : redoublez de vigilance ! », article, Le Lynx, France, site d’accès : https://www.lelynx.fr/assurance-auto/conduite/securite-routiere/prevention/meteo/nuit/

7.	Données communiquée par l’ONISR, « Statistiques d’accidents, année complète 2018 » , article, Association Prévention Routière, France,  publié le 22 décembre 2019, site d’accès : https://www.preventionroutiere.asso.fr/2019/12/22/statistiques-daccidents/
	 
8.	« Statistiques des accidents avec alcool », article, Permis Ecole, France, Année 2020,  site d’accès : https://www.permisecole.com/conduite/route/statistiques-accidents-alcool#/

9.	«Vigilance, fatigue, stress... » article, En voiture Simone, France, site d’accès :  https://www.envoituresimone.com/code-de-la-route/cours/CONDUCTEUR/vigilance-fatigue-stress-gen13l3#la-fatigue-la-somnolence

10.	« La fatigue et la conduite », article, Sécurité Routière, France, site d’accès : https://www.securite-routiere.gouv.fr/dangers-de-la-route/la-fatigue-et-la-conduite

