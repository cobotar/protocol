package subjectgen

import (
	"bytes"
	"fmt"
	"os"
	"path/filepath"
	"sort"
)

func Prepare(root string) (*Catalog, []Output, error) {
	catalog, err := LoadCatalog(filepath.Join(root, "subjects", "catalog.yaml"))
	if err != nil {
		return nil, nil, err
	}
	messageTypes, err := LoadMessageTypes(root)
	if err != nil {
		return nil, nil, err
	}
	if err := Validate(catalog, messageTypes); err != nil {
		return nil, nil, err
	}
	outputs, err := Generate(catalog)
	if err != nil {
		return nil, nil, err
	}
	sortOutputs(outputs)
	return catalog, outputs, nil
}

func WriteOutputs(root string, outputs []Output) error {
	for _, output := range outputs {
		path := filepath.Join(root, filepath.FromSlash(output.Path))
		if current, err := os.ReadFile(path); err == nil && bytes.Equal(current, output.Content) {
			continue
		}
		if err := os.MkdirAll(filepath.Dir(path), 0o755); err != nil {
			return fmt.Errorf("create output directory for %s: %w", output.Path, err)
		}
		temp, err := os.CreateTemp(filepath.Dir(path), ".subjectgen-*")
		if err != nil {
			return fmt.Errorf("create temporary output for %s: %w", output.Path, err)
		}
		tempPath := temp.Name()
		cleanup := func() { _ = os.Remove(tempPath) }
		if _, err := temp.Write(output.Content); err != nil {
			_ = temp.Close()
			cleanup()
			return fmt.Errorf("write temporary output for %s: %w", output.Path, err)
		}
		if err := temp.Chmod(0o644); err != nil {
			_ = temp.Close()
			cleanup()
			return fmt.Errorf("set permissions for %s: %w", output.Path, err)
		}
		if err := temp.Close(); err != nil {
			cleanup()
			return fmt.Errorf("close temporary output for %s: %w", output.Path, err)
		}
		if err := os.Rename(tempPath, path); err != nil {
			cleanup()
			return fmt.Errorf("replace %s: %w", output.Path, err)
		}
	}
	return nil
}

func CheckOutputs(root string, outputs []Output) error {
	var stale []string
	for _, output := range outputs {
		path := filepath.Join(root, filepath.FromSlash(output.Path))
		current, err := os.ReadFile(path)
		if err != nil || !bytes.Equal(current, output.Content) {
			stale = append(stale, output.Path)
		}
	}
	if len(stale) == 0 {
		return nil
	}
	sort.Strings(stale)
	return fmt.Errorf("generated subject files are missing or stale:\n  %s\nrun `go run ./cmd/subjectgen generate`", joinLines(stale))
}

func joinLines(values []string) string {
	result := ""
	for index, value := range values {
		if index > 0 {
			result += "\n  "
		}
		result += value
	}
	return result
}
