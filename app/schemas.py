from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class LeadCreate(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=255)
    email: EmailStr
    company: Optional[str] = Field(default=None, max_length=255)
    message: Optional[str] = Field(default=None, max_length=2000)
    source: Optional[str] = Field(default=None, max_length=100)


class LeadRead(BaseModel):
    # Pydantic v2 replacement for old `class Config`
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: EmailStr
    company: Optional[str]
    message: Optional[str]
    source: Optional[str]
    created_at: datetime


class LeadListResponse(BaseModel):
    total: int
    items: List[LeadRead]