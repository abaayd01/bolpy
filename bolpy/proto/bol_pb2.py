# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bolpy/proto/bol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bolpy/proto/bol.proto',
  package='bolproto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x62olpy/proto/bol.proto\x12\x08\x62olproto\"H\n\x16PriceEvaluationRequest\x12\x14\n\x0c\x63urrentPrice\x18\x01 \x01(\x02\x12\x18\n\x10historicalPrices\x18\x02 \x03(\x02\"\xad\x01\n\x17PriceEvaluationResponse\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x17\n\x0f\x65valuationPrice\x18\x02 \x01(\x02\x12\x17\n\x0ftargetExitPrice\x18\x03 \x01(\x02\x12\x15\n\rstopLossPrice\x18\x04 \x01(\x02\x12\x10\n\x08\x62olUpper\x18\x05 \x01(\x02\x12\x10\n\x08\x62olLower\x18\x06 \x01(\x02\x12\x15\n\rmovingAverage\x18\x07 \x01(\x02\x32h\n\x0ePriceEvaluator\x12V\n\rEvaluatePrice\x12 .bolproto.PriceEvaluationRequest\x1a!.bolproto.PriceEvaluationResponse\"\x00\x62\x06proto3')
)




_PRICEEVALUATIONREQUEST = _descriptor.Descriptor(
  name='PriceEvaluationRequest',
  full_name='bolproto.PriceEvaluationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentPrice', full_name='bolproto.PriceEvaluationRequest.currentPrice', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='historicalPrices', full_name='bolproto.PriceEvaluationRequest.historicalPrices', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=35,
  serialized_end=107,
)


_PRICEEVALUATIONRESPONSE = _descriptor.Descriptor(
  name='PriceEvaluationResponse',
  full_name='bolproto.PriceEvaluationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='bolproto.PriceEvaluationResponse.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evaluationPrice', full_name='bolproto.PriceEvaluationResponse.evaluationPrice', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetExitPrice', full_name='bolproto.PriceEvaluationResponse.targetExitPrice', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopLossPrice', full_name='bolproto.PriceEvaluationResponse.stopLossPrice', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bolUpper', full_name='bolproto.PriceEvaluationResponse.bolUpper', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bolLower', full_name='bolproto.PriceEvaluationResponse.bolLower', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movingAverage', full_name='bolproto.PriceEvaluationResponse.movingAverage', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=110,
  serialized_end=283,
)

DESCRIPTOR.message_types_by_name['PriceEvaluationRequest'] = _PRICEEVALUATIONREQUEST
DESCRIPTOR.message_types_by_name['PriceEvaluationResponse'] = _PRICEEVALUATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PriceEvaluationRequest = _reflection.GeneratedProtocolMessageType('PriceEvaluationRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRICEEVALUATIONREQUEST,
  '__module__' : 'bolpy.proto.bol_pb2'
  # @@protoc_insertion_point(class_scope:bolproto.PriceEvaluationRequest)
  })
_sym_db.RegisterMessage(PriceEvaluationRequest)

PriceEvaluationResponse = _reflection.GeneratedProtocolMessageType('PriceEvaluationResponse', (_message.Message,), {
  'DESCRIPTOR' : _PRICEEVALUATIONRESPONSE,
  '__module__' : 'bolpy.proto.bol_pb2'
  # @@protoc_insertion_point(class_scope:bolproto.PriceEvaluationResponse)
  })
_sym_db.RegisterMessage(PriceEvaluationResponse)



_PRICEEVALUATOR = _descriptor.ServiceDescriptor(
  name='PriceEvaluator',
  full_name='bolproto.PriceEvaluator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=285,
  serialized_end=389,
  methods=[
  _descriptor.MethodDescriptor(
    name='EvaluatePrice',
    full_name='bolproto.PriceEvaluator.EvaluatePrice',
    index=0,
    containing_service=None,
    input_type=_PRICEEVALUATIONREQUEST,
    output_type=_PRICEEVALUATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRICEEVALUATOR)

DESCRIPTOR.services_by_name['PriceEvaluator'] = _PRICEEVALUATOR

# @@protoc_insertion_point(module_scope)
