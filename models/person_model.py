from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

from core.configs import settings


class PersonModel(settings.DBBaseModel):
    __tablename__ = 'person'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)
    celphone = Column(String(11), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    # is_student = Column(Boolean, nullable=False, default=False)
    # uuid_student = Column(UUID(as_uuid=True), ForeignKey("empregador.uuid"))
    # student = relationship("EmpregadorModel", back_populates="colaboradores", lazy="select")
    #
    # is_teacher = Column(Boolean, nullable=False, default=False)
    # uuid_teacher = Column(UUID(as_uuid=True), ForeignKey("empregador.uuid"))
    # teacher = relationship("EmpregadorModel", back_populates="colaboradores", lazy="select")
    #
    # uuid_address = Column(UUID(as_uuid=True), ForeignKey("empregador.uuid"), nullable=False)
    # teacher = relationship("EmpregadorModel", back_populates="colaboradores", lazy="select")

