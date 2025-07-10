#python has an INTEGER type called int

print("int")
print("******")
print(0)
print(1)
print(-1)
print("******")

#python has an REAL NUMBER type called float       

print("float")
print("******")
print(0.0)
print(1.0)
print(-1.0)
print(3.14)
print("******")

#python has a COMPLEX NUMBER type called complex
print("complex")        
print("******")
print(0j)
print(1j)
print(-1j)
print(3.14j)
print(1 + 2j)
print("******")

#python has a BOOLEAN type called bool
print("bool")
print("******")
print(True)
print(False)
print("******")

#python has a type called NoneType
print("NoneType")
print("******")
print(None)
print("******")

#python has a type called bytes
#bytes are IMMUTABLE sequences of bytes
#bytes CANNOT be MODIFIED after creation
print("bytes")
print("******")
print(b'hello')
print(b'world')
print(b'123')   
print(b'\x00\x01\x02')  # bytes with hex values
print("******")

#python has a type called bytearray
#bytearray are MUTABLE sequences of bytes
#bytearray can be MODIFIED after creation
print("bytearray")
print("******")
print(bytearray(b'hello'))  
print(bytearray(b'world'))
print(bytearray(b'123'))
print(bytearray(b'\x00\x01\x02'))  # bytearray with hex values
print("******")

#python has a type called memoryview
print("memoryview")
print("******")
data = bytearray(b'hello world')
mv = memoryview(data)
print(mv)  # memoryview of bytearray
print(mv[0:5])  # slicing memoryview
print(mv[6:11])  # slicing memoryview
print(bytes(mv[0:5]))   # Shows b'hello'
print(bytes(mv[6:11]))  # Shows b'world'
#print(bytes(memoryview(data)[0:5]))  # Shows b'hello'
print("******")

#python has a type called conversion    
print("conversion")
print("******")
print(int(3.14))  # converting float to int
print(float(3))  # converting int to float
print(complex(1, 2))  # converting to complex
print(bool(1))  # converting int to bool
print(bool(0))  # converting int to bool
print(str(123))  # converting int to str
print("******")

#python has a type called type
print("type")
print("******")
print(type(1))  # type of int
print(type(1.0))  # type of float
print(type(1 + 2j))  # type of complex
print(type(True))  # type of bool
print(type(None))  # type of NoneType
print(type(b'hello'))  # type of bytes
print(type(bytearray(b'hello')))  # type of bytearray
print(type(memoryview(bytearray(b'hello'))))  # type of memoryview
print("******")

#python has a type called id
print("id")
print("******")
print(id(1))  # id of int
print(id(1.0))  # id of float
print(id(1 + 2j))  # id of complex
print(id(True))  # id of bool
print(id(None))  # id of NoneType
print(id(b'hello'))  # id of bytes
print(id(bytearray(b'hello')))  # id of bytearray
print(id(memoryview(bytearray(b'hello'))))  # id of memoryview
print("******")

#python has a type called isinstance
print("isinstance")
print("******")
print(isinstance(1, int))  # check if int
print(isinstance(1j, float))  # check if float
print(isinstance(1 + 2j, complex))  # check if complex
print(isinstance(True, bool))  # check if bool
print(isinstance(None, type(None)))  # check if NoneType
print(isinstance(b'hello', bytes))  # check if bytes
print(isinstance(bytearray(b'hello'), bytearray))  # check if bytearray
print(isinstance(memoryview(bytearray(b'hello')), memoryview))  # check if memory
print("******")

#python has a type called isinstance with multiple types
print("isinstance with multiple types")
print("******")
print(isinstance(1, (int, float)))  # check if int or float
print(isinstance(1.0, (int, float)))  # check if int or float
print(isinstance(1 + 2j, (int, float, complex)))  # check if int, float, or complex
print(isinstance(True, (bool, int)))  # check if bool or int
print(isinstance(None, (type(None),)))  # check if NoneType
print(isinstance(b'hello', (bytes, bytearray)))  # check if bytes or bytearray
print(isinstance(bytearray(b'hello'), (bytes, bytearray)))  # check if bytes or bytearray
print(isinstance(memoryview(bytearray(b'hello')), (bytes, bytearray, memoryview)))  # check if bytes, bytearray, or memoryview
print("******")

#python has a type called isinstance with custom classes
print("isinstance with custom classes")
print("******")
class MyClass:
    pass # used as a placeholder for a class definition as currently this class does not have any attributes or methods            
class MySubClass(MyClass):
    pass    
