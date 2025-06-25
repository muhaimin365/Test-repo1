print ("***********Set Operation**********")

set_a={10,20,30,40,50}
set_b={40,50,60,70,80}
print(f"Set_A:{set_a}")
print(f"Set_B:{set_b}")

unione_set= set_a.union(set_b)
print(f"union of a& b: {unione_set}")

interset_set = set_a.intersection(set_b)
print(f"intersection of a& b: {interset_set}")

different_set = set_a.difference(set_b)
print(f"difference of a& b: {different_set}")

list_a=[10,20,30,20,30,40]
list_b=[40,50,60,20,30,40]

print(f"List_A:{list_a}")
print(f"List_B:{list_b}")

unique_element_set=set(list_a)
print(f"remove the duplicate: {unique_element_set}")

unique_element_list=list(unique_element_set)
print(f"print again with duplicate: {unique_element_list}")
