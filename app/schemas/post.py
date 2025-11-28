from pydantic import BaseModel

class PostBase(BaseModel):
    content: str
    parent_post_id: int | None = None
    
    
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    thread_id: int
    post_number: int
    created_at: str
    