import redis


def next_message(conn: redis.Redis):
    message = conn.srandmember('message:created')
    if message is None:
        return message
    print('from: %s' % conn.hget(message, 'author'))
    print('to: %s' % conn.hget(message, 'target'))
    print('')
    print(conn.hget(message, 'text'), flush=True)
    return message


def mark_as_spam(conn: redis.Redis, msg: str):
    author = conn.hget(msg, 'author')
    pipe = conn.pipeline()
    pipe.hset(msg, 'status', 'spam')
    pipe.zincrby('user:spam', 1, author)
    pipe.smove('message:created', 'message:spam', msg)
    pipe.publish('message:spam:event', msg)
    pipe.execute()


def deliver(conn: redis.Redis, msg: str):
    pipe = conn.pipeline()
    pipe.hset(msg, 'status', 'delivered')
    pipe.smove('message:created', 'message:delivered', msg)
    pipe.execute()
