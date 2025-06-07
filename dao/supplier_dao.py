from sqlalchemy import MetaData, Table, Column, Integer, String, select
from sqlalchemy.engine import Engine

class SupplierDAO:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.metadata = MetaData()
        self.table = Table(
            "suppliers",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String, nullable=False),
            Column("email", String, nullable=False),
            Column("phone", String),
        )
        self.metadata.create_all(engine)

    def insert(self, dto: dict) -> int:
        with self.engine.begin() as conn:
            res = conn.execute(self.table.insert().values(**dto))
            return res.inserted_primary_key[0]

    def select_all(self) -> list[dict]:
        with self.engine.begin() as conn:
            res = conn.execute(select(self.table))
            return [dict(row._mapping) for row in res]

    def update(self, pk: int, dto: dict) -> int:
        with self.engine.begin() as conn:
            res = conn.execute(
                self.table.update().where(self.table.c.id == pk).values(**dto)
            )
            return res.rowcount

    def delete(self, pk: int) -> int:
        with self.engine.begin() as conn:
            res = conn.execute(self.table.delete().where(self.table.c.id == pk))
            return res.rowcount
