from configparser import ConfigParser

file = 'config.ini'

config=ConfigParser()
config.read(file)



print(config.sections())
print("*"*5)

print(list(config['account']))
print("*"*5)

print(config['account']['Status'])

config.add_section('Bank')
config.set('Bank','Name','HSBC')

with open(file,'w') as config_w:
    config.write(config_w)