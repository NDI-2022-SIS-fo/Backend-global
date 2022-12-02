from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import Session

import main
from etat import Etat

class Carte(main.Base):
    __tablename__ = "cartes"

    id = Column(Integer)
    etat = Column(Enum(Etat))
    texte = Column(String)
    previewGauche = Column(String)
    previewDroite = Column(String)
    gauche = Column(Integer)
    droit = Column(Integer)
    explicGauche = Column(Integer)
    explicDroit = Column(Integer)


if __name__ == "__main__":
    main.Base.metadata.create_all(main.Engine)
    
    # Story 1 :
    cartes = [
        # BASE carte
        Carte(
            id = 1,
            etat = Etat.BASE, 
            texte="Hey ! Hier, j'ai invité un garçon à mon appart ! On s'est un peu chauffé entre nous et il y a eu un début de pénétration mais il n'avait pas de capote... C'est grave ?!", 
            previewGauche="Aucun risque s'il n'a pas éjaculé à l'intérieur de toi.", 
            previewDroite="Il peut y avoir des conséquences sans moyen de contraception.", 
            gauche = 2, 
            droit = 3, 
            explicGauche = 12, 
            explicDroit = 13
        ),
        # MID carte
        Carte(
            id = 2,
            etat = Etat._, 
            texte="Non, il n'a pas éjaculé. Mais j'ai entendu parler de VIH. Il faudrait que je me fasse dépister, non ?!", 
            previewGauche="Inutile de se faire dépister, tu le s'auras bien assez tôt si tu as attrapé le VIH.", 
            previewDroite="Tu as raison, certains dépistages sont rapides, accessibles et anonymes.", 
            gauche = 4, 
            droit = 5, 
            explicGauche = 14, 
            explicDroit = 15
        ),
        Carte(
            id = 3,
            etat = Etat._, 
            texte="Ah bon? Quelles peuvent être ces conséquences ?", 
            previewGauche="Laisse tomber de toute façon c'est trop tard.", 
            previewDroite="Tu peux tomber enceinte même sans éjaculation par exemple.", 
            gauche = 6, 
            droit = 7, 
            explicGauche = 16, 
            explicDroit = 17
        ),
        Carte(
            id = 5,
            etat = Etat._, 
            texte="Ah bon ? Je peux aller où ?", 
            previewGauche="Tu peux seulement le faire dans une clinique spécialisée sur les maladies du sexe.", 
            previewDroite="Renseigne-toi auprès d'un personnel de santé ou cherche ta question sur le site 'sida-info-service'", 
            gauche = 8, 
            droit = 9, 
            explicGauche = 18, 
            explicDroit = 19
        ),
        Carte(
            id = 7,
            etat = Etat._, 
            texte="Oh merde, je devrais faire quoi ?", 
            previewGauche="Il faut avorter au plus vite !", 
            previewDroite="Tu peux acheter un test de grossesse facilement à un supermarché.", 
            gauche = 10, 
            droit = 11, 
            explicGauche = 20, 
            explicDroit = 21
        ),
        # FIN carte
        Carte(
            id = 4,
            etat = Etat.FIN, 
            texte="Okay, ça me rassure. J'irai voir le médecin si je ressens quelque chose.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 6,
            etat = Etat.FIN, 
            texte="Oh non, dit pas ça, ce n'est pas drôle.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 8,
            etat = Etat.FIN, 
            texte="Ah... Je ne sais pas où trouver une clinique de ce type. C'est trop compliqué en plus, j'ai peur que mes parents l'apprennent", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 9,
            etat = Etat.FIN, 
            texte="Okay super, le site à l'air très complet. Je vais appeler un des numéro du site pour me renseigner facilement.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 10,
            etat = Etat.FIN, 
            texte="Oh non! Je suis trop jeune pour tomber enceinte", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 11,
            etat = Etat.FIN, 
            texte="Super je vais faire ça !", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),

        # Carte Informations
        Carte(
            id = 12,
            etat = None,
            texte="Mauvaise réponse - Pénétration sans protection et éjaculation - Toutes pénétrations non protégées peuvent avoir des risques. Des IST peuvent être attrapées, sans oublier le risque de grossesse. Même sans éjaculation ! Il faut utiliser des moyens de contraceptions.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 13,
            etat = None,
            texte="Bonne réponse - Pénétration sans moyen de contraception - Toutes pénétrations non protégées peuvent avoir des risques. Des IST peuvent être attrapées, sans oublier le risque de grossesse. Même sans éjaculation ! Il faut utiliser des moyens de contraceptions.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 14,
            etat = None,
            texte="Mauvaise réponse - Dépistage tardif du VIH - Un test de dépistage du VIH doit être réalisé au plus vite afin de prendre le traitement qui correspond. Il peut exister de graves conséquences si le virus se développe sans que tu prennes de traîtement.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 15,
            etat = None,
            texte="Bonne réponse - Accessibilité des dépistages - En effet, certains tests sont très rapides, gratuits et faciles d'accès, tout en conservant ton anonymat.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 16,
            etat = None,
            texte="Mauvaise réponse - Réagir rapidement et calmement - A propos des IST, il est possible de se tester plusieurs semaines après l'évènement. Pour le risque de grossesse, il est possible de réagir immédiatement avec une pillule du lendemain ou effectuer un test de grosses dans les semaines qui suivent. L'avortement est toujours envisageable plusieurs semaines après l'acte.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 17,
            etat = None,
            texte="Bonne réponse - Tomber enceinte sans éjaculation - Les spermatozoïdes ont une durée de vie de 4 jours. Ils peuvent être stockés dans l'urètre et sortir avec le liquide pré-séminal.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 18,
            etat = None,
            texte="Mauvaise réponse - Lieu de dépistage pour le VIH - Plusieurs IST existent, dont le VIH. Il est la cause du SIDA. Il peut être dépisté facilement via des différents tests tout en restant anonyme. Un exemple de cela étant le TROD.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 19,
            etat = None,
            texte="Bonne réponse - Accessibilité de l'informations - Très bonne solution, il est important de s'informer auprès de personnes ou de site fiables.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 20,
            etat = None,
            texte="Mauvaise réponse - Pilule du lendemain - Même s'il est légal en France, l'avortement n'est pas la première solution à envisager. En effet, la pilule du lendemain se procure facilement à la pharmacie si elle est ouverte ou à la pharmacie de garde. Attention, à ne pas en abuser.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        Carte(
            id = 21,
            etat = None,
            texte="Bonne réponse - Achat test de grossesse - Il existe de nombreux endroits où se procurer un test de grossesse. Supermarché, pharmacie, association. Les spécialistes de santé peuvent te conseiller et te rassurer sur ce sujet.", 
            previewGauche=None, 
            previewDroite=None, 
            gauche = None, 
            droit = None, 
            explicGauche = None, 
            explicDroit = None
        ),
        
         

    ]
    with Session(main.Engine) as session:
        