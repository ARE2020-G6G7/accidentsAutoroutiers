## Travail effectué sur le projet semaine par semaine

=> Description hebdomadaire du travail effectué (variez les auteurs !)

### Semaine 1

Bonjour a tous,

A partir de ce jour, nous actualiserons chaque semaine le journal de l’aventure de notre projet.
Pour le lancement de nos idées, nous avons commencé par l’établissement  de notre monde, nous avons d’abord  songer  à une matrice  (d au km x 3 voies) censée représenter une chaussée d'autoroute à 3 voies, dont les coefficients seraient 1 (risque faible), 2 (risque moyen) ou 3 (risque élevé). 

Sauf que cette modélisation ne s’avère pas très efficace: nous devons modéliser l'ensemble des véhicules avec, pour chacun, leur risque d’accident ce qui nous semble irréalisable pour notre niveau. Nous avons ensuite pensé à utiliser un graphique pour modéliser notre projet ce qui nous a paru plus efficace et plus réalisable.

Ainsi, pour cela, le graphique imaginé sera représenté par  3 courbes, chaque courbe symbolisant un conducteur sur chaque voie, c’est-à-dire, la voie pour véhicules lents, la voie centrale, et la voie de dépassement. Les paramètres d’évolution des courbes sont le temps (en heure) en abscisse, et en ordonnée  le coefficient multiplicateur d’accident qui dépend des coefficients (0, 1, 2 ou 3) de la matrice  auquel nous avons pensé au départ, ces coefficients étant obtenus par les facteurs d’accidents.
Le coefficient d'accident au départ est de 1 pour un conducteur normal. Puis, il sera multiplié par d’autres coefficients en fonction des risques ajoutés.

On se questionne sur comment manipuler les statistiques pour obtenir les coefficients multiplicateurs.
On se retrouve donc à la semaine prochaine pour la suite de nos avancées !

L'équipe vous souhaite un bon confinement :)

Bonne journée

#### Auteurs F. Julien et S. Ménalie

### Semaine 2

Rebonjour à tous, 

Nous revenons vers vous pour enfin alimenter le blog une semaine après!
Bien que le début de notre projet a été difficile pour élaborer notre modélisation, nous avons finalement réussit à nous concrétiser un peu mieu la manière dont nous allons réaliser notre projet.

Ainsi, nous présenterons un tableau composé d’un certain nombre de lignes qui variera en fonction des heures de conduites, ainsi que de 3 colonnes représentant chacune une voie de l’autoroute  auquel nous avions déjà songé la 1ere semaine.
Il y aura un véhicule par voie et nous étudierons son risque d’accident avec le nombre d’heures d'éveil qui ne fera qu’augmenter. 
Ainsi, notre tableau s’allongera verticalement jusqu’à ce qu’il y ait potentiellement un accident. 
Par conséquent, notre autoroute aura une distance infinie. 

Les valeurs de ce tableau seront sûrement  des coefficients qui représenteront le risque d’avoir un accident sur telle voie et à telle heure. Nous utiliserons des coefficients multiplicateurs qui seront de plus en plus importants en fonctions des différents paramètres. Mais nous sommes toujours dans la recherche d’information en % sur notre projet.

Nous avons de même rédiger quelques codes python, ces codes permettant d’obtenir des coefficients multiplicateurs d’accidents en fonction des différents motifs ( temps d’éveil, alcoolémie, moment de la journée, week-end ou non et le sexe de la personne). 
A partir de cela, nous parviendrons sans doute à rendre notre projet plus dynamique et plus étudiable!

Nous espérons vous retrouver la semaine prochaine en forme pour de nouvelles aventures !

L’équipe vous souhaite un bon confinement.

#### Auteurs S. Ménalie et F. Julien  

### Semaine 3

Bonjour à tous, 

Nous revoilà aujourd’hui pour la suite de notre journal.
Nous avons décidé de diviser notre étude en 2 parties.
Dans un premier temps, nous étudierons le nombre d’heure d’éveil maximal d’un conducteur à partir de l’hypothèse principale, en faisant varier nos différents paramètre, et ce, pour chaque voie. Dans un deuxième temps, nous répondrons à notre problématique, à partir des résultats précédents en faisant cette fois varier le nombre d’heure d'éveil avant la conduite, donc en prenant en compte la fatigue, 1er facteur d’accident.

Nous avons donc rajouté des conditions initiales dans la première partie: l’exclusion du facteur de fatigue, de toute distraction par téléphone ou entourage, l’absence d’accident ou de chantier, une route en bonne état, un véhicule correct, un beau temps (pas d’intempérie).

Concernant l’avancement du projet, nous avons commencé l’élaboration du code du risque d’accident global de la voie 1. Étant trop longue, nous avons décidé de le diviser en plusieurs codes, séparant chaque coefficient-paramètre.
Souhaitant de même obtenir une certaine différence entre les 3 voies, soit un coefficient qui variera en fonction de la vitesse, facteur individuel à chaque voie, nous avons trouvé qu’une augmentation de 5 km/h double le risque d’accident. Ainsi, nous avons défini un  coefficient de 1 pour une vitesse de 60km/h (voie 1) à partir duquel nous avons fait découler les coefficients des autres voies (voie 2: x16 et voie 3: x28).  

