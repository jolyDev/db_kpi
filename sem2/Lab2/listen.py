import redis


def listen(conn: redis.Redis):
    pb = conn.pubsub()
    pb.subscribe(['user:event', 'message:spam:event'])

    print('Listening...')

    for item in pb.listen():
        if item['type'] != 'message':
            continue
        item = item['data']

        if item.startswith(b'message'):
            print('Spam: ', item)
        else:
            if item.startswith(b'user'):
                user = item.split(':')[:2]
            if item.endswith(b'login'):
                print('Logged in')
                conn.sadd('logged-in', user)
            else:
                if item.endswith(b'logout'):
                    print('Logged out')
                    conn.srem('logged-in', user)
