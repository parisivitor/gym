import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.configs import settings

from models.train_category_type_association import train_category_type_association


class CategoryTypeModel(settings.DBBaseModel):
    __tablename__ = 'category_type'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(256))

    train = relationship("TrainModel", secondary=train_category_type_association, back_populates="category_types", lazy='select')

