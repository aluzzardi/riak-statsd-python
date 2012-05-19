from .transport import RiakStatsdTransportProxy


def create_proxy(transport_class, stats):
    class TransportClass(RiakStatsdTransportProxy):
        _stats = stats
        _transport_class = transport_class
    return TransportClass
