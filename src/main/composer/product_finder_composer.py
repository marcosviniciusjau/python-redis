from src.main.server.server_settings import redis_connection, sqlite_connection
from src.models.redis.repos.redis_repos import RedisRepo
from src.models.sqlite.repos.products_repos import ProductsRepo
from src.data.product_finder import ProductFinder
def product_finder_composer():
  redis_conn = redis_connection.get_conn()
  sqlite_conn = sqlite_connection.get_connection()

  redis_repo = RedisRepo(redis_conn)
  products_repo = ProductsRepo(sqlite_conn)

  return ProductFinder(redis_repo, products_repo)