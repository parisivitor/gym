import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings


class ExerciseModel(settings.DBBaseModel):
    __tablename__ = 'exercise'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    example = Column(String(250))

    uuid_exercise_type = Column(UUID(as_uuid=True), ForeignKey("exercise_type.uuid"), nullable=False)
    exercise_type = relationship("ExerciseTypeModel")

