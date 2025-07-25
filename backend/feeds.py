from schemas import FeedResponse, FeedEntry
from models import Feed 
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from typing import List

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
def get_all_feedings(session: Session = Depends(get_session)):
    try:
        feeds = session.exec(select(Feed)).all()
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
