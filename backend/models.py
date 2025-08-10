
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, HttpUrl, field_validator
class ProductMatch(BaseModel):
    retailer: str
    title: str
    price: Optional[float]
    currency: str = "RM"
    url: HttpUrl
    availability: Optional[str] = None
    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        return " ".join(v.split())
