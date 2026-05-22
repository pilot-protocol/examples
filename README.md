# examples

Pilot Protocol example programs — start here to see how the daemon,
SDKs, and CLI fit together.

## Layout

| Path | What it is |
|---|---|
| `go/client/` | Minimal Go program: connect to local daemon, send a datagram. |
| `go/echo/` | Echo client + listener using `pkg/driver`. |
| `go/httpclient/` | HTTP-over-pilot client (proxy a fetch through the overlay). |
| `go/secure/` | Encrypted-stream demo using `pkg/secure`. |
| `go/webserver/` | A tiny web server reachable by virtual address. |
| `go/config/` | Sample JSON configs for daemon, rendezvous, nameserver. |
| `cli/` | Shell-script demos using the `pilotctl` CLI — data exchange, event stream, task submit. |
| `python_sdk/` | Python SDK examples — basic usage, pydantic_ai integration, demos. |

## Run a Go example

```bash
cd go
go run ./client
```

The examples use `replace ../web4` so they build against the local
sibling checkout of the protocol repo. If you want to build against
a tagged release instead, replace `v0.0.0` in `go/go.mod` with the
version you want and drop the replace lines.

## Prerequisites

You'll generally need a running daemon. Either:

```bash
# Build + run from the protocol repo:
cd ../web4
go build -o bin/pilot-daemon ./cmd/daemon
./bin/pilot-daemon -registry rendezvous.pilotprotocol.network:9000 \
                   -beacon rendezvous.pilotprotocol.network:9001 \
                   -socket /tmp/pilot.sock -encrypt
```

or install via the [website](https://pilotprotocol.network).
