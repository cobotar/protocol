// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: ar/v1/events.proto

package arv1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type EventType int32

const (
	EventType_EVENT_TYPE_UNSPECIFIED        EventType = 0
	EventType_EVENT_TYPE_TASK_COMPLETE      EventType = 10
	EventType_EVENT_TYPE_TASK_UNDO          EventType = 11
	EventType_EVENT_TYPE_TASK_ASSIGN        EventType = 12
	EventType_EVENT_TYPE_TASK_HIGHLIGHT     EventType = 13
	EventType_EVENT_TYPE_TASK_HELP          EventType = 14
	EventType_EVENT_TYPE_ROBOT_TCP          EventType = 100
	EventType_EVENT_TYPE_ROBOT_JOINT_ANGLES EventType = 101
	EventType_EVENT_TYPE_ROBOT_FORCE_TORQUE EventType = 102
	EventType_EVENT_TYPE_ROBOT_STATE        EventType = 110
	EventType_EVENT_TYPE_ROBOT_PATH         EventType = 120
	EventType_EVENT_TYPE_ROBOT_WAYPOINTS    EventType = 121
)

// Enum value maps for EventType.
var (
	EventType_name = map[int32]string{
		0:   "EVENT_TYPE_UNSPECIFIED",
		10:  "EVENT_TYPE_TASK_COMPLETE",
		11:  "EVENT_TYPE_TASK_UNDO",
		12:  "EVENT_TYPE_TASK_ASSIGN",
		13:  "EVENT_TYPE_TASK_HIGHLIGHT",
		14:  "EVENT_TYPE_TASK_HELP",
		100: "EVENT_TYPE_ROBOT_TCP",
		101: "EVENT_TYPE_ROBOT_JOINT_ANGLES",
		102: "EVENT_TYPE_ROBOT_FORCE_TORQUE",
		110: "EVENT_TYPE_ROBOT_STATE",
		120: "EVENT_TYPE_ROBOT_PATH",
		121: "EVENT_TYPE_ROBOT_WAYPOINTS",
	}
	EventType_value = map[string]int32{
		"EVENT_TYPE_UNSPECIFIED":        0,
		"EVENT_TYPE_TASK_COMPLETE":      10,
		"EVENT_TYPE_TASK_UNDO":          11,
		"EVENT_TYPE_TASK_ASSIGN":        12,
		"EVENT_TYPE_TASK_HIGHLIGHT":     13,
		"EVENT_TYPE_TASK_HELP":          14,
		"EVENT_TYPE_ROBOT_TCP":          100,
		"EVENT_TYPE_ROBOT_JOINT_ANGLES": 101,
		"EVENT_TYPE_ROBOT_FORCE_TORQUE": 102,
		"EVENT_TYPE_ROBOT_STATE":        110,
		"EVENT_TYPE_ROBOT_PATH":         120,
		"EVENT_TYPE_ROBOT_WAYPOINTS":    121,
	}
)

func (x EventType) Enum() *EventType {
	p := new(EventType)
	*p = x
	return p
}

