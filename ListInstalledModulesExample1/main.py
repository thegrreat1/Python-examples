import pkgutil
installed_modules = 0

for modules in pkgutil.iter_modules():
    installed_modules = installed_modules + 1
    print("---> Module name: {} \n".format(modules.name))

print("---------{} modules found".format(installed_modules))
