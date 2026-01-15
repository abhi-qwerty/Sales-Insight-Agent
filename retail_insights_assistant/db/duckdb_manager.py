import duckdb
import pandas as pd
from config.settings import DUCKDB_TABLE_NAME

class DuckDBManager:
    def __init__(self):
        self.con = duckdb.connect(database=":memory:")

    def register_dataframe(self, df: pd.DataFrame):
        self.con.register(DUCKDB_TABLE_NAME, df)

    def execute(self, sql: str) -> pd.DataFrame:
        return self.con.execute(sql).df()
