from dataclasses import dataclass
from datetime import datetime
from typing import  List
from models.mail_box import MailBox

@dataclass
class Alias:
    id: int
    email: str
    pinned: bool
    creation_date: datetime
    creation_timestamp: int
    disable_pgp: bool
    enabled: bool
    latest_activity: datetime
    mailbox: MailBox
    mailboxes: List[MailBox]
    name: str
    nb_block: int
    nb_forward: int
    nb_reply: int
    note: str
    support_pgp: bool

