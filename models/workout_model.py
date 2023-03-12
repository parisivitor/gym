import uuid

from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings

from models.train_workout_association import train_workout_association

class WorkoutModel(settings.DBBaseModel):
    __tablename__ = 'workout'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    repeats = Column(String(10), nullable=False)
    measure = Column(String(10), nullable=False)
    rest_time = Column(String(10), nullable=False)
    description = Column(String(256))
    cadence = Column(String(5))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    uuid_exercise = Column(UUID(as_uuid=True), ForeignKey("exercise.uuid"), nullable=False)
    exercise = relationship("ExerciseModel")

    uuid_measure_type = Column(UUID(as_uuid=True), ForeignKey("measure_type.uuid"), nullable=False)
    measure_type = relationship("MeasureTypeModel")

    uuid_execution_type = Column(UUID(as_uuid=True), ForeignKey("execution_type.uuid"), nullable=False)
    execution_type = relationship("ExecutionTypeModel")

    train = relationship("TrainModel", secondary=train_workout_association, back_populates="workouts", lazy='select')



