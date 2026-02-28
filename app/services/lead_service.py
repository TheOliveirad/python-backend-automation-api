from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException, status

from app.models.lead import Lead
from app.schemas import LeadCreate


class LeadService:
    @staticmethod
    def create_lead(db: Session, payload: LeadCreate) -> Lead:
        lead = Lead(
            full_name=payload.full_name,
            email=payload.email,
            company=payload.company,
            message=payload.message,
            source=payload.source,
        )

        db.add(lead)

        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Lead with this email already exists.",
            )

        db.refresh(lead)
        return lead

    @staticmethod
    def list_leads(db: Session, limit: int = 50, offset: int = 0):
        total = db.scalar(select(func.count()).select_from(Lead))
        stmt = select(Lead).offset(offset).limit(limit)
        results = db.scalars(stmt).all()
        return total, results