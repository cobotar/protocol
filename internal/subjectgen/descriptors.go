package subjectgen

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/descriptorpb"
)

func LoadMessageTypes(root string) (map[string]struct{}, error) {
	tempDir, err := os.MkdirTemp("", "subjectgen-descriptors-")
	if err != nil {
		return nil, fmt.Errorf("create descriptor directory: %w", err)
	}
	defer os.RemoveAll(tempDir)

	descriptorPath := filepath.Join(tempDir, "protocol.binpb")
	cmd := exec.Command("buf", "build", "--as-file-descriptor-set", "-o", descriptorPath)
	cmd.Dir = root
	if output, err := cmd.CombinedOutput(); err != nil {
		return nil, fmt.Errorf("build protobuf descriptors: %w: %s", err, output)
	}

	data, err := os.ReadFile(descriptorPath)
	if err != nil {
		return nil, fmt.Errorf("read protobuf descriptors: %w", err)
	}
	set := &descriptorpb.FileDescriptorSet{}
	if err := proto.Unmarshal(data, set); err != nil {
		return nil, fmt.Errorf("decode protobuf descriptors: %w", err)
	}

	types := make(map[string]struct{})
	for _, file := range set.File {
		prefix := file.GetPackage()
		for _, message := range file.MessageType {
			indexMessage(types, prefix, message)
		}
	}
	return types, nil
}

func indexMessage(types map[string]struct{}, prefix string, message *descriptorpb.DescriptorProto) {
	name := message.GetName()
	if prefix != "" {
		name = prefix + "." + name
	}
	types[name] = struct{}{}
	for _, nested := range message.NestedType {
		indexMessage(types, name, nested)
	}
}
