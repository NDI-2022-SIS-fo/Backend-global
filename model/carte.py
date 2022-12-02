from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import Session

import main
from etat import Etat

class Carte(main.Base):
    __tablename__ = "cartes"

    id = Column(Integer, primary_key = True)
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
    carte = Carte(etat = Etat.BASE, texte='pouet', previewGauche='NO', previewDroite='YE', gauche = 2, droit = 3, eplicGauche = 1, eplicDroit = 2)
    with Session(main.Engine) as session:
        session.add(carte)
        session.commit()