Nous avons de même défini le code du paramètre jour, utile pour la réinitialisation de l’heure à 0 et donc le risque d’accident en Week-End ou non. 
Dernièrement, nous avons affiné le code de l’alcool, de manière à pouvoir y rentrer n’importe qu’elle valeur. Nous disposons ainsi aujourd’hui de code pour chacun de nos paramètres, qui nous reste plus qu’à appliquer sur nos voies. 
Le corps du code de la Voie 1 reste cependant à finir et à améliorer/ diviser ingénieusement.
Barrage pour l’avancée: nous réfléchissons toujours sur comment manier nos coefficients multiplicateurs pour simuler un accident.

Merci d’avoir prêté attention à notre rédaction, 
On se retrouve la semaine prochaine pour l’actualisation de notre projet.

Sur ce, je vous souhaite une très bonne fin de semaine :) 

#### Auteurs S. Ménalie et F. Julien 


### Semaine 4

Bonjour tout le monde,

Nous revoilà aujourd’hui pour la suite de l’actualité du projet! 
Cette semaine, notre travail s’est concentré sur du codage et de la réflexion sur l’aboutissement du projet, nous n’avons donc pas énormément de choses à communiquer sur le journal.

Nous avons cette semaine intensifié notre travail sur le code. Nous avons amélioré les codes de nos différents paramètres (alcool, éveil, coeff_alcool, moment, sexe, jour, coeff_par_voie et week) de manière à pouvoir  les coordonner et les ajouter dans le code global: voie_sans_fatigue qui est en cours. 

Comme nous l’avons déjà dit, nous effectuerons de même, un second code global voie_avec_fatigue qui prendra en compte la fatigue, paramètre principal, qui sera appliqué au code voie_sans_fatigue.  
Tout ceci nous permettra de répondre ingénieusement à notre objectif.
Bien évidemment, tout ceci est en cours d’élaboration. 

Nous réfléchissons toujours à la manipulation de nos résultats, chose pas très simple ٩(๑❛ᴗ❛๑)۶.  
Pour la représentation des données obtenues, nous penchons pour un dictionnaire de type dict[str: tuple[Number,str,Number]], à l’image d’un tableau. Il aboutira à un graphique lentement mais sûrement!

Sur ce, nous vous souhaitons une bonne semaine.
En espérant que l’intelligence soit avec nous.

A la prochaine chers lecteurs !

#### Auteurs F. Julien et S. Ménalie


### Semaine 5
Cher lecteurs,

Depuis un bon moment, nous n’avions pas réellement fait de progrès dû à un problème dans le code global. Donc, notre rythme de travail s’était atténué. Mais grâce à l’intervention de l’un de nos professeurs, nous avons pu résoudre notre problème, reprendre et continuer.
Nous continuons à réaliser notre code global tout en essayant de l’optimiser.  Nous avons pris la décision de faire ressortir un tableau ainsi qu’un graphique si nous y arrivons.

Notre code global cadré par une boucle while se bouclera par l’utilisation d’un random permettant de simuler un accident.
Pour parvenir à l’élaboration du tableau, cela n’étant pas dans nos compétences, nous nous sommes aidé d’un cours Python du site openclassrooms.com .

Pour l’instant, nous sommes en cours d’écriture d’un code pour le tableau qui prendra en compte les 3 voies avec l’indication du nombre d’heure d'éveil, des risques d’accident à chaque heure ainsi qu’une affirmation ou non de la réalisation de l’accident. Nous obtiendrons ces informations sous forme d’un tuple à la sortie du code global.

Par conséquent, nous approfondirons cette ultime étape de représentation des données dans l’espoir de clôturer le projet dans une  semaine et demie.

Sur ce, nous vous remercions d’avoir prêté attention à notre étude, tout au long de son déroulement, on vous dit à la semaine prochaine pour la dernière rédaction de ce carnet de bord.

Portez-vous bien et à bientôt ! 

#### Auteurs F. Julien et S. Ménalie


### Semaine 6

Bonjour à tous,

Aujourd’hui nous actualisons ce journal une dernière fois avant le rendu du projet. A l’heure où nous écrivons, nous sommes finalement parvenu à terminer entièrement le projet. Nous avons finalement contourner l’idée de créer un tableau car cela nous ralentissait dans l’avancement de notre projet, car il présentait trop de complication au niveau du codage. Nous avons donc supprimé le code intermédiaire list_for_board pour aussitôt le remplacer avec list_for_graph.
Nous nous sommes donc directement penchés sur la création du graphique.

Finalement,l’un de nous a terminé des paragraphes incomplets nécessaires pour le site tel que l’introduction ou la présentation des choix.
Et nous avons ainsi pu terminer le projet dans de bonnes conditions.

Ce projet fût une bonne expérience en terme de communication entre les membres ayant participé continuellement au projet ainsi qu’en terme de découverte et d'approfondissement de nos connaissances: le thème de l’autoroute a été réellement une bonne idée car elle nous a permis de récolter des informations sans trop de difficultés. 

D’autre part, l’utilisation d’un logiciel informatique tel que Python était non seulement à notre guise mais aussi à notre dépassement. Nous avons pu découvrir de nouveaux codages pour la création de tableaux ou de graphiques.
Tout cela nous a permis de générer des données aussi conformes que surprenantes. 

Cela nous incite bien à continuer dans cette voie!  
Nous vous remercions d’avoir suivi le déroulement de notre projet.

#### Auteurs S. Ménalie et F. Julien
<a href="index.html"> Retour à la page principale </a>
