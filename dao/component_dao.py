from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from sqlalchemy.engine import Engine


class ComponentDAO:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.metadata = MetaData()
        self.table = Table(
            "components",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String, nullable=False),
            Column("unit", String, nullable=False),
            Column("qty", Integer, nullable=False, default=0),
        )
        self.metadata.create_all(engine)

    def insert(self, dto: dict) -> int:
        with self.engine.begin() as conn:
            result = conn.execute(self.table.insert().values(**dto))
            return result.inserted_primary_key[0]

    def select_all(self) -> list[dict]:
        with self.engine.begin() as conn:
            result = conn.execute(select(self.table))
            return [dict(row._mapping) for row in result]

    def update(self, pk: int, dto: dict) -> int:
        with self.engine.begin() as conn:
            result = conn.execute(
                self.table.update().where(self.table.c.id == pk).values(**dto)
            )
            return result.rowcount

    def delete(self, pk: int) -> int:
        with self.engine.begin() as conn:
            result = conn.execute(self.table.delete().where(self.table.c.id == pk))
            return result.rowcount
