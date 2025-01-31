package bronze5

import (
	"bufio"
	"fmt"
	"os"
)

func Q108692UseScanf() {
	var a, b int
	fmt.Scanf("%d%d", &a, &b)
	fmt.Println(a + b)
	fmt.Println(a - b)
	fmt.Println(a * b)
	fmt.Println(a / b)
	fmt.Println(a % b)
	// 872mb, 4ms
}

func Q108692UseBufio() {
	var reader = bufio.NewReader(os.Stdin)
	var writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var a, b int

	fmt.Fscanln(reader, &a, &b)
	fmt.Fprintln(writer, a+b)
	fmt.Fprintln(writer, a-b)
	fmt.Fprintln(writer, a*b)
	fmt.Fprintln(writer, a/b)
	fmt.Fprintln(writer, a%b)
	// 872mb, 4ms
}
