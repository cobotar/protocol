// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: robot/v1/program_state_request.proto

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

type ProgramStateRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	RequestId     string                 `protobuf:"bytes,1,opt,name=request_id,json=requestId,proto3" json:"request_id,omitempty"`
	RobotId       string                 `protobuf:"bytes,2,opt,name=robot_id,json=robotId,proto3" json:"robot_id,omitempty"`
	State         ProgramState           `protobuf:"varint,3,opt,name=state,proto3,enum=robot.v1.ProgramState" json:"state,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ProgramStateRequest) Reset() {
	*x = ProgramStateRequest{}
	mi := &file_robot_v1_program_state_request_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ProgramStateRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ProgramStateRequest) ProtoMessage() {}

func (x *ProgramStateRequest) ProtoReflect() protoreflect.Message {
	mi := &file_robot_v1_program_state_request_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ProgramStateRequest.ProtoReflect.Descriptor instead.
func (*ProgramStateRequest) Descriptor() ([]byte, []int) {
	return file_robot_v1_program_state_request_proto_rawDescGZIP(), []int{0}
}

func (x *ProgramStateRequest) GetRequestId() string {
	if x != nil {
		return x.RequestId
	}
	return ""
}

func (x *ProgramStateRequest) GetRobotId() string {
	if x != nil {
		return x.RobotId
	}
	return ""
}

func (x *ProgramStateRequest) GetState() ProgramState {
	if x != nil {
		return x.State
	}
	return ProgramState_PROGRAM_STATE_UNSPECIFIED
}

var File_robot_v1_program_state_request_proto protoreflect.FileDescriptor

const file_robot_v1_program_state_request_proto_rawDesc = "" +
	"\n" +
	"$robot/v1/program_state_request.proto\x12\brobot.v1\x1a\x1crobot/v1/program_state.proto\"}\n" +
	"\x13ProgramStateRequest\x12\x1d\n" +
	"\n" +
	"request_id\x18\x01 \x01(\tR\trequestId\x12\x19\n" +
	"\brobot_id\x18\x02 \x01(\tR\arobotId\x12,\n" +
	"\x05state\x18\x03 \x01(\x0e2\x16.robot.v1.ProgramStateR\x05stateB\xaa\x01\n" +
	"\fcom.robot.v1B\x18ProgramStateRequestProtoP\x01Z5github.com/cobotar/protocol/messages/robot/v1;robotv1\xa2\x02\x03RXX\xaa\x02\x12Messages.Common.V1\xca\x02\bRobot\\V1\xe2\x02\x14Robot\\V1\\GPBMetadata\xea\x02\tRobot::V1b\x06proto3"

var (
	file_robot_v1_program_state_request_proto_rawDescOnce sync.Once
	file_robot_v1_program_state_request_proto_rawDescData []byte
)

func file_robot_v1_program_state_request_proto_rawDescGZIP() []byte {
	file_robot_v1_program_state_request_proto_rawDescOnce.Do(func() {
		file_robot_v1_program_state_request_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_robot_v1_program_state_request_proto_rawDesc), len(file_robot_v1_program_state_request_proto_rawDesc)))
	})
	return file_robot_v1_program_state_request_proto_rawDescData
}

var file_robot_v1_program_state_request_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_robot_v1_program_state_request_proto_goTypes = []any{
	(*ProgramStateRequest)(nil), // 0: robot.v1.ProgramStateRequest
	(ProgramState)(0),           // 1: robot.v1.ProgramState
}
var file_robot_v1_program_state_request_proto_depIdxs = []int32{
	1, // 0: robot.v1.ProgramStateRequest.state:type_name -> robot.v1.ProgramState
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_robot_v1_program_state_request_proto_init() }
func file_robot_v1_program_state_request_proto_init() {
	if File_robot_v1_program_state_request_proto != nil {
		return
	}
	file_robot_v1_program_state_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_robot_v1_program_state_request_proto_rawDesc), len(file_robot_v1_program_state_request_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_robot_v1_program_state_request_proto_goTypes,
		DependencyIndexes: file_robot_v1_program_state_request_proto_depIdxs,
		MessageInfos:      file_robot_v1_program_state_request_proto_msgTypes,
	}.Build()
	File_robot_v1_program_state_request_proto = out.File
	file_robot_v1_program_state_request_proto_goTypes = nil
	file_robot_v1_program_state_request_proto_depIdxs = nil
}