func (x EventType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (EventType) Descriptor() protoreflect.EnumDescriptor {
	return file_ar_v1_events_proto_enumTypes[0].Descriptor()
}

func (EventType) Type() protoreflect.EnumType {
	return &file_ar_v1_events_proto_enumTypes[0]
}

func (x EventType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use EventType.Descriptor instead.
func (EventType) EnumDescriptor() ([]byte, []int) {
	return file_ar_v1_events_proto_rawDescGZIP(), []int{0}
}

type SupportedEventsMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Events        []EventType            `protobuf:"varint,1,rep,packed,name=events,proto3,enum=ar.v1.EventType" json:"events,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SupportedEventsMessage) Reset() {
	*x = SupportedEventsMessage{}
	mi := &file_ar_v1_events_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SupportedEventsMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SupportedEventsMessage) ProtoMessage() {}

func (x *SupportedEventsMessage) ProtoReflect() protoreflect.Message {
	mi := &file_ar_v1_events_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SupportedEventsMessage.ProtoReflect.Descriptor instead.
func (*SupportedEventsMessage) Descriptor() ([]byte, []int) {
	return file_ar_v1_events_proto_rawDescGZIP(), []int{0}
}

func (x *SupportedEventsMessage) GetEvents() []EventType {
	if x != nil {
		return x.Events
	}
	return nil
}

var File_ar_v1_events_proto protoreflect.FileDescriptor

const file_ar_v1_events_proto_rawDesc = "" +
	"\n" +
	"\x12ar/v1/events.proto\x12\x05ar.v1\"B\n" +
	"\x16SupportedEventsMessage\x12(\n" +
	"\x06events\x18\x01 \x03(\x0e2\x10.ar.v1.EventTypeR\x06events*\xeb\x02\n" +
	"\tEventType\x12\x1a\n" +
	"\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n" +
	"\x18EVENT_TYPE_TASK_COMPLETE\x10\n" +
	"\x12\x18\n" +
	"\x14EVENT_TYPE_TASK_UNDO\x10\v\x12\x1a\n" +
	"\x16EVENT_TYPE_TASK_ASSIGN\x10\f\x12\x1d\n" +
	"\x19EVENT_TYPE_TASK_HIGHLIGHT\x10\r\x12\x18\n" +
	"\x14EVENT_TYPE_TASK_HELP\x10\x0e\x12\x18\n" +
	"\x14EVENT_TYPE_ROBOT_TCP\x10d\x12!\n" +
	"\x1dEVENT_TYPE_ROBOT_JOINT_ANGLES\x10e\x12!\n" +
	"\x1dEVENT_TYPE_ROBOT_FORCE_TORQUE\x10f\x12\x1a\n" +
	"\x16EVENT_TYPE_ROBOT_STATE\x10n\x12\x19\n" +
	"\x15EVENT_TYPE_ROBOT_PATH\x10x\x12\x1e\n" +
	"\x1aEVENT_TYPE_ROBOT_WAYPOINTS\x10yB\x87\x01\n" +
	"\tcom.ar.v1B\vEventsProtoP\x01Z/github.com/cobotar/protocol/messages/ar/v1;arv1\xa2\x02\x03AXX\xaa\x02\x0eMessages.AR.V1\xca\x02\x05Ar\\V1\xe2\x02\x11Ar\\V1\\GPBMetadata\xea\x02\x06Ar::V1b\x06proto3"

var (
	file_ar_v1_events_proto_rawDescOnce sync.Once
	file_ar_v1_events_proto_rawDescData []byte
)

func file_ar_v1_events_proto_rawDescGZIP() []byte {
	file_ar_v1_events_proto_rawDescOnce.Do(func() {
		file_ar_v1_events_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_ar_v1_events_proto_rawDesc), len(file_ar_v1_events_proto_rawDesc)))
	})
	return file_ar_v1_events_proto_rawDescData
}

var file_ar_v1_events_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_ar_v1_events_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_ar_v1_events_proto_goTypes = []any{
	(EventType)(0),                 // 0: ar.v1.EventType
	(*SupportedEventsMessage)(nil), // 1: ar.v1.SupportedEventsMessage
}
var file_ar_v1_events_proto_depIdxs = []int32{
	0, // 0: ar.v1.SupportedEventsMessage.events:type_name -> ar.v1.EventType
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_ar_v1_events_proto_init() }
func file_ar_v1_events_proto_init() {
	if File_ar_v1_events_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_ar_v1_events_proto_rawDesc), len(file_ar_v1_events_proto_rawDesc)),
			NumEnums:      1,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_ar_v1_events_proto_goTypes,
		DependencyIndexes: file_ar_v1_events_proto_depIdxs,
		EnumInfos:         file_ar_v1_events_proto_enumTypes,
		MessageInfos:      file_ar_v1_events_proto_msgTypes,
	}.Build()
	File_ar_v1_events_proto = out.File
	file_ar_v1_events_proto_goTypes = nil
	file_ar_v1_events_proto_depIdxs = nil
}
