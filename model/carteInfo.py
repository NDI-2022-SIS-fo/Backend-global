from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

import main
from etat import Etat

class CarteInfo(main.Base):
    __tablename__ = "cartes"

    id = Column(Integer, primary_key = True)
    texte = Column(String)

if __name__ == "__main__":
    main.Base.metadata.create_all(main.Engine)
    carteInfo = CarteInfo(texte='texte Explicatif')
    with Session(main.Engine) as session:
        session.add(carteInfo)
        session.commit()