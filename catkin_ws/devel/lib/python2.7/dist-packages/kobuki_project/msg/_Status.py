# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kobuki_project/Status.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Status(genpy.Message):
  _md5sum = "e2b13e0be7f646a991aebf8dd021b595"
  _type = "kobuki_project/Status"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 x     # X position
float32 y     # Y position
bool left     # left bumper
bool front    # front bumper
bool right    # right bumper
uint32 power  # power system state: 0: unplugged, 1: plugged to adapter, 2: plugged to dock, 3: charged, 4: battery_low, 5: battery_critical 
"""
  __slots__ = ['x','y','left','front','right','power']
  _slot_types = ['float32','float32','bool','bool','bool','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y,left,front,right,power

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Status, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.left is None:
        self.left = False
      if self.front is None:
        self.front = False
      if self.right is None:
        self.right = False
      if self.power is None:
        self.power = 0
    else:
      self.x = 0.
      self.y = 0.
      self.left = False
      self.front = False
      self.right = False
      self.power = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2f3BI().pack(_x.x, _x.y, _x.left, _x.front, _x.right, _x.power))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 15
      (_x.x, _x.y, _x.left, _x.front, _x.right, _x.power,) = _get_struct_2f3BI().unpack(str[start:end])
      self.left = bool(self.left)
      self.front = bool(self.front)
      self.right = bool(self.right)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2f3BI().pack(_x.x, _x.y, _x.left, _x.front, _x.right, _x.power))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 15
      (_x.x, _x.y, _x.left, _x.front, _x.right, _x.power,) = _get_struct_2f3BI().unpack(str[start:end])
      self.left = bool(self.left)
      self.front = bool(self.front)
      self.right = bool(self.right)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f3BI = None
def _get_struct_2f3BI():
    global _struct_2f3BI
    if _struct_2f3BI is None:
        _struct_2f3BI = struct.Struct("<2f3BI")
    return _struct_2f3BI
