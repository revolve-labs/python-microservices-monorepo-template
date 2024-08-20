from typing import Optional
from uuid import uuid4

from pydantic import UUID4, Field

from app.core.schemas.base import Base


class SampleObject(Base):
    id: UUID4 = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None


class SampleRequest(Base):
    obj: SampleObject


class SampleResponse(Base):
    obj: SampleObject
