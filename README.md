Transport proxy for instrumenting Riak clients
==============================================

riak-statsd-python is a tiny transport proxy to instrument Riak clients written in Python.

Request counters as well as response times are sent to statsd for instrumentation.

Usage
-----
```python

import riak
import riak_statsd

stats = statsd.StatsClient()

db = riak.RiakClient('localhost', 1234,
        transport_class=riak_statsd.create_proxy(riak.RiakHttpTransport, stats))

```
