
from sqlite3 import Connection as SqliteConnection

from src.models.sqlite.repos.interfaces.products_repos import ProductsReposInterface

class ProductsRepo(ProductsReposInterface):
  def __init__(self, conn:SqliteConnection) -> None:
    self.__conn = conn

  def find_by_name(self, name:str) -> tuple:
    cursor = self.__conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
    return cursor.fetchone()
  
  def insert_product(self,name: str, price: float,quantity:int) -> None:
    cursor = self.__conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    self.__conn.commit()