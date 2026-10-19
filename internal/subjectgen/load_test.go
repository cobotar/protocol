package subjectgen

import (
	"os"
	"path/filepath"
	"strings"
	"testing"
)

func TestLoadCatalogRejectsUnknownFields(t *testing.T) {
	path := filepath.Join(t.TempDir(), "catalog.yaml")
	data := []byte("version: 1\nunknown: true\n")
	if err := os.WriteFile(path, data, 0o600); err != nil {
		t.Fatal(err)
	}

	_, err := LoadCatalog(path)
	if err == nil || !strings.Contains(err.Error(), "field unknown not found") {
		t.Fatalf("LoadCatalog() error = %v", err)
	}
}
