// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        (unknown)
// source: common/v1/configuration.proto

package commonv1

import (
	v1 "github.com/cobotar/protocol/messages/tracker/v1"
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

type ConfigurationMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	InstanceId    string                 `protobuf:"bytes,1,opt,name=instance_id,json=instanceId,proto3" json:"instance_id,omitempty"`
	Id            string                 `protobuf:"bytes,2,opt,name=id,proto3" json:"id,omitempty"`
	Name          string                 `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	Description   string                 `protobuf:"bytes,4,opt,name=description,proto3" json:"description,omitempty"`
	Agents        []*Agent               `protobuf:"bytes,5,rep,name=agents,proto3" json:"agents,omitempty"`
	Trackers      []*v1.Tracker          `protobuf:"bytes,6,rep,name=trackers,proto3" json:"trackers,omitempty"`
	Properties    []*Property            `protobuf:"bytes,7,rep,name=properties,proto3" json:"properties,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ConfigurationMessage) Reset() {
	*x = ConfigurationMessage{}
	mi := &file_common_v1_configuration_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ConfigurationMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ConfigurationMessage) ProtoMessage() {}

func (x *ConfigurationMessage) ProtoReflect() protoreflect.Message {
	mi := &file_common_v1_configuration_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ConfigurationMessage.ProtoReflect.Descriptor instead.
func (*ConfigurationMessage) Descriptor() ([]byte, []int) {
	return file_common_v1_configuration_proto_rawDescGZIP(), []int{0}
}

func (x *ConfigurationMessage) GetInstanceId() string {
	if x != nil {
		return x.InstanceId
	}
	return ""
}

func (x *ConfigurationMessage) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *ConfigurationMessage) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *ConfigurationMessage) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *ConfigurationMessage) GetAgents() []*Agent {
	if x != nil {
		return x.Agents
	}
	return nil
}

func (x *ConfigurationMessage) GetTrackers() []*v1.Tracker {
	if x != nil {
		return x.Trackers
	}
	return nil
}

func (x *ConfigurationMessage) GetProperties() []*Property {
	if x != nil {
		return x.Properties
	}
	return nil
}

type LoadConfigurationMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Id            string                 `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`                                   // Id of the configuration to be loaded
	InstanceId    string                 `protobuf:"bytes,2,opt,name=instance_id,json=instanceId,proto3" json:"instance_id,omitempty"` // Instance id of the current loaded configuration - from the requestors perspective - used to avoid reloading a configuration.
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *LoadConfigurationMessage) Reset() {
	*x = LoadConfigurationMessage{}
	mi := &file_common_v1_configuration_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *LoadConfigurationMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LoadConfigurationMessage) ProtoMessage() {}

func (x *LoadConfigurationMessage) ProtoReflect() protoreflect.Message {
	mi := &file_common_v1_configuration_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LoadConfigurationMessage.ProtoReflect.Descriptor instead.
func (*LoadConfigurationMessage) Descriptor() ([]byte, []int) {
	return file_common_v1_configuration_proto_rawDescGZIP(), []int{1}
}

func (x *LoadConfigurationMessage) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *LoadConfigurationMessage) GetInstanceId() string {
	if x != nil {
		return x.InstanceId
	}
	return ""
}

type AddConfigurationMessage struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Name          string                 `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`                               // Name of the new configuration
	Description   string                 `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`                 // A description of the new configuration
	TemplateId    string                 `protobuf:"bytes,3,opt,name=template_id,json=templateId,proto3" json:"template_id,omitempty"` // Template id is used to pre-populate a configuration. Leave empty for a new fresh start.
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *AddConfigurationMessage) Reset() {
	*x = AddConfigurationMessage{}
	mi := &file_common_v1_configuration_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *AddConfigurationMessage) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AddConfigurationMessage) ProtoMessage() {}

func (x *AddConfigurationMessage) ProtoReflect() protoreflect.Message {
	mi := &file_common_v1_configuration_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AddConfigurationMessage.ProtoReflect.Descriptor instead.
func (*AddConfigurationMessage) Descriptor() ([]byte, []int) {
	return file_common_v1_configuration_proto_rawDescGZIP(), []int{2}
}

func (x *AddConfigurationMessage) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *AddConfigurationMessage) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *AddConfigurationMessage) GetTemplateId() string {
	if x != nil {
		return x.TemplateId
	}
	return ""
}