print(isinstance(MyClass(), MyClass))  # check if instance of MyClass
print(isinstance(MySubClass(), MySubClass))  # check if instance of MySubClass
print(isinstance(MyClass(), MySubClass))  # check if instance of MyClass
print(isinstance(MySubClass(), MyClass))  # check if instance of MyClass    
print(isinstance(MyClass(), (MyClass, MySubClass)))  # check if instance of MyClass or MySubClass
print(isinstance(MySubClass(), (MyClass, MySubClass)))  # check if instance of MyClass or MySubClass
print("******")
#python has a type called isinstance with built-in types
print("isinstance with built-in types") 
print("******")
print(isinstance(1, (int, float, complex)))  # check if int, float, or complex
print(isinstance(1.0, (int, float, complex)))  # check if int, float, or complex
print(isinstance(1 + 2j, (int, float, complex)))  # check if int, float, or complex
print(isinstance(True, (bool, int)))  # check if bool or int    
print(isinstance(None, (type(None),)))  # check if NoneType
print(isinstance(b'hello', (bytes, bytearray)))  # check if bytes or bytearray
print(isinstance(bytearray(b'hello'), (bytes, bytearray)))  # check if bytes or bytearray
print(isinstance(memoryview(bytearray(b'hello')), (bytes, bytearray, memoryview )))  # check if bytes, bytearray, or memoryview
print("******") 

#python has a type called isinstance with custom types      
print("isinstance with custom types")
print("******")
class CustomType:
    pass
class AnotherCustomType:
    pass
print(isinstance(CustomType(), CustomType))  # check if instance of CustomType
print(isinstance(AnotherCustomType(), AnotherCustomType))  # check if instance of Another
print(isinstance(CustomType(), (CustomType, AnotherCustomType)))  # check if instance of CustomType or AnotherCustomType
print(isinstance(AnotherCustomType(), (CustomType, AnotherCustomType)))  # check if instance of CustomType or AnotherCustomType
print("******")

#python has a type called isinstance with built-in types and custom types
print("isinstance with built-in types and custom types")
print("******")
print(isinstance(1, (int, float, complex, CustomType)))  # check if int, float, complex, or CustomType
print(isinstance(1.0, (int, float, complex, CustomType)))  # check if int, float, complex, or CustomType
print(isinstance(1 + 2j, (int, float, complex, CustomType)))  # check if int, float, complex, or CustomType
print(isinstance(True, (bool, int, CustomType)))  # check if bool, int, or CustomType
print(isinstance(None, (type(None), CustomType)))  # check if NoneType or CustomType
print(isinstance(b'hello', (bytes, bytearray, CustomType)))  # check if bytes, bytearray, or CustomType
print(isinstance(bytearray(b'hello'), (bytes, bytearray, CustomType)))  # check if bytes, bytearray, or CustomType
print(isinstance(memoryview(bytearray(b'hello')), (bytes, bytearray, memoryview, CustomType)))  # check if bytes, bytearray, memoryview, or CustomType
print("******")

#python has a type called isinstance with multiple custom types
print("isinstance with multiple custom types")  
print("******")
class CustomType1:
    pass    
class CustomType2:
    pass    
print(isinstance(CustomType1(), CustomType1))  # check if instance of CustomType1
print(isinstance(CustomType2(), CustomType2))  # check if instance of CustomType2
print(isinstance(CustomType1(), (CustomType1, CustomType2)))  # check if instance of CustomType1 or CustomType2
print(isinstance(CustomType2(), (CustomType1, CustomType2)))  # check if instance of CustomType1 or CustomType2
print("******") 
#python has a type called isinstance with built-in types and multiple custom types
print("isinstance with built-in types and multiple custom types")
print("******")
print(isinstance(1, (int, float, complex, CustomType1, CustomType2)))  # check if int, float, complex, CustomType1, or CustomType2
print(isinstance(1.0, (int, float, complex, CustomType1, CustomType2)))  # check if int, float, complex, CustomType1, or CustomType2
print(isinstance(1 + 2j, (int, float, complex, CustomType1, CustomType2)))  # check if int, float, complex, CustomType1, or CustomType2
print(isinstance(True, (bool, int, CustomType1, CustomType2)))  # check if bool, int, CustomType1, or CustomType2
print(isinstance(None, (type(None), CustomType1, CustomType2)))  #  check if NoneType, CustomType1, or CustomType2
print(isinstance(b'hello', (bytes, bytearray, CustomType1, CustomType2)))  # check if bytes, bytearray, CustomType1, or CustomType2
print(isinstance(bytearray(b'hello'), (bytes, bytearray, CustomType1, CustomType2)))  # check if bytes, bytearray, CustomType1, or CustomType2
print(isinstance(memoryview(bytearray(b'hello')), (bytes, bytearray, memoryview , CustomType1, CustomType2)))  # check if bytes, bytearray, memoryview, CustomType1, or CustomType2
print("******") 


