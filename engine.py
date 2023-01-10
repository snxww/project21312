def func_gen():
    for _ in [27, 587,114 ]:
        yield _

gen_interetor = func_gen().__iter__()
for _ in rage (1,4):
    print(gen_interetor.__next__())

print(type(gen_interetor))
print(iter([27,587,114]))