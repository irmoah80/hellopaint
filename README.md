# Hellopaint!
a very simple paint use QT in python. the aim of this project is to make the paint app via **undo/redo** function. Thanks for "geeksforgeeks" website.

# Algorithm of Undo/Redo implemention
In this case , we use **stack** dsa. by using 2 Stacks , named **stack_main** and  **stack_cach**. **main** is use for **undo** function and on the other hand **cache** used for **redo** function.

##  **Redo Algorithm** :
first check the base of algorithm :

> 1 - by press "Ctrl+Z" function called
> 1.5 - if **main**  is last empty (except the white fill at first) go ahead
> 2 - push **pop** of **main** in **cache**
> 3 - equal the **Canvas** image to **top** of **main** stack
> 4 - done!

before implement undo/redo function , we need to push each level in **main stack** :

    def  mouseReleaseEvent(self, e):
	    if  e.button() == Qt.LeftButton:
			self.ur.push(self.pixmap().copy()) #push in main stack
			...
**ur** is an object , from *UndoRedo* from undo_redo.py , push function :

    def  push(s , v):
	    if  not  s.stack_cach.is_empty():
		    s.c_cach()
		    s.stack_main.push(v)

In this project , we have **3 undo** function for this way , first & second at **main.py** :

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

We want to make an **Widget** for paint area , in main window , this is the reason of class " Canvas " :

	class  MainWindow(QMainWindow):
		def  __init__(self):
			super().__init__()
			...
			l = QtWidgets.QVBoxLayout() # vertical layout
			w.setLayout(l)
			l.addWidget(self.canvas)

the next and last one is undo function in **undo_redo.py** :

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
the `QApplication.beep()` is make a default error **beep** in your OS , and , for the condition , ````s.stack_main.size() == 1```` , cause is we have not delete the **white** screen that push it manually at the first.

##  **Undo Algorithm** :
like the previous , first , let check the base algorithm



