# 📒 Mon carnet de bord

Amar

Alle
**Adresse de mon site :** https://alleamar5.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code est stocké sur GitHub et déployé sur PythonAnywhere, où il est exécuté pour fabriquer la réponse envoyée au navigateur.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que mon site est hébergé sur PythonAnywhere et accessible sur Internet. Mon voisin peut simplement ouvrir l'adresse du site dans son navigateur, sans installer quoi que ce soit.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom de domaine est www.google.com et le chemin est /maps.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ « Not Found » signifie que la ressource demandée n'a pas été trouvée. C'est le serveur qui renvoie cette réponse, généralement avec le code HTTP 404, et le navigateur l'affiche.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Flask peut provoquer une erreur lors de l'enregistrement des routes, car deux fonctions utilisent le même nom de point de vue (endpoint). On peut consulter l'Error log pour identifier l'erreur.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie du texte contenant du HTML. Le navigateur interprète les balises pour afficher une page structurée avec des titres, des paragraphes et des listes.

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ `<h1>` sert au titre principal, `<p>` crée un paragraphe, `<ul>` crée une liste à puces et `<li>` représente un élément de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ Parce que la balise `<img>` utilise une URL qui pointe vers une image hébergée sur un autre serveur. Le navigateur télécharge l'image depuis cette adresse pour l'afficher.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Cela permet de mieux organiser le projet. Le développeur peut modifier le fonctionnement en Python, tandis que le graphiste peut modifier la présentation HTML sans toucher au code Python.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Les variables sont remplacées par le serveur grâce à Flask et au moteur de templates Jinja. Je l'ai vérifié avec Ctrl + U : le code source reçu par le navigateur contient les valeurs réelles, par exemple Amar Alle, et non les expressions `{{ prenom }}` et `{{ nom }}`.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML définit la structure du contenu de la page, comme les titres et les paragraphes. Le CSS définit son apparence, comme les couleurs, les polices et les marges.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Deux fichiers principaux : le document HTML et le fichier CSS style.css.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Parce que le navigateur peut conserver une ancienne version du fichier CSS dans son cache. Ctrl + F5 force le rechargement de la page et de ses ressources.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur envoie la requête au serveur, et le serveur renvoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ J'ai observé deux requêtes principales : le document HTML presentation et la feuille de style style.css.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code 200 signifie que la requête a réussi. Le code 404 signifie que la ressource demandée n'a pas été trouvée. Mon site renvoie 404 Not Found lorsque je demande /favicon.ico.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Parce que ces modifications sont temporaires et locales à mon navigateur. Elles ne changent pas les fichiers enregistrés sur le serveur.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le nom du paramètre est search_query et sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Le serveur plante, car int() ne peut pas convertir le texte bonjour en nombre entier. Il faut vérifier la valeur reçue et gérer les erreurs de conversion, par exemple avec try et except.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Parce qu'un utilisateur peut envoyer du HTML ou du JavaScript qui modifie la page ou provoque une faille de sécurité. Il faut échapper les données ou utiliser un template qui les traite de manière sûre.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ Avec GET, les données du formulaire apparaissent dans l'URL, par exemple sous la forme `?prenom=Amar&ville=Paris`. Avec POST, les données ne sont pas affichées dans la barre d'adresse : elles sont envoyées dans le corps de la requête HTTP.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche, je choisirais GET, car les critères apparaissent dans l'URL et peuvent être copiés ou mis en favoris. Pour un formulaire de connexion, je choisirais POST afin de ne pas mettre le mot de passe dans l'URL. Il faut aussi utiliser HTTPS pour protéger les données pendant leur transmission.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non. POST ne rend pas les données secrètes : on peut les voir dans les outils de développement, dans l'onglet Réseau. HTTPS est nécessaire pour chiffrer les données pendant leur transmission, mais l'application doit aussi les protéger correctement.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_
