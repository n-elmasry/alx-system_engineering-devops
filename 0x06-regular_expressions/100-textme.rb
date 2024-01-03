#!/usr/bin/env ruby
#  script should output: [SENDER],[RECEIVER],[FLAGS]
input_string = ARGV[0]

sender = input_string.scan(/(?<=from:).[a-zA-Z0-9]{1,}/).join
receiver = input_string.scan(/(?<=\[to:).[a-zA-Z0-9]{1,}/).join
flags = input_string.scan(/(?<=flags:).?\d[:].?\d[:].?\d[:].?\d[:].?\d/).join

puts "#{sender},#{receiver},#{flags}"

