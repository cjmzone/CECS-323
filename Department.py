from orm_base import Base
from sqlalchemy import Column, Integer, UniqueConstraint, Identity
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Department(Base):
    __tablename__ = "departments"  # Gives SQLAlchemy the name of the table.

    # Department table and variables in 2a-2f
    name: Mapped[str] = mapped_column('name', String(50), nullable=False, primary_key=True)
    abbreviation: Mapped[str] = mapped_column('abbreviation', String(6), nullable=False)
    chairName: Mapped[str] = mapped_column('chair_name', String(80), nullable=False)
    building: Mapped[str] = mapped_column('building', String(10), nullable=False)
    office: Mapped[int] = mapped_column("office", Integer, nullable=False)
    description: Mapped[str] = mapped_column("description", String(80), nullable=False)

    # Four uniqueness constraints asked for in 2g.
    __table_args__ = (UniqueConstraint("abbreviation", name="departments_uk_01"),
                      UniqueConstraint("chair_name", name="departments_uk_02"),
                      UniqueConstraint("building", "office", name="departments_uk_03"),
                      UniqueConstraint("description", name="departments_uk_04"),)

    # Constructor asked for in 2h.
    def __init__(self, name: str, abbreviation: str, chairName: str, building: str, office: int, description: str):
        self.name = name
        self.abbreviation = abbreviation  # Corrected typo here
        self.chairName = chairName
        self.building = building
        self.office = office
        self.description = description

    # __str__ method asked for in 2h.
    def __str__(self):
        return f"Department name: {self.abbreviation} - {self.name}\nChair: {self.chairName}\nOffice: {self.building} - {self.office}\nDescription: {self.description}"
