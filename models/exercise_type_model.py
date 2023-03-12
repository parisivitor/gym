import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from core.configs import settings


class ExerciseTypeModel(settings.DBBaseModel):
    __tablename__ = 'exercise_type'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(256))


