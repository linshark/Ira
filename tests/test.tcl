set string1 "ololo"
puts "String for search: $string1"
set fp [open "tcl.txt" r]

set file_data [read $fp]
puts "Text is: $file_data"
set sl1 [string first $string1 $file_data]
#puts $sl1
close $fp
puts "Here [string length $string1] symbols in \"$string1\""
set sl2 [string length $string1]
#puts $sl2
if {$string1=="ololo"} {
puts "The test was successful"
} else {
puts "The test was failed"
}
puts "The string has found: \"[string range $file_data $sl1 $sl1+$sl2]\""