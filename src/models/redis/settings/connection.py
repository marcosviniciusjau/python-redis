from redis import Redis

class RedisConnHandler:
  def __init__(self)->None:
    self.__redis_conn= None

  def connect(self) -> Redis:
    redis_conn = Redis(host="localhsot", port=6379, db=0)
    self.__redis_conn = redis_conn
    return redis_conn
  
  def get_conn(self) -> Redis:
    return self.__redis_conn