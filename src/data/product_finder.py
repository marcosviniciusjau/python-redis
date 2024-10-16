from src.models.redis.repos.interfaces.redis_repos import RedisReposInterface
from src.models.sqlite.repos.interfaces.products_repos import ProductsReposInterface


class ProductFinder:
  def __init__(self,
               redis_repo:RedisReposInterface,
               products_repo: ProductsReposInterface
                ):
    self.__redis_repo = redis_repo
    self.__products_repo = products_repo
  def find_product_by_name(self, name:str):
    return self.__products_repo.find_product_by_name(name)