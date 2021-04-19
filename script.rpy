# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Narrateur', color="#c8ffc8")
define m = Character('MisterADN', color="#F8BC26")

# Le jeu commence ici
label start:

#label scenario_vertebre_oui_terrestre_carnivore_separation:
#(Image de la planète 5)

   n "Salut à toi jeune scientifique ! Nous voici quelques 200 millions d’années après le féroce combat qu’il y a eu lieu entre le … et le Broutiminus Chordus. Je te propose dès à présent de suivre l’histoire évolutive des descendants de …"

#(Image d’un paysage polaire)

   n "Comme tu peux le voir, l’endroit est plutôt frais pour la saison, cet environnement correspond plus ou moins à notre Antarctique sauf qu’ici la fraicheur ambiante est dû à une masse importante de nuage qui couvre l’ensemble de la région,"

   n "ceux-ci empêchent les rayons du soleil de passer et de réchauffer l’ambiance. Car en effet au-dessus de ces nuages, on retrouve une température proche des forêts tropicales de ce monde (environ 35-36°)."

#(Image d’un Hasnovourus chordus derrière un gros caillou)

   n "Tiens ! Malgré cet environnement extrême, il semble que la vie ait trouvé son chemin. Allons voir ça de plus près."

#(Le caillou disparaît et on voit la bestiole en entier)

   n "Incroyable, je te présente le Hasnovourus chordus, il s’agit d’un descendant de Carnicroqus chordus dont l’évolution l’a mené à vivre dans ces lieux reculés. Vois-tu ce pelage bleuté et ces deux belles cornes en formes de cornets de glace ?"

   n "Et bien il s’agit d’un signe distinctif que prend cet animal pour montrer qui est le chef de sa meute, les autres ayant un pelage virant au blanc cassé et au rose pâle."

   n "Bien évidemment, comme dans chaque espèce de nombreuses différences existent entre les individus d’une même population et c’est cela qui leurs permettent d’évoluer."

#(Image d’une famille d’Hasnouvourus avec un chef et 3-4 autres plus petits)

   n "En effet il s’agit d’un animal vivant en meute, comme des loups ! Leur mode de chasse étant de s’enfouir dans la neige et de ne laisser que les cornets de glaces passés."

   n "Des animaux peu vigilants comme les Alessandris codusmaximus vont vouloir s’en nourrir mais resteront collés par la langue aux cornet de glaces."

   n "C’est à ce moment-là que nos amis les Hasnovourus s’élanceront sur la pauvre bête et apporteront sa dépouille au chef de la meute afin qu’il partage les parts pour chacun."

#(Vidéo d’un tremblement de Terre)

   n "Mais qu’est-ce qu’il se passe ???"

#(Image d’iles flottantes)

   n "Faramineux ! Dû à un alignement parfait des deux lunes et de la grande étoile, une sous gravité s’est produite permettant à des lopins de terres de s’envoler au-dessus des nuages ce qui forme des îles flottantes !"

#(Montrer une famille de Hasnouvourus chordus)

   n " Sur certaines de ces îles, on retrouve plusieurs familles de Hasnouvourus chordus. Ces animaux risquent de disparaître car comme expliqué précédemment au-dessus de cette couche de nuage la température est assez importante…"

   n "toutefois le climat humide pourrait pallier le manque de fraîcheur. Bien évidemment comme tu as pu le voir ces îles ne sont pas reliées entre elles formant ainsi un grand nombre de population d’Hasnouvourus."

   n "Ceux qui n’ont pas été pris par ce changement géologique quant à eux sont restés en dessous de la couche de nuage et leur environnement ne s’est pas changé."

   menu:
         n "Alors as toi de décidé maintenant, avec quels amis Hasnouvourus souhaites tu poursuivre ton aventure ?"

         "Je souhaite continuer avec les Hasnouvourus chordus qui restent dans le pays de glace":
            jump pays_de_glace     

         "Je souhaite continuer avec les Hasnouvourus chordus qui sont sur les îles flottantes":
            m "WIP"
   m "WIP"

  


   return

