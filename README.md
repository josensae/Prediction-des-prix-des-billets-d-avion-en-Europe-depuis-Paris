# Projet-Python-pour-le-Data-Scientist

Bienvenu sur le Github de notre projet Python Pour le Data Scientist:

L'objectif du projet est de prédire les prix de billets d'avions entre Paris et 5 destinations (Londres, Moscou, Oslo, Madrid et Athènes) pour des allers-retours d'une semaine entre début avril et fin septembre 2022. 

Notre projet ce divise en 4 étapes :

## 1. La récupération des données ou Webscrapping

Le but est de récupérer sur le site Kayak les caractéristiques de tous les vols entre Paris et une des 5 destinations sélectionée. 
Par exemple pour un vol Paris-Moscou, notre code de scrapping va récupérer les informations encadrées en rouge.

![Kayak_image_Scrap](https://user-images.githubusercontent.com/84531691/147736791-ef41ba06-b442-48b0-b5dc-88ef68dd8906.png)


## 2. La Manipulation de données

En utilisant la bibliothèque "pandas", nous avons formaté les données récupérées suite au scrapping.
En effet, les données récupérées sont stockées sous forme de texte donc nous les avons converties en variables quantitatives.

Avant             |  Après
-------------------------|-------------------------
<img width="521" alt="tableau_avant" src="https://user-images.githubusercontent.com/84531691/147737482-bd5692be-04cf-4cd7-aedc-651df79e16e4.PNG">|<img width="456" alt="tableau_apres" src="https://user-images.githubusercontent.com/84531691/147737518-e66277b1-6a9a-44e3-8e7e-1453dd6a1608.PNG">

## 3. DataVizualisation

Après avoir récupéré et formaté les données, nous sommes passés à l'étape de dataviz, pour donner du sens aux variables sélectionnées.

## 4. Modélisation

A partir des données sur les vols et en utilisant la bibiliothèque Scickit, nous avions créé un modèle capable de prédire les prix des billets d'avion d'un aller-retour Paris avec une des 5 destinations européennes. Nous l'avons ensuite complété par un modèle de deep learning en utilisant tensorflow et Keras, que nous avons trouvé plus perfomant en terme de prédiction.
