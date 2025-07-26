from schemas import FeedResponse, FeedEntry
from models import Feed 
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from database import get_session
from enums import FeedingMethod
from datetime import datetime, date
from typing import List, Optional

router = APIRouter()


@router.post("/feeding", response_model= FeedResponse, status_code = 201)
def create_feed(feed: FeedEntry, session: Session = Depends(get_session)):
    try:
        db_feed = Feed(**feed.dict())
        session.add(db_feed)
        session.commit()
        session.refresh(db_feed)
        return db_feed
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code = 400, detail = f"Error with creating feed entry: {e}")

@router.get("/feedings", response_model=List[FeedResponse])
def get_all_feedings(
    method: Optional[FeedingMethod] = Query(None),
    ml: Optional[float] = Query(None, gt=0),
    oz: Optional[float] = Query(None, gt=0),
    date_only: Optional[date] = Query(None),
    session: Session = Depends(get_session)):
    try:
        query = select(Feed)

        if method:
            query = query.where(Feed.method == method)
        if ml:
            query = query.where(Feed.amount_ml != None).where(Feed.amount_ml >= ml)
        if oz:
            query = query.where(Feed.amount_oz != None).where(Feed.amount_oz >= oz)
        if date_only:
            start_dt = datetime.combine(date_only, datetime.min.time())
            end_dt = datetime.combine(date_only, datetime.max.time())
            query = query.where(Feed.time >= start_dt, Feed.time <= end_dt)

        feeds = session.exec(query).all()
        if not feeds:
            raise HTTPException(status_code=404, detail="No feed entries found")

        return feeds
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@router.get("/feedings/{feed_id}", response_model = FeedResponse)
def get_feed_by_id(feed_id: int, session: Session = Depends(get_session)):
    feed = session.get(Feed, feed_id)
    if not feed:
        raise HTTPException(status_code=404, detail = "Feed entry not found")
    return feed

@router.delete("/feedings/{feed_id}", status_code=204)
def delete_feed_entry(feed_id: int, session: Session = Depends(get_session)):
    feed = session.get(Feed, feed_id)
    if not feed:
        raise HTTPException(status_code=404, detail="No feed entries found")
    
    session.delete(feed)
    session.commit()
    return {"detail": "Feed entry deleted"}

@router.delete("/feedings/", status_code=204)
def delete_all_feed_entries(session: Session = Depends(get_session)):
    feedings = session.exec(select(Feed)).all()
    if not feedings:
        raise HTTPException(status_code=404, detail="No feed entries to delete")
    
    for feed in feedings:
        session.delete(feed)

    session.commit()
    return {"detail": "All feed entries deleted"}
