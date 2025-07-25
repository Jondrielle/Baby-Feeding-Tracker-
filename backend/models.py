from sqlmodel import SQLModel, Field
from datetime import datetime
from enums import FeedingMethod
from typing import Optional 

class Feed(SQLModel, table= True):
	id: int | None= Field(default=None, primary_key=True)
	time: datetime
	amount_ml: Optional[float] = Field(default = None,gt=0,le=1000)
	amount_oz: Optional[float] = Field(default = None,gt=0,le=100)
	method: FeedingMethod
	notes: Optional[str] = Field(default=None, max_length=250)