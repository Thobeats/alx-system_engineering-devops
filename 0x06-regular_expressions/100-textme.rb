#!/usr/bin/env ruby
# write a regex that matched the expression "hbt**n"

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
