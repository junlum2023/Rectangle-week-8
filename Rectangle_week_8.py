from dataclasses import data dataclass

@dataclass
class Rectanngle:
    height: int
    width: int
    
    def getPerimeter(self):
        perimeter = self.height * 2 + self.width * 2
        return perimeter 
    
    def getArea(self):
        area = self.height * self.width
        return area 
    

    def getStr(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.height - 2):
            s += "*"
            s += "  " * (self.width - 2)
            s += "* \n"
        s += w
        return s
    def main():
        print("Rectangle Calculator")
        print()
        
        again = "y"
        while again.lower() == "y":
            height = int(input("Height: "))
            width = int(input("Width: "))
        
            rectangle = rectangle(height, width)
            print("Perimeter:", rectangle.getPerimeter())
            print("Area:", rectangle.getArea())
        
            again = input("Continue? (y/n): ").lower()
        print("Bye!")
        
    if __name__ == "__main__":
        main()
        
    
