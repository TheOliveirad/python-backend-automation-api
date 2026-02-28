from __future__ import annotations

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas import LeadCreate, LeadRead, LeadListResponse
from app.services.lead_service import LeadService
from app.logger import get_logger

router = APIRouter(prefix="/leads", tags=["leads"])
log = get_logger(__name__)


@router.post(
    "",
    response_model=LeadRead,
    status_code=status.HTTP_201_CREATED,
)
def create_lead(
    payload: LeadCreate,
    db: Session = Depends(get_db),
) -> LeadRead:
    lead = LeadService.create_lead(db=db, payload=payload)

    log.info(
        f"lead_created id={lead.id} email={lead.email} source={lead.source}"
    )

    return lead


@router.get(
    "",
    response_model=LeadListResponse,
)
def list_leads(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
) -> LeadListResponse:
    total, leads = LeadService.list_leads(
        db=db,
        limit=limit,
        offset=offset,
    )

    return LeadListResponse(
        total=total,
        items=leads,
    )