import uuid

from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings

from models.planned_train_association import planned_train_association
from models.train_workout_association import train_workout_association
from models.train_category_type_association import train_category_type_association

class TrainModel(settings.DBBaseModel):
    __tablename__ = 'train'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(256))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    planned = relationship("PlannedModel", secondary=planned_train_association, back_populates="train", lazy='select')
    workouts = relationship("WorkoutModel", secondary=train_workout_association, back_populates="train", lazy='select')
    category_types = relationship("CategoryTypeModel", secondary=train_category_type_association, back_populates="train", lazy='select')



