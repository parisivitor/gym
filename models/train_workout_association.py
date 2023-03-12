from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, Table


from core.configs import settings

train_workout_association = Table(
    "train_workout",
    settings.DBBaseModel.metadata,
    Column("uuid_train", ForeignKey("train.uuid"), primary_key=True),
    Column("uuid_workout", ForeignKey("workout.uuid"), primary_key=True)
)
