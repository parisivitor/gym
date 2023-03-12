from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, Table


from core.configs import settings

planned_train_association = Table(
    "planned_train",
    settings.DBBaseModel.metadata,
    Column("uuid_planned", ForeignKey("planned.uuid"), primary_key=True),
    Column("uuid_train", ForeignKey("train.uuid"), primary_key=True)
)
