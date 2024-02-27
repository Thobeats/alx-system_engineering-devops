#!/usr/bin/env ruby
# write a regex that matched the expression "hbt**n"

puts ARGV[0].scan(/h[a-zA-Z0-9]{1}n/).join
