from riak.transports.transport import RiakTransport


class RiakStatsdTransportProxy(RiakTransport):
    def __init__(self, *args, **kwargs):
        self._transport = self._transport_class(*args, **kwargs)

    def _instrument(self, name):
        self._stats.incr('riak.{0}.requests'.format(name))
        return self._stats.timer('riak.{0}.response_time'.format(name))

    def ping(self, *args, **kwargs):
        return self._transport.ping(*args, **kwargs)

    def get(self, *args, **kwargs):
        with self._instrument('get'):
            return self._transport.get(*args, **kwargs)

    def put(self, *args, **kwargs):
        with self._instrument('put'):
            return self._transport.put(*args, **kwargs)

    def put_new(self, *args, **kwargs):
        with self._instrument('new'):
            return self._transport.put_new(*args, **kwargs)

    def delete(self, *args, **kwargs):
        with self._instrument('delete'):
            return self._transport.delete(*args, **kwargs)

    def get_buckets(self, *args, **kwargs):
        return self._transport.get_buckets(*args, **kwargs)

    def get_bucket_props(self, *args, **kwargs):
        return self._transport.get_bucket_props(*args, **kwargs)

    def set_bucket_props(self, *args, **kwargs):
        return self._transport.set_bucket_props(*args, **kwargs)

    def mapred(self, *args, **kwargs):
        with self._instrument('mapred'):
            return self._transport.mapred(*args, **kwargs)

    def set_client_id(self, *args, **kwargs):
        return self._transport.set_client_id(*args, **kwargs)

    def get_client_id(self, *args, **kwargs):
        return self._transport.get_client_id(*args, **kwargs)

    def store_file(self, *args, **kwargs):
        with self._instrument('store_file'):
            return self._transport.store_file(*args, **kwargs)

    def get_file(self, *args, **kwargs):
        with self._instrument('get_file'):
            return self._transport.get_file(*args, **kwargs)

    def delete_file(self, *args, **kwargs):
        with self._instrument('delete_file'):
            return self._transport.delete_file(*args, **kwargs)
