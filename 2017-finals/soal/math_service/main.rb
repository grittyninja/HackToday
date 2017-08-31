input = $stdin.read
if /^([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)$/.match(input)
  puts eval(input)
else
  puts("no cheating")
end




