from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import Session

import main
from sexe import Sexe
from phobie import Phobie
from orientation import Orientation

class Personnage(main.Base):
    __tablename__ = "cartes"

    id = Column(Integer, primary_key = True)
    nom = Column(String)
    sexe = Column(Enum(Sexe))
    phobie = Column(Enum(Phobie))
    isTrans = Column(Integer)
    orientation = Column(Enum(Orientation))



if __name__ == "__main__":
    main.Base.metadata.create_all(main.Engine)
    perso = Personnage(nom='pouet', sexe=Sexe.HOMME, phobie=Phobie._, isTrans = 0, orientation = Orientation.HETERO)
    with Session(main.Engine) as session:
        session.add(perso)
        session.commit()