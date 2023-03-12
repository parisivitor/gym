from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, Table


from core.configs import settings

train_category_type_association = Table(
    "train_category_type",
    settings.DBBaseModel.metadata,
    Column("uuid_train", ForeignKey("train.uuid"), primary_key=True),
    Column("uuid_category_type", ForeignKey("category_type.uuid"), primary_key=True)
)
