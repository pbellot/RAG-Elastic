# Interrogation de HAL pour récupérer des PDF

Pour ce TP, vous interrogerez le serveur de publications HAL en utilisant directement l'API dédiée et des requêtes HTTP. Cette interrogation se fera tout d'abord manuellement (saisie de la requête HTTP dans la barre d'adresse du navigateur) puis automatiquement dans un notebook Python. HAL est une bibliothèque numérique ouverte d'articles couvrant tous les domaines scientifiques. Plus de 1,2 millions d'articles sont accessibles en texte intégral et les méta-données de plus de 3,4 millions d'articles sont disponibles.

Le cadre expérimental consistera à explorer un thème scientifique de votre choix (les exemples ci-dessous utilisent comme thème "_informatique quantique_", vous le remplacerez par un thème de votre choix).

**1) Explorer [HAL](https://hal.science) :**

*   saisir une requête dans le champ de recherche,
*   observer l'URL générée,
*   analyser les possibilités de filtrage offertes dans la fenêtre des résultats qui s'affiche, 
*   choisir des articles dans la liste des réponses et observer les méta-données associées

Par exemple pour la requête "_informatique quantique_", l'URL générée est : [https://hal.science/search/index?q=informatique+quantique](https://hal.science/search/index?q=informatique+quantique)

**2\. Explorer l'[API HAL](https://api.archives-ouvertes.fr/docs/search). L'API est utilisée pour interroger HAL par programme : les requêtes sont envoyées au serveur HAL et la réponse est fournie sous la forme d'un texte en JSON, XML ou CSV.**

*   Explorer l'[API HAL](https://api.archives-ouvertes.fr/docs/search) en regardant et essayant les exemples donnés. Cela doit vous permettre de comprendre ce que désigne les **concepts de filtrage et de facette**. D'autres exemples de requêtes sont donnés [ici](https://wiki.ccsd.cnrs.fr/wikis/hal/index.php/Requêtes_sur_les_ressources_de_HAL#R.C3.A9cup.C3.A9rer_la_liste_des_collections_rattach.C3.A9es_.C3.A0_son_institution). 
    *   La requête "_informatique quantique_" avec réponses en XML correspond à l'appel de l'API : [https://api.archives-ouvertes.fr/search/?q="informatique quantique"&wt=xml](https://api.archives-ouvertes.fr/search/?q=%22informatique%20quantique%22&wt=xml)
    *   Varier le format de sortie de XML vers JSON puis CSV afin de comprendre ces formats
*   Trouver la requête à envoyer pour obtenir les articles qui traitent de l'informatique quantique et qui ont été publiés entre 2018 et 2022.
    *   On cherchera dans cette optique les articles dont le titre, le résumé ou les mots clés contiennent au moins l'un des mots suivants : _quantum, quantique, "informatique quantique", qubits, qbits_
    *   On filtrera la liste des réponses pour se limiter aux documents publiés entre 2018 et 2022
    *   On utilisera les facettes afin de connaître le nombre d'articles publiés pour chacun des années entre 2018 et 2022
    *   Grouper les résultats de façon à que l'on retrouve dans le fichier des sorties d'abord les documents de 2018, puis de 2019 etc.

Aide : regarder la liste des [champs](https://api.archives-ouvertes.fr/docs/search/?schema=fields#fields) disponibles pour savoir comment limiter la requêtes aux titres, résumés et mots-clés 

**3\. Créer un notebook Python qui pose la requête créée en 2. et qui enregistre la sortie dans un fichier au format JSON.**

Aide :

*   Pour poser la requête, on utilisera le package requests et la méthode [requests.get](https://www.w3schools.com/python/ref_requests_get.asp). Celle-ci retourne un objet de type [requests.Reponse](https://www.w3schools.com/python/ref_requests_response.asp). Si son contenu est au format JSON, les données sont accessibles par la méthode [requests.Reponse](https://www.w3schools.com/python/ref_requests_response.asp).json() mais son contenu complet au format texte est dans la variable .text
    *   reponses.json()\["response"\]\["numFound"\] permet connaître le nombre de réponses fournies
        
    *   réponses.text est la chaîne de caractères complète de toutes les réponses (= ce que l'on doit enregistrer)
*   Utiliser le champ _rows_ dans la requête pour limiter le nombre de réponses fournies à une valeur faible
*   Enregistrer le fichier avec les fonctions Python _open_ (argument "w"), _write_ et _close._ Pour bien faire, vous utiliserez la méthode _with_: 
    
    with open(nomFichier,"w") as file:  
         file.write(reponses.text)
    

**(optionnel) 4. Refaire 3. mais cette fois-ci avec une sortie au format CSV, enregistrer le fichier, le relire puis le transformer en DataFrame Pandas.**
