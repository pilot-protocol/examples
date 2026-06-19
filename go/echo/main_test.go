package main

import "testing"

// TestExampleCompiles is a placeholder so `go test ./...` exercises the
// compile + link path for this example. The example itself is a main
// package; running its main() requires a live daemon, so we only assert
// that it builds cleanly. Compile = type-check + link, which catches
// upstream pkg/protocol or SDK API breakage as web4 evolves.
func TestExampleCompiles(t *testing.T) {
	// Build success is implicit: the test binary cannot link if main.go
	// references a missing or renamed symbol in github.com/pilot-protocol/pilotprotocol.
}
