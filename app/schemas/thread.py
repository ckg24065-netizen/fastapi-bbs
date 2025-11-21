from pydantic import BaseModel
from datetime import datetime 

#ThreadBase:共通部分(title)
class ThreadBase(BaseModel):
    title: str

#ThreadCreate(ThreadBaseを継承):新規作成時に使う(まだidは無い)
class ThreadCreate(ThreadBase):
    pass

#ThreadResponse(ThreadBaseを継承):一覧を返す(idがある)
class ThreadResponse(ThreadBase):
    id: int
    created_at:datetime