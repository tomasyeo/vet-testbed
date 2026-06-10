package main

import (
	"fmt"
	"os/exec"

	"golang.org/x/text/language"
)

func handle(userInput string) {
	cmd := exec.Command("sh", "-c", userInput)
	_ = cmd.Run()
}

func main() {
	tag := language.Make("en")
	fmt.Println(tag)
	handle("echo hello")
}
