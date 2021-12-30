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

