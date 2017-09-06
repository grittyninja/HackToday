$/ = "="
input = STDIN.gets()
input = input.split(/=/).first
STDOUT.flush
#input = gets("\t\n")
if /^([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)$/.match(input)
  puts eval(input)
  STDOUT.flush
else
  puts("no cheating")
  STDOUT.flush
end




