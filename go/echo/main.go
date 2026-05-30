// SPDX-License-Identifier: AGPL-3.0-or-later

package main

import (
	"flag"
	"log"

	"github.com/pilot-protocol/common/driver"
)

func main() {
	socketPath := flag.String("socket", "/tmp/pilot.sock", "daemon socket path")
	port := flag.Uint("port", 7, "pilot port to listen on")
	raw := flag.Bool("raw", true, "raw echo (no prefix)")
	flag.Parse()

	d, err := driver.Connect(*socketPath)
	if err != nil {
		log.Fatalf("connect to daemon: %v", err)
	}
	defer d.Close()

	ln, err := d.Listen(uint16(*port))
	if err != nil {
		log.Fatalf("listen: %v", err)
	}

	log.Printf("echo server listening on pilot port %d", *port)

	for {
		conn, err := ln.Accept()
		if err != nil {
			log.Printf("accept: %v", err)
			continue
		}

		go func() {
			defer conn.Close()
			buf := make([]byte, 65535)
			for {
				n, err := conn.Read(buf)
				if err != nil {
					return
				}
				if *raw {
					if _, err := conn.Write(buf[:n]); err != nil {
						log.Printf("write: %v", err)
						return
					}
				} else {
					log.Printf("received from %s: %s", conn.RemoteAddr(), string(buf[:n]))
					if _, err := conn.Write(append([]byte("echo: "), buf[:n]...)); err != nil {
						log.Printf("write: %v", err)
						return
					}
				}
			}
		}()
	}
}
