// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: ar/v1/authoring_feedback.proto

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

type FeedbackNewMessage struct {
	state          protoimpl.MessageState `protogen:"open.v1"`
	ParentConfigId string                 `protobuf:"bytes,1,opt,name=parent_config_id,json=parentConfigId,proto3" json:"parent_config_id,omitempty"`
	Name           string                 `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Icon           string                 `protobuf:"bytes,3,opt,name=icon,proto3" json:"icon,omitempty"`
	Description    string                 `protobuf:"bytes,4,opt,name=description,proto3" json:"description,omitempty"`
	Type           FeedbackType           `protobuf:"varint,5,opt,name=type,proto3,enum=ar.v1.FeedbackType" json:"type,omitempty"`
	FrameId        string                 `protobuf:"bytes,6,opt,name=frame_id,json=frameId,proto3" json:"frame_id,omitempty"`
	AgentId        string                 `protobuf:"bytes,7,opt,name=agent_id,json=agentId,proto3" json:"agent_id,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *FeedbackNewMessage) Reset() {
	*x = FeedbackNewMessage{}
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *FeedbackNewMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeedbackNewMessage) ProtoMessage() {}

func (x *FeedbackNewMessage) ProtoReflect() protoreflect.Message {
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeedbackNewMessage.ProtoReflect.Descriptor instead.
func (*FeedbackNewMessage) Descriptor() ([]byte, []int) {
	return file_ar_v1_authoring_feedback_proto_rawDescGZIP(), []int{0}
}

func (x *FeedbackNewMessage) GetParentConfigId() string {
	if x != nil {
		return x.ParentConfigId
	}
	return ""
}

func (x *FeedbackNewMessage) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *FeedbackNewMessage) GetIcon() string {
	if x != nil {
		return x.Icon
	}
	return ""
}

func (x *FeedbackNewMessage) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *FeedbackNewMessage) GetType() FeedbackType {
	if x != nil {
		return x.Type
	}
	return FeedbackType_FEEDBACK_TYPE_UNSPECIFIED
}

func (x *FeedbackNewMessage) GetFrameId() string {
	if x != nil {
		return x.FrameId
	}
	return ""
}

func (x *FeedbackNewMessage) GetAgentId() string {
	if x != nil {
		return x.AgentId
	}
	return ""
}

type FeedbackUpdateMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Id            string                 `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	Name          string                 `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Icon          string                 `protobuf:"bytes,3,opt,name=icon,proto3" json:"icon,omitempty"`
	Description   string                 `protobuf:"bytes,4,opt,name=description,proto3" json:"description,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *FeedbackUpdateMessage) Reset() {
	*x = FeedbackUpdateMessage{}
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *FeedbackUpdateMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeedbackUpdateMessage) ProtoMessage() {}

func (x *FeedbackUpdateMessage) ProtoReflect() protoreflect.Message {
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeedbackUpdateMessage.ProtoReflect.Descriptor instead.
func (*FeedbackUpdateMessage) Descriptor() ([]byte, []int) {
	return file_ar_v1_authoring_feedback_proto_rawDescGZIP(), []int{1}
}

func (x *FeedbackUpdateMessage) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *FeedbackUpdateMessage) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *FeedbackUpdateMessage) GetIcon() string {
	if x != nil {
		return x.Icon
	}
	return ""
}

func (x *FeedbackUpdateMessage) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

type FeedbackCloneMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	OriginalId    string                 `protobuf:"bytes,1,opt,name=original_id,json=originalId,proto3" json:"original_id,omitempty"`
	Name          string                 `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Icon          string                 `protobuf:"bytes,3,opt,name=icon,proto3" json:"icon,omitempty"`
	Description   string                 `protobuf:"bytes,4,opt,name=description,proto3" json:"description,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *FeedbackCloneMessage) Reset() {
	*x = FeedbackCloneMessage{}
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *FeedbackCloneMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeedbackCloneMessage) ProtoMessage() {}

func (x *FeedbackCloneMessage) ProtoReflect() protoreflect.Message {
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeedbackCloneMessage.ProtoReflect.Descriptor instead.
func (*FeedbackCloneMessage) Descriptor() ([]byte, []int) {
	return file_ar_v1_authoring_feedback_proto_rawDescGZIP(), []int{2}
}

func (x *FeedbackCloneMessage) GetOriginalId() string {
	if x != nil {
		return x.OriginalId
	}
	return ""
}

func (x *FeedbackCloneMessage) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *FeedbackCloneMessage) GetIcon() string {
	if x != nil {
		return x.Icon
	}
	return ""
}

func (x *FeedbackCloneMessage) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

type FeedbackDeleteMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Id            string                 `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *FeedbackDeleteMessage) Reset() {
	*x = FeedbackDeleteMessage{}
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *FeedbackDeleteMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FeedbackDeleteMessage) ProtoMessage() {}

