# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='SawDemo',
  syntax='proto3',
  serialized_pb=_b('\n\x11transaction.proto\x12\x07SawDemo\"\xeb\x02\n\x07Payload\x12\'\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x17.SawDemo.Payload.Action\x12/\n\rcreateAccount\x18\x02 \x01(\x0b\x32\x18.SawDemo.Payload.Account\x12+\n\x08transact\x18\x03 \x01(\x0b\x32\x19.SawDemo.Payload.Transact\x12\x16\n\x0eissueTimestamp\x18\x04 \x01(\t\x1a&\n\x07\x41\x63\x63ount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x1ag\n\x08Transact\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x03\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.SawDemo.Payload.Transact.Type\"\x1d\n\x04Type\x12\n\n\x06\x43REDIT\x10\x00\x12\t\n\x05\x44\x45\x42IT\x10\x01\"0\n\x06\x41\x63tion\x12\x0b\n\x07\x41\x43\x43OUNT\x10\x00\x12\x0c\n\x08TRANSACT\x10\x01\x12\x0b\n\x07\x42\x41LANCE\x10\x02\x62\x06proto3')
)



_PAYLOAD_TRANSACT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='SawDemo.Payload.Transact.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREDIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBIT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=315,
  serialized_end=344,
)
_sym_db.RegisterEnumDescriptor(_PAYLOAD_TRANSACT_TYPE)

_PAYLOAD_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='SawDemo.Payload.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALANCE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=346,
  serialized_end=394,
)
_sym_db.RegisterEnumDescriptor(_PAYLOAD_ACTION)


_PAYLOAD_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='SawDemo.Payload.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SawDemo.Payload.Account.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='SawDemo.Payload.Account.email', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=239,
)

_PAYLOAD_TRANSACT = _descriptor.Descriptor(
  name='Transact',
  full_name='SawDemo.Payload.Transact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='SawDemo.Payload.Transact.amount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='SawDemo.Payload.Transact.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PAYLOAD_TRANSACT_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=344,
)

_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='SawDemo.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='SawDemo.Payload.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createAccount', full_name='SawDemo.Payload.createAccount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transact', full_name='SawDemo.Payload.transact', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issueTimestamp', full_name='SawDemo.Payload.issueTimestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PAYLOAD_ACCOUNT, _PAYLOAD_TRANSACT, ],
  enum_types=[
    _PAYLOAD_ACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=394,
)

_PAYLOAD_ACCOUNT.containing_type = _PAYLOAD
_PAYLOAD_TRANSACT.fields_by_name['type'].enum_type = _PAYLOAD_TRANSACT_TYPE
_PAYLOAD_TRANSACT.containing_type = _PAYLOAD
_PAYLOAD_TRANSACT_TYPE.containing_type = _PAYLOAD_TRANSACT
_PAYLOAD.fields_by_name['action'].enum_type = _PAYLOAD_ACTION
_PAYLOAD.fields_by_name['createAccount'].message_type = _PAYLOAD_ACCOUNT
_PAYLOAD.fields_by_name['transact'].message_type = _PAYLOAD_TRANSACT
_PAYLOAD_ACTION.containing_type = _PAYLOAD
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(

  Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
    DESCRIPTOR = _PAYLOAD_ACCOUNT,
    __module__ = 'transaction_pb2'
    # @@protoc_insertion_point(class_scope:SawDemo.Payload.Account)
    ))
  ,

  Transact = _reflection.GeneratedProtocolMessageType('Transact', (_message.Message,), dict(
    DESCRIPTOR = _PAYLOAD_TRANSACT,
    __module__ = 'transaction_pb2'
    # @@protoc_insertion_point(class_scope:SawDemo.Payload.Transact)
    ))
  ,
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:SawDemo.Payload)
  ))
_sym_db.RegisterMessage(Payload)
_sym_db.RegisterMessage(Payload.Account)
_sym_db.RegisterMessage(Payload.Transact)


# @@protoc_insertion_point(module_scope)
