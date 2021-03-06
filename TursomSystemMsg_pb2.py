# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TursomSystemMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TursomSystemMsg.proto',
  package='cn.tursom.im.protobuf',
  syntax='proto3',
  serialized_options=b'B\017TursomSystemMsgH\001Z\024./tursom_im_protobuf',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15TursomSystemMsg.proto\x12\x15\x63n.tursom.im.protobuf\" \n\x0eListenLiveRoom\x12\x0e\n\x06roomId\x18\x01 \x01(\t\"\x15\n\x13ListLiveRoomRequest\"3\n\x14ListLiveRoomResponse\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0e\n\x06roomId\x18\x02 \x03(\t\"@\n\x0f\x41\x64\x64MailReceiver\x12\x10\n\x08receiver\x18\x01 \x01(\t\x12\x0b\n\x03\x61ll\x18\x02 \x01(\x08\x12\x0e\n\x06roomId\x18\x03 \x03(\t\"T\n\x16GetLiveDanmuRecordList\x12\r\n\x05reqId\x18\x01 \x01(\t\x12\x0e\n\x06roomId\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x05\x12\r\n\x05limit\x18\x04 \x01(\x05\"v\n\x19ReturnLiveDanmuRecordList\x12\r\n\x05reqId\x18\x01 \x01(\t\x12\x0e\n\x06roomId\x18\x02 \x01(\t\x12:\n\nrecordList\x18\x03 \x03(\x0b\x32&.cn.tursom.im.protobuf.LiveDanmuRecord\":\n\x0fLiveDanmuRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x04\x12\x0c\n\x04stop\x18\x03 \x01(\x04\">\n\x12GetLiveDanmuRecord\x12\r\n\x05reqId\x18\x01 \x01(\t\x12\x19\n\x11liveDanmuRecordId\x18\x02 \x01(\t\"C\n\x15ReturnLiveDanmuRecord\x12\r\n\x05reqId\x18\x01 \x01(\t\x12\r\n\x05\x65xist\x18\x02 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"Z\n\x0fLiveRecordReady\x12\r\n\x05reqId\x18\x01 \x01(\t\x12\x0e\n\x06roomId\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0c\n\x04stop\x18\x04 \x01(\x03\x12\x0b\n\x03url\x18\x05 \x01(\tB)B\x0fTursomSystemMsgH\x01Z\x14./tursom_im_protobufb\x06proto3'
)




_LISTENLIVEROOM = _descriptor.Descriptor(
  name='ListenLiveRoom',
  full_name='cn.tursom.im.protobuf.ListenLiveRoom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomId', full_name='cn.tursom.im.protobuf.ListenLiveRoom.roomId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=80,
)


_LISTLIVEROOMREQUEST = _descriptor.Descriptor(
  name='ListLiveRoomRequest',
  full_name='cn.tursom.im.protobuf.ListLiveRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=103,
)


_LISTLIVEROOMRESPONSE = _descriptor.Descriptor(
  name='ListLiveRoomResponse',
  full_name='cn.tursom.im.protobuf.ListLiveRoomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='cn.tursom.im.protobuf.ListLiveRoomResponse.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomId', full_name='cn.tursom.im.protobuf.ListLiveRoomResponse.roomId', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=156,
)


_ADDMAILRECEIVER = _descriptor.Descriptor(
  name='AddMailReceiver',
  full_name='cn.tursom.im.protobuf.AddMailReceiver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='receiver', full_name='cn.tursom.im.protobuf.AddMailReceiver.receiver', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='all', full_name='cn.tursom.im.protobuf.AddMailReceiver.all', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomId', full_name='cn.tursom.im.protobuf.AddMailReceiver.roomId', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=222,
)


_GETLIVEDANMURECORDLIST = _descriptor.Descriptor(
  name='GetLiveDanmuRecordList',
  full_name='cn.tursom.im.protobuf.GetLiveDanmuRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqId', full_name='cn.tursom.im.protobuf.GetLiveDanmuRecordList.reqId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomId', full_name='cn.tursom.im.protobuf.GetLiveDanmuRecordList.roomId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip', full_name='cn.tursom.im.protobuf.GetLiveDanmuRecordList.skip', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='cn.tursom.im.protobuf.GetLiveDanmuRecordList.limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=308,
)


_RETURNLIVEDANMURECORDLIST = _descriptor.Descriptor(
  name='ReturnLiveDanmuRecordList',
  full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqId', full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecordList.reqId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomId', full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecordList.roomId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recordList', full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecordList.recordList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=428,
)


_LIVEDANMURECORD = _descriptor.Descriptor(
  name='LiveDanmuRecord',
  full_name='cn.tursom.im.protobuf.LiveDanmuRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cn.tursom.im.protobuf.LiveDanmuRecord.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='cn.tursom.im.protobuf.LiveDanmuRecord.start', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop', full_name='cn.tursom.im.protobuf.LiveDanmuRecord.stop', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=430,
  serialized_end=488,
)


_GETLIVEDANMURECORD = _descriptor.Descriptor(
  name='GetLiveDanmuRecord',
  full_name='cn.tursom.im.protobuf.GetLiveDanmuRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqId', full_name='cn.tursom.im.protobuf.GetLiveDanmuRecord.reqId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='liveDanmuRecordId', full_name='cn.tursom.im.protobuf.GetLiveDanmuRecord.liveDanmuRecordId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=490,
  serialized_end=552,
)


_RETURNLIVEDANMURECORD = _descriptor.Descriptor(
  name='ReturnLiveDanmuRecord',
  full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqId', full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecord.reqId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exist', full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecord.exist', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='cn.tursom.im.protobuf.ReturnLiveDanmuRecord.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=621,
)


_LIVERECORDREADY = _descriptor.Descriptor(
  name='LiveRecordReady',
  full_name='cn.tursom.im.protobuf.LiveRecordReady',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqId', full_name='cn.tursom.im.protobuf.LiveRecordReady.reqId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomId', full_name='cn.tursom.im.protobuf.LiveRecordReady.roomId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start', full_name='cn.tursom.im.protobuf.LiveRecordReady.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop', full_name='cn.tursom.im.protobuf.LiveRecordReady.stop', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='cn.tursom.im.protobuf.LiveRecordReady.url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=623,
  serialized_end=713,
)

_RETURNLIVEDANMURECORDLIST.fields_by_name['recordList'].message_type = _LIVEDANMURECORD
DESCRIPTOR.message_types_by_name['ListenLiveRoom'] = _LISTENLIVEROOM
DESCRIPTOR.message_types_by_name['ListLiveRoomRequest'] = _LISTLIVEROOMREQUEST
DESCRIPTOR.message_types_by_name['ListLiveRoomResponse'] = _LISTLIVEROOMRESPONSE
DESCRIPTOR.message_types_by_name['AddMailReceiver'] = _ADDMAILRECEIVER
DESCRIPTOR.message_types_by_name['GetLiveDanmuRecordList'] = _GETLIVEDANMURECORDLIST
DESCRIPTOR.message_types_by_name['ReturnLiveDanmuRecordList'] = _RETURNLIVEDANMURECORDLIST
DESCRIPTOR.message_types_by_name['LiveDanmuRecord'] = _LIVEDANMURECORD
DESCRIPTOR.message_types_by_name['GetLiveDanmuRecord'] = _GETLIVEDANMURECORD
DESCRIPTOR.message_types_by_name['ReturnLiveDanmuRecord'] = _RETURNLIVEDANMURECORD
DESCRIPTOR.message_types_by_name['LiveRecordReady'] = _LIVERECORDREADY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListenLiveRoom = _reflection.GeneratedProtocolMessageType('ListenLiveRoom', (_message.Message,), {
  'DESCRIPTOR' : _LISTENLIVEROOM,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.ListenLiveRoom)
  })
