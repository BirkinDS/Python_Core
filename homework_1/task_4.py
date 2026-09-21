# task description
# В строке "Ivanou Ivan" поменяйте местами слова:"Ivanou Ivan" => "Ivan Ivanou"

# solution
s = "Ivanou Ivan"
parts = s.split()
s = parts[1] + " " + parts[0]
print(s)
