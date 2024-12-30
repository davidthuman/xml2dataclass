
from dataclasses import dataclass

### Data Structures ###

@dataclass
class FieldLite:

    name: str
    type_hint: str

    def to_py_str(self):
        return f"{self.name}: {self.type_hint}"

@dataclass
class DataClass:

    name: str
    attributes: list[FieldLite]
    fields: list[FieldLite]

    def to_py_str(self):
  
        fields_py_str = ""

        for field in [*self.attributes, *self.fields]:
      
            fields_py_str += "    " + field.to_py_str() + "\n"
   
        py_str = f"""\
@dataclass
class {self.name}:

{fields_py_str}
"""
        return py_str