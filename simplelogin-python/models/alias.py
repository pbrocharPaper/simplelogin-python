from dataclasses import dataclass

@dataclass
class Alias:
    id: int
    email: str
    pinned: bool

    def __init__(self, alias_data):
        self.creation_date = alias_data.get("creation_date")
        self.creation_timestamp = alias_data.get("creation_timestamp")
        self.disable_pgp = alias_data.get("disable_pgp")
        self.email = alias_data.get("email")
        self.enabled = alias_data.get("enabled")
        self.id = alias_data.get("id")
        self.latest_activity = alias_data.get("latest_activity")
        self.mailbox = alias_data.get("mailbox")
        self.mailboxes = alias_data.get("mailboxes")
        self.name = alias_data.get("name")
        self.nb_block = alias_data.get("nb_block")
        self.nb_forward = alias_data.get("nb_forward")
        self.nb_reply = alias_data.get("nb_reply")
        self.note = alias_data.get("note")
        self.pinned = alias_data.get("pinned")
        self.support_pgp = alias_data.get("support_pgp")
