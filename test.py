import os


set_modules = set()
set_files_and_folder = set()
for root, dirs, files in os.walk("."):
    for dir in dirs:
        set_files_and_folder.add(dir)
    for file in files:
        set_files_and_folder.add(file.split('.')[0])
        fp = os.path.join(root, file)
        if not fp.endswith('.py'):
            continue
        with open(fp, 'r') as f:
            for line in f:
                if line.startswith('from'):
                    line = line.split(' ')[1]
                    set_modules.add(line.strip())
                elif line.startswith('import'):
                    line = line.split(' ')[1]
                    set_modules.add(line.strip())
                    
real_modules = set()                    
for module_ in set_modules:
    for module in set_files_and_folder:
        if module not in module_:
            real_modules.add(module_.split('.')[0])
            break
            
print(real_modules)
print("main_app" in set_files_and_folder)
print("main_app.views.controller.c_main_window" in set_modules)