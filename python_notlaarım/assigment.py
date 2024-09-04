values = 1, 2, 3

x, y, z = values

print(values)

print(type(values))

# fazla değer olursa x y x denilince çıktı gelmez. *z liste yapılır  çıktı 1 2 [3, 4, 5] böyle olur
values = 1, 2, 3, 4, 5

x, y, *z = values
print(x, y, z)

# ortadakiler liste olur :
x, *y, z = values
print(x, y, z)

#**********************************************
# x, *y, z = values işlemine göre y nin değerleri toplamı kaçtır

values = 1, 2, 3, 4, 5
x, *y, z = values

result = y[0] + y[1] + y[2]

print(result)
