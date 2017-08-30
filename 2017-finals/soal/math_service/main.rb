puts("Selamat Datang Di Math Service")
puts("Kamu bisa menghitung disini")
input = gets

#regex check
# ^([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)$

valid = false


if /^([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)$/.match(input)

  puts(eval(input))
else
  puts("no cheating")
end




