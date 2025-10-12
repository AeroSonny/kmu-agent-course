from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

class QAState(BaseModel):

    question: str = Field(...,
                          description="사용자가 입력한 질문")
    answer: Optional[str] = Field(None,
                                  description="사용자가 입력한 질문에 대한 답변.")
    flag: bool = Field(..., 
                       description="웹 검색이 필요한지 여부")
    context: Optional[List[Dict[str, Any]]] = Field(None,
                                                   description="질문에 대한 답변을 생성하기 위해 검색된 문서의 컨텍스트.")
