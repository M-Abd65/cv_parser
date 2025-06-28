# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, LargeBinary
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class CVInfo(Base):
    __tablename__ = 'cv_info'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String)
    datebirth = Column(Date)

    cv_content = Column(LargeBinary, nullable=True)

    skills = relationship("Skill", back_populates="cv_info")
    languages = relationship("Language", back_populates="cv_info")
    experiences = relationship("Experience", back_populates="cv_info")
    educations = relationship("Education", back_populates="cv_info")


class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(String)
    cv_id = Column(Integer, ForeignKey('cv_info.id'))

    cv_info = relationship("CVInfo", back_populates="skills")


class Language(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(String)
    cv_id = Column(Integer, ForeignKey('cv_info.id'))

    cv_info = relationship("CVInfo", back_populates="languages")


class Experience(Base):
    __tablename__ = 'experiences'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    company = Column(String)
    date_start = Column(Date)
    date_end = Column(Date)
    cv_id = Column(Integer, ForeignKey('cv_info.id'))

    cv_info = relationship("CVInfo", back_populates="experiences")


class Education(Base):
    __tablename__ = 'educations'
    id = Column(Integer, primary_key=True)
    degree = Column(String)
    institution = Column(String)
    date_start = Column(Date)
    date_end = Column(Date)
    cv_id = Column(Integer, ForeignKey('cv_info.id'))

    cv_info = relationship("CVInfo", back_populates="educations")
