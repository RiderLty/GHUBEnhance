package main

import (
	"net"
	"os"
	"strconv"
)

func main() {
	byteStr := os.Args[1]
	byteValue, _ := strconv.Atoi(byteStr)
	udpAddr, _ := net.ResolveUDPAddr("udp", "127.0.0.1:7779")
	conn, _ := net.DialUDP("udp", nil, udpAddr)
	defer conn.Close()
	conn.Write([]byte{byte(byteValue)})
}
