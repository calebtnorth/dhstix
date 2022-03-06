## dhstix
An esolang for programmers who hate themselves.

You are given a linear array that can expand infinitely.
`|  ||` to move the pointer right
`||  |` to move the pointer left
`| |||` to increment the value at the pointer
`||| |` to decrememt the value at the pointer
`  |||` to output the value at the pointer
` ||||` to output the ASCII value at the pointer
`|||  ` to receive a number value at the pointer
`|| ||` to run the commands to the next || || if the value at the pointer is not 0

Whitespace is important. Newlines are ignored.
`|  |||  ||` is how you move left twice, not `|  || |  ||`