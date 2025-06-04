
## lint: run the buf lint command
.PHONY: lint
lint:
	buf lint

## breaking: run the buf breaking command
.PHONY: breaking
breaking:
	buf breaking --against "https://github.com/cobotar/protocol.git#branch=main"
