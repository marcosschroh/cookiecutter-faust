import faust


class PageView(faust.Record):
    id: int
    user: str
