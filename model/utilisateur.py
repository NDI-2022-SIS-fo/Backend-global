from sqlalchemy import Column, String
from sqlalchemy.orm import Session

import main

class Utilisateur(main.Base):
    __tablename__ = "Utilisateur"

    id = Column(String)
    nom = Column(String)


if __name__ == "__main__":
    main.Base.metadata.create_all(main.Engine)
    
    utilisateurs = [
        {"id": "1", "nom": "Gérard"},
        {"id": "2", "nom": "Clément"},
        {"id": "3", "nom": "Gabriel"},
    ]

    with Session(main.Engine) as session:
        for utilisateur in utilisateurs:
            session.add(utilisateur)
        session.commit()