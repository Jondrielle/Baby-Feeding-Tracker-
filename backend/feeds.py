from schemas import FeedResponse, FeedEntry
from models import Feed 
from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session
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
