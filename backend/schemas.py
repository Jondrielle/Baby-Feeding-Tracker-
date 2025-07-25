import bleach 
from pydantic import BaseModel, Field, model_validator,field_validator
from datetime import datetime, timezone
from enums import FeedingMethod
from typing import Optional 

class FeedEntry(BaseModel):
    time: datetime
    amount_ml: Optional[float] = Field(default = None, le=1000)
    amount_oz: Optional[float] = Field(default = None, le=100)
    method: FeedingMethod
    notes: Optional[str] = Field(default=None, max_length=250)

    @model_validator(mode="after")
    def check_oz_or_ml(self):
        oz = self.amount_oz
        ml = self.amount_ml
        if(oz is not None and oz < 0) or ( ml is not None and ml < 0):
            raise ValueError("Provide postive amounts only")
        if (oz is not None and oz > 0) and (ml is not None and ml > 0):
            raise ValueError("Provide only one amount unit: ml or oz, not both.")
        return self

    @field_validator("notes")
    @classmethod
    def sanitize_notes(cls, v):
        if v is None:
            return v
        cleaned = bleach.clean(v, tags=[], strip=True)
        return cleaned

    @field_validator("time", mode="after")
    @classmethod
    def time_not_in_future(cls, v: datetime):
        print(f"Validator received time: {v} (tzinfo={v.tzinfo})")
        now = datetime.now(timezone.utc)  # aware datetime in UTC

        # Make v aware in UTC if naive
        if v.tzinfo is None:
            v = v.replace(tzinfo=timezone.utc)

        if v > now:
            raise ValueError("Time cannot be in the future")
        return v



class FeedResponse(FeedEntry):
    id: int
    class Config:
        orm_mode = True