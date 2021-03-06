# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: assets.proto

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
  name='assets.proto',
  package='Asset',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x61ssets.proto\x12\x05\x41sset\"_\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x03\x12\x11\n\tpublicKey\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\"\xc2\x01\n\x05Trail\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x11\n\ttxnNumber\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x13\n\x0buserAddress\x18\x04 \x01(\t\x12$\n\x06\x61\x63tion\x18\x06 \x01(\x0e\x32\x14.Asset.Trail.Actions\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\"5\n\x07\x41\x63tions\x12\n\n\x06\x43REDIT\x10\x00\x12\t\n\x05\x44\x45\x42IT\x10\x01\x12\x13\n\x0f\x41\x43\x43OUNT_CREATED\x10\x02\x62\x06proto3')
)



_TRAIL_ACTIONS = _descriptor.EnumDescriptor(
  name='Actions',
  full_name='Asset.Trail.Actions',
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
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_CREATED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=262,
  serialized_end=315,
)
_sym_db.RegisterEnumDescriptor(_TRAIL_ACTIONS)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='Asset.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='Asset.Account.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='Asset.Account.userName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='Asset.Account.balance', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicKey', full_name='Asset.Account.publicKey', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='Asset.Account.email', index=4,
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
  serialized_start=23,
  serialized_end=118,
)


_TRAIL = _descriptor.Descriptor(
  name='Trail',
  full_name='Asset.Trail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='Asset.Trail.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txnNumber', full_name='Asset.Trail.txnNumber', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Asset.Trail.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userAddress', full_name='Asset.Trail.userAddress', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='Asset.Trail.action', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='Asset.Trail.address', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRAIL_ACTIONS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=315,
)

_TRAIL.fields_by_name['action'].enum_type = _TRAIL_ACTIONS
_TRAIL_ACTIONS.containing_type = _TRAIL
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Trail'] = _TRAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'assets_pb2'
  # @@protoc_insertion_point(class_scope:Asset.Account)
  ))
_sym_db.RegisterMessage(Account)

Trail = _reflection.GeneratedProtocolMessageType('Trail', (_message.Message,), dict(
  DESCRIPTOR = _TRAIL,
  __module__ = 'assets_pb2'
  # @@protoc_insertion_point(class_scope:Asset.Trail)
  ))
_sym_db.RegisterMessage(Trail)


# @@protoc_insertion_point(module_scope)
