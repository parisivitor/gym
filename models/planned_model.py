import uuid

from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings

from models.planned_train_association import planned_train_association

class Planned(settings.DBBaseModel):
    __tablename__ = 'planned'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    goal = Column(String(50), nullable=False)
    description = Column(String(50))
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    uuid_person = Column(UUID(as_uuid=True), ForeignKey("person.uuid"), nullable=False)
    person = relationship("PersonModel", back_populates="planned", lazy="select")

    train = relationship("TrainModel", secondary=planned_train_association, back_populates="planned", lazy='select')

    # is_teacher = Column(Boolean, nullable=False, default=False)
    # uuid_teacher = Column(UUID(as_uuid=True), ForeignKey("empregador.uuid"))
    # teacher = relationship("EmpregadorModel", back_populates="colaboradores", lazy="select")
    #
    # uuid_address = Column(UUID(as_uuid=True), ForeignKey("empregador.uuid"), nullable=False)
    # teacher = relationship("EmpregadorModel", back_populates="colaboradores", lazy="select")