func (x *FeedbackDeleteMessage) ProtoReflect() protoreflect.Message {
	mi := &file_ar_v1_authoring_feedback_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FeedbackDeleteMessage.ProtoReflect.Descriptor instead.
func (*FeedbackDeleteMessage) Descriptor() ([]byte, []int) {
	return file_ar_v1_authoring_feedback_proto_rawDescGZIP(), []int{3}
}

func (x *FeedbackDeleteMessage) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

var File_ar_v1_authoring_feedback_proto protoreflect.FileDescriptor

const file_ar_v1_authoring_feedback_proto_rawDesc = "" +
	"\n" +
	"\x1ear/v1/authoring_feedback.proto\x12\x05ar.v1\x1a\x14ar/v1/feedback.proto\"\xe7\x01\n" +
	"\x12FeedbackNewMessage\x12(\n" +
	"\x10parent_config_id\x18\x01 \x01(\tR\x0eparentConfigId\x12\x12\n" +
	"\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n" +
	"\x04icon\x18\x03 \x01(\tR\x04icon\x12 \n" +
	"\vdescription\x18\x04 \x01(\tR\vdescription\x12'\n" +
	"\x04type\x18\x05 \x01(\x0e2\x13.ar.v1.FeedbackTypeR\x04type\x12\x19\n" +
	"\bframe_id\x18\x06 \x01(\tR\aframeId\x12\x19\n" +
	"\bagent_id\x18\a \x01(\tR\aagentId\"q\n" +
	"\x15FeedbackUpdateMessage\x12\x0e\n" +
	"\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n" +
	"\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n" +
	"\x04icon\x18\x03 \x01(\tR\x04icon\x12 \n" +
	"\vdescription\x18\x04 \x01(\tR\vdescription\"\x81\x01\n" +
	"\x14FeedbackCloneMessage\x12\x1f\n" +
	"\voriginal_id\x18\x01 \x01(\tR\n" +
	"originalId\x12\x12\n" +
	"\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n" +
	"\x04icon\x18\x03 \x01(\tR\x04icon\x12 \n" +
	"\vdescription\x18\x04 \x01(\tR\vdescription\"'\n" +
	"\x15FeedbackDeleteMessage\x12\x0e\n" +
	"\x02id\x18\x01 \x01(\tR\x02idB\x92\x01\n" +
	"\tcom.ar.v1B\x16AuthoringFeedbackProtoP\x01Z/github.com/cobotar/protocol/messages/ar/v1;arv1\xa2\x02\x03AXX\xaa\x02\x0eMessages.AR.V1\xca\x02\x05Ar\\V1\xe2\x02\x11Ar\\V1\\GPBMetadata\xea\x02\x06Ar::V1b\x06proto3"

var (
	file_ar_v1_authoring_feedback_proto_rawDescOnce sync.Once
	file_ar_v1_authoring_feedback_proto_rawDescData []byte
)

func file_ar_v1_authoring_feedback_proto_rawDescGZIP() []byte {
	file_ar_v1_authoring_feedback_proto_rawDescOnce.Do(func() {
		file_ar_v1_authoring_feedback_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_ar_v1_authoring_feedback_proto_rawDesc), len(file_ar_v1_authoring_feedback_proto_rawDesc)))
	})
	return file_ar_v1_authoring_feedback_proto_rawDescData
}

var file_ar_v1_authoring_feedback_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_ar_v1_authoring_feedback_proto_goTypes = []any{
	(*FeedbackNewMessage)(nil),    // 0: ar.v1.FeedbackNewMessage
	(*FeedbackUpdateMessage)(nil), // 1: ar.v1.FeedbackUpdateMessage
	(*FeedbackCloneMessage)(nil),  // 2: ar.v1.FeedbackCloneMessage
	(*FeedbackDeleteMessage)(nil), // 3: ar.v1.FeedbackDeleteMessage
	(FeedbackType)(0),             // 4: ar.v1.FeedbackType
}
var file_ar_v1_authoring_feedback_proto_depIdxs = []int32{
	4, // 0: ar.v1.FeedbackNewMessage.type:type_name -> ar.v1.FeedbackType
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_ar_v1_authoring_feedback_proto_init() }
func file_ar_v1_authoring_feedback_proto_init() {
	if File_ar_v1_authoring_feedback_proto != nil {
		return
	}
	file_ar_v1_feedback_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_ar_v1_authoring_feedback_proto_rawDesc), len(file_ar_v1_authoring_feedback_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_ar_v1_authoring_feedback_proto_goTypes,
		DependencyIndexes: file_ar_v1_authoring_feedback_proto_depIdxs,
		MessageInfos:      file_ar_v1_authoring_feedback_proto_msgTypes,
	}.Build()
	File_ar_v1_authoring_feedback_proto = out.File
	file_ar_v1_authoring_feedback_proto_goTypes = nil
	file_ar_v1_authoring_feedback_proto_depIdxs = nil
}
