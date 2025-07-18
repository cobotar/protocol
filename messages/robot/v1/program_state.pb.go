// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: robot/v1/program_state.proto

package robotv1

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

type ProgramState int32

const (
	ProgramState_PROGRAM_STATE_UNSPECIFIED ProgramState = 0
	ProgramState_PROGRAM_STATE_PLAY        ProgramState = 1
	ProgramState_PROGRAM_STATE_PAUSE       ProgramState = 2
	ProgramState_PROGRAM_STATE_STOP        ProgramState = 3
)

// Enum value maps for ProgramState.
var (
	ProgramState_name = map[int32]string{
		0: "PROGRAM_STATE_UNSPECIFIED",
		1: "PROGRAM_STATE_PLAY",
		2: "PROGRAM_STATE_PAUSE",
		3: "PROGRAM_STATE_STOP",
	}
	ProgramState_value = map[string]int32{
		"PROGRAM_STATE_UNSPECIFIED": 0,
		"PROGRAM_STATE_PLAY":        1,
		"PROGRAM_STATE_PAUSE":       2,
		"PROGRAM_STATE_STOP":        3,
	}
)

func (x ProgramState) Enum() *ProgramState {
	p := new(ProgramState)
	*p = x
	return p
}

func (x ProgramState) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (ProgramState) Descriptor() protoreflect.EnumDescriptor {
	return file_robot_v1_program_state_proto_enumTypes[0].Descriptor()
}

func (ProgramState) Type() protoreflect.EnumType {
	return &file_robot_v1_program_state_proto_enumTypes[0]
}

func (x ProgramState) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use ProgramState.Descriptor instead.
func (ProgramState) EnumDescriptor() ([]byte, []int) {
	return file_robot_v1_program_state_proto_rawDescGZIP(), []int{0}
}

type ProgramStateMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	RobotId       string                 `protobuf:"bytes,1,opt,name=robot_id,json=robotId,proto3" json:"robot_id,omitempty"`
	StateCode     ProgramState           `protobuf:"varint,2,opt,name=state_code,json=stateCode,proto3,enum=robot.v1.ProgramState" json:"state_code,omitempty"`
	State         string                 `protobuf:"bytes,3,opt,name=state,proto3" json:"state,omitempty"`
	ProgramFile   string                 `protobuf:"bytes,4,opt,name=program_file,json=programFile,proto3" json:"program_file,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ProgramStateMessage) Reset() {
	*x = ProgramStateMessage{}
	mi := &file_robot_v1_program_state_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ProgramStateMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ProgramStateMessage) ProtoMessage() {}

func (x *ProgramStateMessage) ProtoReflect() protoreflect.Message {
	mi := &file_robot_v1_program_state_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ProgramStateMessage.ProtoReflect.Descriptor instead.
func (*ProgramStateMessage) Descriptor() ([]byte, []int) {
	return file_robot_v1_program_state_proto_rawDescGZIP(), []int{0}
}

func (x *ProgramStateMessage) GetRobotId() string {
	if x != nil {
		return x.RobotId
	}
	return ""
}

func (x *ProgramStateMessage) GetStateCode() ProgramState {
	if x != nil {
		return x.StateCode
	}
	return ProgramState_PROGRAM_STATE_UNSPECIFIED
}

func (x *ProgramStateMessage) GetState() string {
	if x != nil {
		return x.State
	}
	return ""
}

func (x *ProgramStateMessage) GetProgramFile() string {
	if x != nil {
		return x.ProgramFile
	}
	return ""
}

var File_robot_v1_program_state_proto protoreflect.FileDescriptor

const file_robot_v1_program_state_proto_rawDesc = "" +
	"\n" +
	"\x1crobot/v1/program_state.proto\x12\brobot.v1\"\xa0\x01\n" +
	"\x13ProgramStateMessage\x12\x19\n" +
	"\brobot_id\x18\x01 \x01(\tR\arobotId\x125\n" +
	"\n" +
	"state_code\x18\x02 \x01(\x0e2\x16.robot.v1.ProgramStateR\tstateCode\x12\x14\n" +
	"\x05state\x18\x03 \x01(\tR\x05state\x12!\n" +
	"\fprogram_file\x18\x04 \x01(\tR\vprogramFile*v\n" +
	"\fProgramState\x12\x1d\n" +
	"\x19PROGRAM_STATE_UNSPECIFIED\x10\x00\x12\x16\n" +
	"\x12PROGRAM_STATE_PLAY\x10\x01\x12\x17\n" +
	"\x13PROGRAM_STATE_PAUSE\x10\x02\x12\x16\n" +
	"\x12PROGRAM_STATE_STOP\x10\x03B\xa3\x01\n" +
	"\fcom.robot.v1B\x11ProgramStateProtoP\x01Z5github.com/cobotar/protocol/messages/robot/v1;robotv1\xa2\x02\x03RXX\xaa\x02\x12Messages.Common.V1\xca\x02\bRobot\\V1\xe2\x02\x14Robot\\V1\\GPBMetadata\xea\x02\tRobot::V1b\x06proto3"

var (
	file_robot_v1_program_state_proto_rawDescOnce sync.Once
	file_robot_v1_program_state_proto_rawDescData []byte
)

func file_robot_v1_program_state_proto_rawDescGZIP() []byte {
	file_robot_v1_program_state_proto_rawDescOnce.Do(func() {
		file_robot_v1_program_state_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_robot_v1_program_state_proto_rawDesc), len(file_robot_v1_program_state_proto_rawDesc)))
	})
	return file_robot_v1_program_state_proto_rawDescData
}

var file_robot_v1_program_state_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_robot_v1_program_state_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_robot_v1_program_state_proto_goTypes = []any{
	(ProgramState)(0),           // 0: robot.v1.ProgramState
	(*ProgramStateMessage)(nil), // 1: robot.v1.ProgramStateMessage
}
var file_robot_v1_program_state_proto_depIdxs = []int32{
	0, // 0: robot.v1.ProgramStateMessage.state_code:type_name -> robot.v1.ProgramState
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_robot_v1_program_state_proto_init() }
func file_robot_v1_program_state_proto_init() {
	if File_robot_v1_program_state_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_robot_v1_program_state_proto_rawDesc), len(file_robot_v1_program_state_proto_rawDesc)),
			NumEnums:      1,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_robot_v1_program_state_proto_goTypes,
		DependencyIndexes: file_robot_v1_program_state_proto_depIdxs,
		EnumInfos:         file_robot_v1_program_state_proto_enumTypes,
		MessageInfos:      file_robot_v1_program_state_proto_msgTypes,
	}.Build()
	File_robot_v1_program_state_proto = out.File
	file_robot_v1_program_state_proto_goTypes = nil
	file_robot_v1_program_state_proto_depIdxs = nil
}
