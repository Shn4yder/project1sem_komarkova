import module
import figures

# module.get_set()

# module.get_txt()

# print(module.list_doc.doc)

print(module.file_doc.doc)

# print(dir(module))

print(figures.circle_area())
print(figures.triangle_area())
print(figures.square_area())

"""
    Таким образом, если изменить имя пакета figure на другое и импортирорвать библиотеку с другим именем, то результат 
    будет прежним - нигде явно не использовалось имя figure.
"""
