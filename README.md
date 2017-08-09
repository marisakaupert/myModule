My Module is a UI that creates models, prints custom greetings to the Script Editor, and allows you to find the three most common words of a text file.

Put myModule.py in your Maya scripts directory or add the folder with myModule.py to your python path.
Type this into the Script Editor:
```python
import myModule
reload(myModule)
myModule.run()
```
