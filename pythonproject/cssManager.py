import random

class css:

    def __init__(self, cssfile):
        print("in css class")
        file = open(cssfile, 'r')
        CSStext = file.read()
        file.close()
        List = []
        file = open(cssfile, 'r')
        for i in file.readlines():
            List.append(i)
        file.close()
        print(List)
        self.ListContent = List
        self.cssContent = CSStext
        self.CSSFile =  cssfile
    def refresh(self):
        text = ''
        for i in self.ListContent:
            text += i
        self.cssContent = text
        file = open(self.CSSFile, 'w')
        file.write(self.cssContent)
        file.close()
    def toList(self,ob):
        li = []
        for i in ob:
            li.append(i)
        return li
    def decoder(self, li):
        if 'bg' in li:
            if li == 'bg-c' :
                return 'background-color'
        elif 'c' == li:
            return 'color'
        elif 'w' == li:
            return 'width'
        elif 'h' == li:
            return 'height'
        elif 'f' in li:
            if 'f-fm' == li:
                return 'font-family'
            elif 'f-sz' == li:
                return 'font-size'
    def write(self, selector, elem):
        elements = self.toList(elem)

        if selector in self.cssContent:
            NewList = []
            cindex = 0
            string = ''
            print(self.decoder(elements[0]))
            print(elem[elements[0]])
            for i in range(len(self.ListContent)):
                try:
                    deEl = self.decoder(elements[cindex])
                    if  deEl in self.ListContent[i]: 
                        string =self.ListContent[i].replace(self.ListContent[i], deEl+':'+elem[elements[cindex]]+';\n') 
                        cindex += 1
                        NewList.append(string)
                    else:
                        NewList.append(self.ListContent[i])
                except:
                    NewList.append(self.ListContent[i])
            print(NewList)
            self.ListContent = NewList
            self.refresh()
        else:
            self.ListContent.append(selector+'{\n')
            for i in elements:
                self.ListContent.append(self.decoder(i) +':'+ elem[i]+';\n')
            self.ListContent.append('}')
            self.refresh()


class CssRand:
    def __init__(self):
        print('css-randoms')

    def color(self):
        char = 'ABCDEF'
        color = '#'
        for i in range(0,6):
            x = random.randrange(0,15)
            if x > 9:
                c = x - 10
                color += char[c]
            else:
                color += str(x)
        return color
       
    def rgb(self):
        rgb = 'rgb('
        for i in range(0,3):
            if i < 2:
                rgb += str(random.randrange(0,256))+','
            else:
                rgb += str(random.randrange(0,256))
        rgb += ')'
        return rgb
           
