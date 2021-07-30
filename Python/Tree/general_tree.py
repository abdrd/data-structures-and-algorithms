"""
    General tree in Python
"""

class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.children: list[Tree] = []
        self.parent: Tree = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def draw(self):
        prefix = ("  " * self.get_depth()) + "|__ " if self.parent else ""
        print(prefix + self.value)
    
        if self.children:    
            for c in self.children:
                c.draw()

    def get_depth(self):
        depth = 0
        p = self.parent
        while p:
            depth += 1
            p = p.parent

        return depth

"""
tree = Tree("Root")
print(tree.children)

tree.add_child("Second")
tree.add_child("Third")

for c in tree.children:
    print("\t-- ", c.value)

"""

src_directory = Tree("src/")
components_directory = Tree("components/")

navbar_dir = Tree("Navbar/")
navbar_comp = Tree("Navbar.tsx")
navbar_dir.add_child(navbar_comp)

home_dir = Tree("Home/")
home_comp = Tree("Home.tsx")
home_dir.add_child(home_comp)
home_dir.add_child(navbar_dir)

auth_dir = Tree("Auth/")
login_dir = Tree("Login/")
login_comp = Tree("Login.tsx")
login_dir.add_child(login_comp)
auth_dir.add_child(login_dir)
register_dir = Tree("Register/")
auth_dir.add_child(register_dir)
register_comp = Tree("Register.tsx")
register_dir.add_child(register_comp)

components_directory.add_child(auth_dir)
components_directory.add_child(home_dir)

src_directory.add_child(components_directory)

gitignore = Tree(".gitignore")
package_json = Tree("package.json")

src_directory.add_child(gitignore)
src_directory.add_child(package_json)

src_directory.draw() # v
"""
src/
  |__ components/       
    |__ Auth/
      |__ Login/        
        |__ Login.tsx   
      |__ Register/     
        |__ Register.tsx
    |__ Home/
      |__ Home.tsx      
      |__ Navbar/       
        |__ Navbar.tsx  
  |__ .gitignore        
  |__ package.json
"""