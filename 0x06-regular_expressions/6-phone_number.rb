#!/usr/bin/env ruby
# A regular expression that matches a given pattern
puts ARGV[0].scan(/^[0-9]{10}$/).join
