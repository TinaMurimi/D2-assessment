class Base:
    def m(self):
        print("m of Base called")
    pass

class A(Base):
    # def m(self):
    #     print("m of A called")
    pass

class B(A):
    # def m(self):
    #     print("---m of B called---")
    #     # A.m(self)
    pass



# print("\nClass B")
# B().m()


class C(A):
    def m(self):
        print("---m of C called---")
        # A.m(self)
    pass


print("\nClass C")
C().m()

class D(B, C):
    pass

# class D(B,C):
#     def m(self):
#         print("m of D called")



print("\nClass D")
x = D()
x.m()
