import msgpack
import typing


from faust.serializers import codecs

# Codec example from https://faust.readthedocs.io/en/latest/userguide/models.html#codecs

class raw_msgpack(codecs.Codec):
    
    def _dumps(self, obj: typing.Any) -> bytes:
        return msgpack.dumps(obj)

    def _loads(self, s: bytes) -> typing.Any:
        return msgpack.loads(s)


def msgpack() -> codecs.Codec:
    return raw_msgpack() | codecs.binary()


