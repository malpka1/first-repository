list_= [7, 10, 23, -19, 80]
list_.sort()
print(list_)
list_.extend(["20", "21"])
print(list_)
list_1 =[-19,7, 10, 20, 21, 23, 80]
print (list_1[0:7:2])
print(list_1.count (20))
list_1.index(20)
print (list_.insert(-19,20))
tuple_ = (4, 8, 12)
print(tuple_)
print (len (tuple_))
print (tuple_ [0] )
print ( tuple_*1)
contacts = { "имя" : "Vera", "возраст" : "30", "семья" : "муж", "профессия" : "учитель" }
print (contacts)
print (contacts.get("имя"))
contacts["профессия"] ="повар"
print (contacts)
contacts["семья"] = "муж","сын"
print (contacts)
contacts["пол"] = "ж"
print (contacts)
contacts.pop("пол")
print (contacts)