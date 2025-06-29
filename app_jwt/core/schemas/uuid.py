from pydantic import BaseModel, Field
import uuid as uu

class UUIDModel(BaseModel):
    uuid: uu.UUID = Field(default_factory=uu.uuid4)