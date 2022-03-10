# dhstix
An esolang for programmers who hate themselves.

## Intro
### Functionality
dhstix functions similarly to [BrainF***](https://esolangs.org/wiki/Brainfuck), in which it uses an array of memory cells that are accessed by moving a pointer left and right and modified by incrementing or decrementing by one. Loops resemble ifs because they function by establishing the beginning of loop and jumping to it if the value at the pointer is not 0 by the end of the loop. dhstix differs in the fact that, unlike the 30k cells allotted in BrainF***, dhstix starts with a single cell but will expand infinitely to the right. Another differentiating feature is that loops in dhstix cannot be nested.
### Execute File
To get started, simply [download the compiler](), only available for Windows as of yet. To execute a file, open up a terminal, navigate to the location where the exe is installed, and type `dhstix.exe <full path to file>`.
### Get Scripting
Each command in dhstix must be five characters long, including spaces. All other characters besides `|` and a space will be ignored.

# Docs
### Pointer Manipulation
<i>Note, the `*` resprents a space. Any `*` including in actual dhstix code will be ignored.</i><br>
`|**||`<br>
Move the pointer right. If the pointer extends above the last cell of the array then the pointer will create a new cell with a value of `0`.<br>
`||**|`<br>
Move the pointer left. If the pointer extends beneath the 0th cell of the array the pointer will be clamped at `0`.<br>
### Data Manipulation
`|*|||`<br>
Increment the value at the pointer by `1`.<br>
`|||*|`<br>
Decrement the value at the pointer by `1`. This value can go below zero<br>
### I/O
`**|||`<br>
Print the value at the pointer.<br>
`*||||`<br>
Print the ASCII equivalent of the value at the pointer.<br>
`|||**`<br>
Set the value at the pointer to an integer provided by the user.<br>
### Loops
`||*||`<br>
The first `||*||` marks the jumping point for the loop. The second `||*||` is the point where the compiler decides to jump to the jumping point or continue on with the script. The jump will be made if the value at pointer is not `0`.

## Errors
`No such file`<br>
The file path provided could not be found.<br>
`Please provide a file`<br>
No file has been provided for the compiler to run.<br> 
`Incomplete script!`<br>
This indicates one of the commands is not a full five characters long.<br>
`Not an integer`<br>
The value entered upon a `  |||` was not an integer.<br>
`Program killed by interrupt`<br>
A keyboard interrupt was performed.

# About
dhstix, or double hockey stix, is an esoteric language designed by [Caleb "fivesixfive" North](https://fivesixfive.dev) with the intent purpose of being excessively difficult to work in. It is inspired heavily by  [BrainF***](https://esolangs.org/wiki/Brainfuck) and is licensed under the [GPL v3.0](https://github.com/thefivesixfive/dhstix/blob/master/LICENSE)