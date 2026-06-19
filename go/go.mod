module github.com/pilot-protocol/examples/go

go 1.25.10

require github.com/pilot-protocol/common v0.1.0

replace github.com/pilot-protocol/pilotprotocol => ../../web4

// Mirror web4's replace directives so transitive deps resolve.
replace github.com/pilot-protocol/app-store => ../../app-store

replace github.com/pilot-protocol/trustedagents => ../../trustedagents

replace github.com/pilot-protocol/skillinject => ../../skillinject

replace github.com/pilot-protocol/webhook => ../../webhook

replace github.com/pilot-protocol/eventstream => ../../eventstream

replace github.com/pilot-protocol/dataexchange => ../../dataexchange

replace github.com/pilot-protocol/updater => ../../updater

replace github.com/pilot-protocol/gateway => ../../gateway

replace github.com/pilot-protocol/nameserver => ../../nameserver

replace github.com/pilot-protocol/policy => ../../policy

replace github.com/pilot-protocol/handshake => ../../handshake

replace github.com/pilot-protocol/runtime => ../../runtime

replace github.com/pilot-protocol/common => ../../common

replace github.com/pilot-protocol/rendezvous => ../../rendezvous

replace github.com/pilot-protocol/beacon => ../../beacon
