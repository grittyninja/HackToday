puts "Hi, please input your calculation here, finished with '='"
puts "Example: 6+5="
STDOUT.flush
$/ = "="
input = STDIN.gets()
input = input.split(/=/).first
#input = gets("\t\n")
if /^([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)$/.match(input)
  puts eval(input)
else
  puts("no cheating")
end

STDOUT.flush