var File_common_v1_configuration_proto protoreflect.FileDescriptor

const file_common_v1_configuration_proto_rawDesc = "" +
	"\n" +
	"\x1dcommon/v1/configuration.proto\x12\tcommon.v1\x1a\x15common/v1/agent.proto\x1a\x18common/v1/property.proto\x1a\x18tracker/v1/tracker.proto\"\x8d\x02\n" +
	"\x14ConfigurationMessage\x12\x1f\n" +
	"\vinstance_id\x18\x01 \x01(\tR\n" +
	"instanceId\x12\x0e\n" +
	"\x02id\x18\x02 \x01(\tR\x02id\x12\x12\n" +
	"\x04name\x18\x03 \x01(\tR\x04name\x12 \n" +
	"\vdescription\x18\x04 \x01(\tR\vdescription\x12(\n" +
	"\x06agents\x18\x05 \x03(\v2\x10.common.v1.AgentR\x06agents\x12/\n" +
	"\btrackers\x18\x06 \x03(\v2\x13.tracker.v1.TrackerR\btrackers\x123\n" +
	"\n" +
	"properties\x18\a \x03(\v2\x13.common.v1.PropertyR\n" +
	"properties\"K\n" +
	"\x18LoadConfigurationMessage\x12\x0e\n" +
	"\x02id\x18\x01 \x01(\tR\x02id\x12\x1f\n" +
	"\vinstance_id\x18\x02 \x01(\tR\n" +
	"instanceId\"p\n" +
	"\x17AddConfigurationMessage\x12\x12\n" +
	"\x04name\x18\x01 \x01(\tR\x04name\x12 \n" +
	"\vdescription\x18\x02 \x01(\tR\vdescription\x12\x1f\n" +
	"\vtemplate_id\x18\x03 \x01(\tR\n" +
	"templateIdB\xaa\x01\n" +
	"\rcom.common.v1B\x12ConfigurationProtoP\x01Z7github.com/cobotar/protocol/messages/common/v1;commonv1\xa2\x02\x03CXX\xaa\x02\x12Messages.Common.V1\xca\x02\tCommon\\V1\xe2\x02\x15Common\\V1\\GPBMetadata\xea\x02\n" +
	"Common::V1b\x06proto3"

var (
	file_common_v1_configuration_proto_rawDescOnce sync.Once
	file_common_v1_configuration_proto_rawDescData []byte
)

func file_common_v1_configuration_proto_rawDescGZIP() []byte {
	file_common_v1_configuration_proto_rawDescOnce.Do(func() {
		file_common_v1_configuration_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_common_v1_configuration_proto_rawDesc), len(file_common_v1_configuration_proto_rawDesc)))
	})
	return file_common_v1_configuration_proto_rawDescData
}

var file_common_v1_configuration_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_common_v1_configuration_proto_goTypes = []any{
	(*ConfigurationMessage)(nil),     // 0: common.v1.ConfigurationMessage
	(*LoadConfigurationMessage)(nil), // 1: common.v1.LoadConfigurationMessage
	(*AddConfigurationMessage)(nil),  // 2: common.v1.AddConfigurationMessage
	(*Agent)(nil),                    // 3: common.v1.Agent
	(*v1.Tracker)(nil),               // 4: tracker.v1.Tracker
	(*Property)(nil),                 // 5: common.v1.Property
}
var file_common_v1_configuration_proto_depIdxs = []int32{
	3, // 0: common.v1.ConfigurationMessage.agents:type_name -> common.v1.Agent
	4, // 1: common.v1.ConfigurationMessage.trackers:type_name -> tracker.v1.Tracker
	5, // 2: common.v1.ConfigurationMessage.properties:type_name -> common.v1.Property
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_common_v1_configuration_proto_init() }
func file_common_v1_configuration_proto_init() {
	if File_common_v1_configuration_proto != nil {
		return
	}
	file_common_v1_agent_proto_init()
	file_common_v1_property_proto_init()
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_common_v1_configuration_proto_rawDesc), len(file_common_v1_configuration_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_common_v1_configuration_proto_goTypes,
		DependencyIndexes: file_common_v1_configuration_proto_depIdxs,
		MessageInfos:      file_common_v1_configuration_proto_msgTypes,
	}.Build()
	File_common_v1_configuration_proto = out.File
	file_common_v1_configuration_proto_goTypes = nil
	file_common_v1_configuration_proto_depIdxs = nil
}