label pays_de_glace:
 #(Mister ADN apparaît)      

   m "Hey salut comment ce passe ton aventure ? Avant que tu ne continues je tenais à te dire que l’apparition de ces îles volantes est considérée comme une séparation qui si les populations vivantes actuellement s’adaptent,"

   m "donnera problablement naissance à une nouvelle espèce car l’environnement sera modifié mais en plus, plus aucun contact avec les Hasnouvourus du sol hermieteonien ne sera possible."

   m "Te rappelles que nous en avions déjà parlé précédemment ? Avec les Squelettus Chordus, nous avions appelé ça une spéciation allopatrique le fait que suite à une barrière géologique, de nouvelles espèces apparaissent. Bien, faisons un bond dans le temps pour voir la descendance de ta population."


#(image du désert de glace avec des oasis juste en dessous des zones lumineuses)

   n "Nous nous retrouvons 200 millions d’années après les évènements de skypiea et la descendance notre population de hasnouvourus vit sans se soucier des îles célestes."

   n "A un détail près, le courant d’air qui a envoyé les parcelles de terre par-dessus les nuages ont créé aussi des trous dans ce mur blanc. La lumière et les rayons du soleil auparavant inexistant sont à présent visible et ont un impact sur les zones quelles touchent."

#(Image d’un oasis (pas la boisson))

   n "En effet les endroits touchés par les rayons lumineux sont fortement chauffés et au cours des millions d’années après les évènements de skypiea plusieurs oasis vont se former sur le territoire avec un bassin d’eau chaude et de la végétation toujours entouré par le désert de glace qui se trouve toujours sous les nuages."

   n "Un phénomène faisant penser à du paranormal a pu être observé en périphéries des oasis dans plusieurs meutes de hasnouvourus sur tout le territoire. Les chefs de meutes au pelage bleuté deviennent subitement très agressifs et plus rapides s’attaquant aux autres membres de la meute ce qui aura pour conséquence de les infecter et de les rendre bleu également."

#(image d’un individus bleu enragé pas content)

   n "Ce phénomène à une explication, les UV qui touchent les individus bleus activent une bactérie vivant en Hasnouvourus."

   n "En absence de rayon lumineux depuis des millions d’années la bactérie est toujours restée inactive mais leur présence était quand même détectable grâce au bleu du pelage d’une certaine partie de la population."

   n "Mais avec les évènements de skypiea la bactérie est devenue active ce qui va avoir une grande influence sur les générations de Hasnouvourus au cours des millions d’années à venir,"

   n "dans un certain périmètre autour des oasis nous allons retrouver uniquement des groupes d’individus bleu vivant sur un même pied d’égalité mais pratiquant un mode de chasse beaucoup moins subtile et moins coordonné dans le but de se nourrir rapidement sans partager."

   n "Alors que les meutes restées loin de ses oasis et des UV ont gardé leur système de hiérarchie et leur chasse groupée dans le but de partager équitablement sans savoir ce qui se passe près des oasis maudites."


   menu:
      n "Qui voulez-vous suivre ?"

      "La nouvelle population hasnouvourus gablue en périphérie des oasis maudits":
            jump gablue

       "La population disciplinée de hasnouvourus diwhite dans le désert de glace":
            m "WIP"
   
   m "WIP"

       
label gablue:     
       
   n "Vous avez décidé de continuer votre aventure avec les Gablue, une population formée de groupes d’individus intelligents d’un bleu homogène non loin des oasis maudites."   

#(Monsieur ADN apparait) 

   m "Sais-tu pourquoi les gablues sont tous colorés d’un bleu neutre ni trop clair ni trop foncé ? simplement car la sélection naturelle est un mécanisme très sensible,"
   
   m "un trop haut taux de bactéries dans l’organisme des hasnouvourus provoquaient une mort instantanée par septicémie chez l’individus et un trop bas taux de bactéries ne permettaient pas aux individus concernés de concurrencer leurs congénères ce qui fait qu’ils n’étaient pas assez bien adaptés pour survivre et se reproduire."

   m "Le caractère idéal est le bleu neutre qui propose la variation la plus propice à son environnement."
   








    return
