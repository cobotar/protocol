package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"

	"github.com/cobotar/protocol/v2/internal/subjectgen"
)

func main() {
	if err := run(os.Args[1:]); err != nil {
		fmt.Fprintln(os.Stderr, "subjectgen:", err)
		os.Exit(1)
	}
}

func run(args []string) error {
	if len(args) == 0 {
		return fmt.Errorf("usage: subjectgen <validate|generate|check> [--root path]")
	}
	command := args[0]
	flags := flag.NewFlagSet(command, flag.ContinueOnError)
	rootFlag := flags.String("root", "", "protocol repository root")
	if err := flags.Parse(args[1:]); err != nil {
		return err
	}
	root, err := repositoryRoot(*rootFlag)
	if err != nil {
		return err
	}

	_, outputs, err := subjectgen.Prepare(root)
	if err != nil {
		return err
	}
	switch command {
	case "validate":
		return nil
	case "generate":
		return subjectgen.WriteOutputs(root, outputs)
	case "check":
		return subjectgen.CheckOutputs(root, outputs)
	default:
		return fmt.Errorf("unknown command %q; expected validate, generate, or check", command)
	}
}

func repositoryRoot(explicit string) (string, error) {
	if explicit != "" {
		return filepath.Abs(explicit)
	}
	directory, err := os.Getwd()
	if err != nil {
		return "", fmt.Errorf("get working directory: %w", err)
	}
	for {
		if _, err := os.Stat(filepath.Join(directory, "buf.yaml")); err == nil {
			return directory, nil
		}
		parent := filepath.Dir(directory)
		if parent == directory {
			return "", fmt.Errorf("could not find repository root containing buf.yaml")
		}
		directory = parent
	}
}
