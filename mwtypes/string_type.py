import jsonable
import jsonable.instance


class StringType(str, jsonable.Type):

    def __new__(cls, string_inst_or_doc, *args, **kwargs):
        if isinstance(string_inst_or_doc, cls):
            inst = string_inst_or_doc
            return inst
        elif isinstance(string_inst_or_doc, dict):
            doc = string_inst_or_dict
            return cls.from_json(doc)
        else:
            string = string_inst_or_doc
            inst = super().__new__(cls, string)
            inst.initialize(string, *args, **kwargs)
            return inst

    def to_json(self):
        doc = super().to_json()
        doc['*'] = str.__str__(self)
        return doc

    @classmethod
    def from_json(cls, doc):
        return cls(doc['*'], **{k: v for k, v in doc.items() if k != "*"})

    def __str__(self):
        return str.__str__(self)

    def __repr__(self):
        return jsonable.instance.simple_repr(
            [self.__class__.__name__],
            str.__str__(self),
            ordered_kwargs=jsonable.instance.slot_items(self)
        )