_sym_db.RegisterMessage(ListenLiveRoom)

ListLiveRoomRequest = _reflection.GeneratedProtocolMessageType('ListLiveRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTLIVEROOMREQUEST,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.ListLiveRoomRequest)
  })
_sym_db.RegisterMessage(ListLiveRoomRequest)

ListLiveRoomResponse = _reflection.GeneratedProtocolMessageType('ListLiveRoomResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTLIVEROOMRESPONSE,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.ListLiveRoomResponse)
  })
_sym_db.RegisterMessage(ListLiveRoomResponse)

AddMailReceiver = _reflection.GeneratedProtocolMessageType('AddMailReceiver', (_message.Message,), {
  'DESCRIPTOR' : _ADDMAILRECEIVER,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.AddMailReceiver)
  })
_sym_db.RegisterMessage(AddMailReceiver)

GetLiveDanmuRecordList = _reflection.GeneratedProtocolMessageType('GetLiveDanmuRecordList', (_message.Message,), {
  'DESCRIPTOR' : _GETLIVEDANMURECORDLIST,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.GetLiveDanmuRecordList)
  })
_sym_db.RegisterMessage(GetLiveDanmuRecordList)

ReturnLiveDanmuRecordList = _reflection.GeneratedProtocolMessageType('ReturnLiveDanmuRecordList', (_message.Message,), {
  'DESCRIPTOR' : _RETURNLIVEDANMURECORDLIST,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.ReturnLiveDanmuRecordList)
  })
_sym_db.RegisterMessage(ReturnLiveDanmuRecordList)

LiveDanmuRecord = _reflection.GeneratedProtocolMessageType('LiveDanmuRecord', (_message.Message,), {
  'DESCRIPTOR' : _LIVEDANMURECORD,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.LiveDanmuRecord)
  })
_sym_db.RegisterMessage(LiveDanmuRecord)

GetLiveDanmuRecord = _reflection.GeneratedProtocolMessageType('GetLiveDanmuRecord', (_message.Message,), {
  'DESCRIPTOR' : _GETLIVEDANMURECORD,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.GetLiveDanmuRecord)
  })
_sym_db.RegisterMessage(GetLiveDanmuRecord)

ReturnLiveDanmuRecord = _reflection.GeneratedProtocolMessageType('ReturnLiveDanmuRecord', (_message.Message,), {
  'DESCRIPTOR' : _RETURNLIVEDANMURECORD,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.ReturnLiveDanmuRecord)
  })
_sym_db.RegisterMessage(ReturnLiveDanmuRecord)

LiveRecordReady = _reflection.GeneratedProtocolMessageType('LiveRecordReady', (_message.Message,), {
  'DESCRIPTOR' : _LIVERECORDREADY,
  '__module__' : 'TursomSystemMsg_pb2'
  # @@protoc_insertion_point(class_scope:cn.tursom.im.protobuf.LiveRecordReady)
  })
_sym_db.RegisterMessage(LiveRecordReady)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
