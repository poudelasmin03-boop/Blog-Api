from sqlalchemy import Column,Integer,String,VARCHAR,DateTime
from database.db import Base
from datetime import timezone,timedelta,datetime

class Blog(Base):
  __tablename__ = "blogtable"
  blog_id = Column(Integer,primary_key=True)
  title =Column(VARCHAR(2000),nullable=False)
  description = Column(VARCHAR(2000),nullable=False)
  content = Column(VARCHAR(2000),nullable=False)
  create_at = Column(DateTime,default=datetime.now)