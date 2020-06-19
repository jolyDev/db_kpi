import redis


def connect():
    return redis.Redis(host='localhost', port=6379, db=0)


def send_message(conn: redis.Redis, token: str, target: str, text: str):
    author = conn.get(token)

    if author is None:
        raise Exception('Failed auth')

    ID = conn.incr('message:id')
    ID = 'message:%s' % ID
    pipe = conn.pipeline()
    pipe.hset(ID, 'target', target)
    pipe.hset(ID, 'author', author)
    pipe.hset(ID, 'text', text)
    pipe.sadd('message:to:%s' % target, ID)
    pipe.sadd('message:from:%s' % author, ID)
    pipe.sadd('message:created', ID)
    pipe.zincrby('user:sent', 1, author)
    pipe.execute()


def print_messages(conn: redis.Redis, token: str):
    if  conn.get(token) is None:
        raise Exception('You are not logged in')

    for message in conn.sinter('message:to:%s' % conn.get(token), 'message:delivered'):
        print(conn.hget(message, 'text'))


def print_message(conn: redis.Redis, msg: str):
    print('from: %s' % str(conn.hget(conn.hget(msg, 'author'), 'username')))
    print('to: %s' % str(conn.hget(conn.hget(msg, 'target'), 'username')))
    print('')
    print(str(conn.hget(msg, 'text')), flush=True)


def get_user(conn: redis.Redis, username: str):
    return conn.hget('user:username', username)


def get_message_stats(conn: redis.Redis, user: str):
    print('created:   ', len(conn.sinter('message:from:%s' % user, 'message:created')))
    print('delivered: ',len(conn.sinter('message:from:%s' % user, 'message:spam')))
    print('spam:      ',len(conn.sinter('message:from:%s' % user, 'message:delivered')))

def register(conn: redis.Redis, username: str):
    if conn.hexists('user:username', username):
        raise Exception('User with name %s already exists' % username)

    ID = conn.incr('user:id')
    if conn.hexists('user:username', username):
        raise Exception('User with name %s already exists' % username)
    pipe = conn.pipeline()
    pipe.hset('user:username', username, 'user:%s' % ID)
    pipe.hset('user:%s' % ID, 'username', username)
    pipe.sadd('user:logged-out', 'user:%s' % ID)
    pipe.execute()

    return 'user:%s' % ID


def login(conn: redis.Redis, username: str):
    user = conn.hget('user:username', username)
    if user is None:
        raise Exception('User does not exist')

    token = 'token:%s' % conn.incr('token:id')
    pipe = conn.pipeline()
    pipe.set(token, user)
    pipe.expire(token, 200)
    pipe.publish('user:event', b'%s:login' % user)
    pipe.execute()
    return token


def logout(conn: redis.Redis, token: str):
    user = conn.get(token)
    if user is None:
        raise Exception('failed auth')

    pipe = conn.pipeline()
    pipe.delete(token)
    pipe.publish('user:event', b'%s:logout' % user)
    pipe.execute()
