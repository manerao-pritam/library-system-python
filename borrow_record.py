from datetime import datetime
from typing import Optional


class BorrowRecord:
    def __init__(self, member_id: str, item_title: str):
        self.member_id = member_id
        self.item_title = item_title
        self.borrow_date = datetime.now()
        self.return_date: Optional[datetime] = None

    def is_active(self) -> bool:
        return self.return_date == None

    def __str__(self) -> str:
        return f'BorrowRecord(Member={self.member_id}, Item={self.item_title}), Borrowed={self.borrow_date}, Returned={self.return_date}'