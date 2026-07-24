# examples

[![ci](https://github.com/pilot-protocol/examples/actions/workflows/ci.yml/badge.svg)](https://github.com/pilot-protocol/examples/actions/workflows/ci.yml)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Pilot Protocol example programs — start here to see how the daemon,
SDKs, and CLI fit together.

## Layout

| Path | What it is |
|---|---|
| `go/client/` | Minimal Go program: connect to the local daemon and send a datagram. |
| `go/echo/` | Echo client + listener built on `pkg/driver`. |
| `go/httpclient/` | HTTP-over-pilot client — proxy a `fetch` through the overlay. |
| `go/secure/` | Encrypted-stream demo using `pkg/secure`. |
| `go/webserver/` | Tiny web server reachable by virtual address. |
| `go/config/` | Sample JSON configs for daemon, rendezvous, and nameserver. |
| `cli/` | Shell-script demos driving the `pilotctl` CLI — data exchange, event stream, task submit. |
| `python_sdk/` | Python SDK examples — basic usage, `pydantic_ai` integration, demos. |

## Prerequisites

You need a running daemon. Either install one from the
[website](https://pilotprotocol.network), or build the protocol
binary and run it locally:

```bash
go build -o bin/pilot-daemon github.com/pilot-protocol/pilotprotocol/cmd/daemon
./bin/pilot-daemon \
    -registry rendezvous.pilotprotocol.network:9000 \
    -beacon   rendezvous.pilotprotocol.network:9001 \
    -socket   /tmp/pilot.sock \
    -encrypt
```

## Run a Go example

```bash
cd go
go run ./client
```

The Go module's `go.mod` pins a tagged release of the protocol module.
Local development uses a `replace` directive to point at a sibling
checkout of the protocol source — drop or adjust that line to build
purely against the released module.

## Run a Python example

```bash
cd python_sdk
pip install -e .
python basic_usage.py
```

## Run a CLI example

```bash
cd cli
./data_exchange.sh
```

See [`cli/BASIC_USAGE.md`](cli/BASIC_USAGE.md) for the full shell walkthrough.

## License

AGPL-3.0-or-later. See [LICENSE](LICENSE).
