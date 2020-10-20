# class A:
#     x = [1, 2, 3]

# class B:
#     y = A()
#     z = 2

# obj = B()
# if obj.y.x.index(obj.z) == 1:
#     print(True)
# else:
#     print(False)

class Sentence:
    
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

    

def sentence(sentence):
    for word in sentence.split():
        yield word

my_sentence = sentence('This is a test')



print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
