# Hellopaint!
A very simple paint use QT library in python. the aim of this project is to make the paint app via **undo/redo** function. Thanks for "[geeksforgeeks](https://www.geeksforgeeks.org/pyqt5-create-paint-application/)" website and our TA "Ali Shafiee".

# Algorithm of Undo/Redo implemention
In this case , we use **stack** dsa. by using 2 Stacks , named **stack_main** and  **stack_cach**. **main** is use for **undo** function and on the other hand **cache** used for **redo** function. The idea is to Save (capture) a frame when user release the left click.



##  **Redo Algorithm** :
First check the base of algorithm :

> 1 - by press "Ctrl+Z" function called
> 
> 1.5 - if **main**  is last empty (except the white fill at first) go ahead
> 
> 2 - push **pop** of **main** in **cache**
> 
> 3 - equal the **Canvas** image (here we have **pixmap**) to **top** of **main** stack
> 
> 4 - done!

Before implement undo/redo function , we need to push each level in **main stack** :

```python
    def  mouseReleaseEvent(self, e):
	    if  e.button() == Qt.LeftButton:
			self.ur.push(self.pixmap().copy()) #push in main stack
			...
```
**ur** is an object , from *UndoRedo* from undo_redo.py , push function :
```python
    def  push(s , v):
	    if  not  s.stack_cach.is_empty():
		    s.c_cach()
		    s.stack_main.push(v)
```
The `s.c_cach()` is function that clear the **cache** , why? When we draw after (for example) 3 undo, the indexes stored in the cache will be unused , as result , we have to clear **cache** stack.

In this project , we have **3 undo** function for this way , first & second at **main.py** :
```python
    class  Canvas(QLabel):
	    ...
	    def  undo(self):
		    x = self.ur.undo()
			if  x != False:
				self.setPixmap(x)
				self.update()
	
	class  MainWindow(QMainWindow):
		def  undo(s):
			s.canvas.undo()
```
We want to make an **Widget** for paint area , in main window , this is the reason of class " Canvas " :
```python
	class  MainWindow(QMainWindow):
		def  __init__(self):
			super().__init__()
			...
			l = QtWidgets.QVBoxLayout() # vertical layout
			w.setLayout(l)
			l.addWidget(self.canvas)
```
the next and last one is undo function in **undo_redo.py** :
```python
    import stack
    from PyQt5.QtWidgets import QApplication
	    class UndoRedo:
	    ...
		    def undo(s):
			    if s.stack_main.size() == 1 :
				    QApplication.beep()
				    return s.stack_main.top()
				
				s.stack_cach.push(s.stack_main.pop())
				return s.stack_main.top()
```
the `QApplication.beep()` is make a default error **beep** in your OS , and , for the condition , ````s.stack_main.size() == 1```` , cause is we have not delete the **white** screen that push it manually at the first.

##  **Undo Algorithm** :
like the previous , first , let check the base algorithm:

> 1- By pressing  " Ctrl+Alt+Z " the function is called
> 
> 1.5- if the **cache** stack is not empty , continue
> 
> 2- push **pop** of **cache** in **main**
> 
> 3- equal the **Canvas** image to **top** of **main** stack
> 
> 4- done!

like the Undo function , we have 3 Redo Function , at the same position.

##  **Why "RedoUndo" Class?** :

Just because we want make a clean project :). this class is in " undo_redo.py " and the work is to manage the "undo & redo" task.
It has 3 main function : push , undo & redo :

```python
    class UndoRedo:
	    stack_main = None
	    stack_cach = None
	    def __init__(self) -> None:
		    self.stack_main = stack.Stack()
		    self.stack_cach = stack.Stack()
		    
		def push(s , v):
		    ...
		def undo(s , v):
			...
		def redo(s , v):
			...
```
#  Shortcuts :
Based on photoshop shortcuts :))

| function | shortcut keys |
|--|--|
| Undo | `Ctrl + Z` |
| Redo | `Ctrl + Alt + Z` |
| Save | `Ctrl + S` 



